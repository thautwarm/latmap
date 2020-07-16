import sys

from itertools import islice
from lclisp_parser import mk_parser, Tokens
from lclisp_lex import lexer, lexer_lazy_bytes, BOF, EOF

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

from sortedcontainers import SortedKeyList
from theme import Theme
import theme
import itertools
import numbers
import time as py_time
from pyximport import install
install()
import avl


class LazyArray:
    __slots__ = ['data', 'gen']

    def __init__(self, gen):
        self.data, self.gen = [], gen

    def __getitem__(self, i):
        data = self.data
        try:
            return data[i]
        except IndexError:
            n = i - len(data) + 24  # 24 is a parameter, must >= 1
            data.extend(islice(self.gen, n))
            return data[i]

    def __setitem__(self, i, v):
        data = self.data
        try:
            data[i] = v
        except IndexError:
            n = i - len(data) + 24  # 24 is a parameter, must >= 1
            data.extend(islice(self.gen, n))
            data[i] = v


class My(QsciLexerCustom):

    def __init__(self,
                 parent,
                 parser_module,
                 lexer_module,
                 filename="unknown",
                 ):
        super().__init__(parent)
        self.setDefaultFont(QFont("Consolas", 14))

        for each in Theme:
            for style in each.value:
                if isinstance(style, QColor):
                    self.setColor(style, each.style_id)

        def show(pos, mod):
            print(pos, mod)
        parent.SendScintilla(parent.SCI_STYLESETHOTSPOT, 1, True)
        parent.SCN_HOTSPOTCLICK.connect(show)
        # parent.textChanged.connect(self._text_change)
        parent.SCN_MODIFIED.connect(self._modify_signal)

        self.filename = filename
        self.intervals = avl.OrthogonalIntervals()
        self.diffs = []
        self.edit_point = None
        self.parser_module = parser_module
        self.lexer_module = lexer_module
        
    def description(self, style):
        return f"style_{style}"  # + Theme.name_of_style_id(style, "")

    def language(self):
        return "SimpleLanguage"

    def styleText(self, _, __):
        self._modify()

    def _modify_signal(self,
            start,
            typ,
            text_diff,
            change_len,
            lines_added,
            *_):

        if typ & QsciScintilla.SC_MOD_INSERTTEXT:
            diffs = self.diffs
            if not diffs:
                self.edit_point = start
            elif self.edit_point != start:
                self._modify()
                # then diffs are cleared
                self.edit_point = start
            diffs.append(change_len)
        elif typ & QsciScintilla.SC_MOD_DELETETEXT:
            diffs = self.diffs            
            if not diffs:
                self.edit_point = start
            elif self.edit_point != start:
                self._modify()
                # then diffs are cleared
                self.edit_point = start
            diffs.append(-change_len)
            
    def _modify(self):
        diffs = self.diffs
        if not diffs:
            return
        
        edit_point = self.edit_point
        change_len = 0
        delete_delta = 0
        new_buffer = 0

        for delta in diffs:
            change_len += delta
            if delta < 0:
                delta = -delta
                if not new_buffer:
                    delete_delta += delta
                elif delta > new_buffer:
                    delete_delta += delta - new_buffer
                    new_buffer = 0
                else:
                    new_buffer -= delta
            else:
                new_buffer += delta
        
            
        intervals = self.intervals
        insert_delta = change_len + delete_delta
    
        print(f'edit({edit_point}, {delete_delta}, {insert_delta})..')
        print('before edit', [node for node in intervals])
        any_affected = intervals.affect_edit(edit_point, delete_delta, insert_delta)
        print('after edit', [node for node in intervals])
        
        if any_affected is None:
            print('no affected')
            assert change_len > 0
            start = edit_point
            end = start + change_len
        else:
            print('affected', any_affected)
            start, end = any_affected 
        
        if start != end:
            self._set_style(start, end)
        diffs.clear()
    
        # print('=====')
        # print('start', start)
        # print('flag', hex(typ))
        # print(f"insert? {bool(typ & QsciScintilla.SC_MOD_INSERTTEXT)}")
        # print(f"delete? {bool(typ & QsciScintilla.SC_MOD_DELETETEXT)}")
        # print(f"lenchange {change_len}")
        # print(f"{self.parent().isModified()}")
        # diffs = self.diffs
        # if typ & QsciScintilla.SC_MOD_INSERTTEXT:
        #     diffs.append((start, change_len))
        # elif typ & QsciScintilla.SC_MOD_DELETETEXT:
        #     diffs.append((start, -change_len))

    def _set_style(self, start, end):
        print(f'START = [{start}, {end})')
        
        def _handler_many(*args):
            args = iter(args)
            handler = _handler
            _next = next
            while True:
                tk = _next(args, None)
                if not tk:
                    return
                style = _next(args)
                handler(tk, style)

        def _handler(tk, s):
            print(f'{tk.offset} : {tk.value} <- {s}')
            self.startStyling(start + tk.offset)
            self.setStyling(len(tk.value), s.style_id)

        def partial_ok():
            nonlocal is_partial_ok
            is_partial_ok = True

        parser_module = self.parser_module
        lexer_module = self.lexer_module

        mk_parser, Tokens = parser_module.mk_parser, parser_module.Tokens
        lexer_lazy_bytes = lexer_module.lexer_lazy_bytes

        parser = mk_parser(s=_handler, ss=_handler_many, partial_ok=partial_ok)
        editor = self.parent()
        qt_bytes = editor.bytes(0, editor.length())
        qt_bytes = qt_bytes[start:end]
        print(qt_bytes)
        
        token_generator = lexer_lazy_bytes(self.filename, qt_bytes)
        lazy_array = LazyArray(token_generator)

        intervals = self.intervals

        tokens = Tokens(lazy_array)

        bof_token = tokens.array[0]
        last_start = start
        last_end = last_start + 1
        token_offset = 0
        maybe_error_token = bof_token

        while True:
            is_partial_ok = False
            status, _ = parser(None, tokens)
            if status:
                last_token = tokens.array[tokens.offset - 1]
                last_end = start + last_token.offset + len(last_token.value)
                if last_end > last_start:
                    print(
                        qt_bytes[last_start-start:last_end-start],
                        'inserted as an interval',
                        f'[{last_start}, {last_end})'
                    )
                    intervals.insert(last_start, last_end, False)
                break

            if token_offset + 1 == tokens.offset:
                err_span = len(maybe_error_token.value)
                err_str_offset = start + maybe_error_token.offset
                last_end = err_str_offset + err_span + 1
                bof_token.offset = last_end
                self.startStyling(err_str_offset)
                self.setStyling(
                    err_span,
                    Theme.Error.style_id
                )
                maybe_error_token = tokens.array[tokens.offset]
                token_offset += 1
                tokens.offset = token_offset
                tokens.array[token_offset] = bof_token
            else:
                maybe_error_token = tokens.array[tokens.offset]
                last_end = maybe_error_token.offset
                if is_partial_ok and last_end > last_start:
                    print(last_start, last_end)
                    intervals.insert(last_start, last_end, True)
                    print(
                        qt_bytes[last_start-start:last_end-start],
                        'inserted as an interval',
                        f'[{last_start}, {last_end})'
                    )
                    last_start = last_end
                bof_token.offset = last_end
                token_offset = tokens.offset - 1
                tokens.offset = token_offset
                tokens.array[token_offset] = bof_token
        
        print('updated', [node for node in intervals])
        print('====')

class MyEditor(QMainWindow):
    def __init__(self, parser_module, lexer_module, filename="unknown"):
        QMainWindow.__init__(self)
        self.setGeometry(50, 200, 1000, 1000)
        self.__frm = QFrame(self)
        self.__frm.setStyleSheet("QWidget { background-color: #ffeaeaea }")
        self.__lyt = QVBoxLayout()
        self.__frm.setLayout(self.__lyt)
        self.setCentralWidget(self.__frm)
        
        save_file = QAction("&Save", self)
        save_file.setShortcut("Ctrl+S")
        save_file.setStatusTip('Save File')
        save_file.triggered.connect(self.save_file)
        
        open_file = QAction("&Open", self)
        open_file.setShortcut("Ctrl+O")
        open_file.setStatusTip('Open File')
        open_file.triggered.connect(self.open_file)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(save_file)
        fileMenu.addAction(open_file)
        

        editor = self.editor = QsciScintilla(self)

        self._lexer = My(editor, parser_module, lexer_module, filename)
        editor.setLexer(self._lexer)
        self.__lyt.addWidget(editor)

        self.setWindowTitle("frontend-for-free")

    def save_file(self):
        name, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if name:
            with open(name,'w') as file:
                text = self.editor.text()
                file.write(text)

    def open_file(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', directory='.')
        if name:
            with open(name, 'r') as file:
                text = file.read()
                self.editor.setText(text)
    
