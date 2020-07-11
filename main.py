import sys

from itertools import islice
from grammar_parser import mk_parser, Tokens
from grammar_lex import lexer, lexer_lazy_bytes, BOF, EOF

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

from sortedcontainers import SortedKeyList
from intervaltree import Interval, IntervalTree
from theme import Theme
import theme
import itertools
import numbers
import time as py_time


class MutInt(numbers.Number):
    __slots__ = ['i']
    def __init__(self, i):
        numbers.Number.__init__(i)
        self.i = i
    
    def __repr__(self):
        return repr(self.i)
    
    def __eq__(self, o):
        return isinstance(o, MutInt) and self.i == o.i or self.i == o

    def __ge__(self, o):
        return isinstance(o, MutInt) and self.i >= o.i or self.i >= o

    def __le__(self, o):
        return isinstance(o, MutInt) and self.i <= o.i or self.i <= o


    def __gt__(self, o):
        return isinstance(o, MutInt) and self.i > o.i or self.i > o

    def __lt__(self, o):
        return isinstance(o, MutInt) and self.i < o.i or self.i < o
    
    def __add__(self, o):
        return _mki(self.i + (isinstance(o, MutInt) and o.i or o))
    
    def __sub__(self, o):
        return _mki(self.i - (isinstance(o, MutInt) and o.i or o))
    
    def __mul__(self, o):
        return _mki(self.i * (isinstance(o, MutInt) and o.i or o))
    
    def __truediv__(self, o):
        return self.i / (isinstance(o, MutInt) and o.i or o)
    
    def __floordiv__(self, o):
        return _mki(self.i // (isinstance(o, MutInt) and o.i or o))
    
    def __hash__(self):
        return hash((MutInt, self.i))

_mki = MutInt

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
                 filename="unknown"
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
        self.intervals = IntervalTree()
        self.text_changing_timer = None
        self.diffs = []

        
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
            self.diffs.append((start, change_len))
        elif typ & QsciScintilla.SC_MOD_DELETETEXT:
            self.diffs.append((start, -change_len))

    def _modify(self):
        if self.text_changing_timer is None:
            self.text_changing_timer = py_time.time()
        elif py_time.time() - self.text_changing_timer > 0.08:
            diffs = self.diffs
            if not diffs:
                self.text_changing_timer = None
                return
            print(diffs)
            for head, deltas in itertools.groupby(diffs, key=lambda x: x[0]):
                change_len = 0
                affected_old_bound = head + 1
                new_buffer = 0
                for _, delta in deltas:
                    change_len += delta
                    if delta < 0:
                        delta = -delta
                        if not new_buffer:
                            affected_old_bound += delta
                        elif delta > new_buffer:
                            affected_old_bound += delta - new_buffer
                            new_buffer = 0
                        else:
                            new_buffer -= delta
                    else:
                        new_buffer += delta

                intervals = self.intervals
                
                print('all intervals', intervals)
                affected = sorted(intervals[head: affected_old_bound])
                print('affected intervals', affected)
                if affected:
                    start = affected[0].begin.i
                    end = affected[-1].end.i
                    intervals.remove_overlap(start, end)
                else:
                    start = head
                    end = self.parent().length()
                
                for adjust in self.intervals[end:]:
                    adjust.begin.i += change_len
                    adjust.end.i += change_len
                
                self._set_style(start, end)
            diffs.clear()
            self.text_changing_timer = None
        
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
        print(f'[{start}, {end})')
        
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

        parser = mk_parser(s=_handler, ss=_handler_many, partial_ok=partial_ok)
        editor = self.parent()
        qt_bytes = editor.bytes(0, editor.length())
        print(qt_bytes)
        qt_bytes = qt_bytes[start:end]
        print(qt_bytes)
        # qt_bytes = editor.bytes(start, end - 1)

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
                last_end = start + last_token.offset + len(last_token.value) + 1
                intervals[_mki(last_start):_mki(last_end)] = None
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
                intervals[_mki(last_start): _mki(last_end)] = None
                last_start = last_end
                bof_token.offset = last_start
                token_offset = tokens.offset - 1
                tokens.offset = token_offset
                tokens.array[token_offset] = bof_token
    
        print('updated', intervals)

class TestApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(50, 200, 1000, 1000)
        self.__frm = QFrame(self)
        self.__frm.setStyleSheet("QWidget { background-color: #ffeaeaea }")
        self.__lyt = QVBoxLayout()
        self.__frm.setLayout(self.__lyt)
        self.setCentralWidget(self.__frm)

        editor = self.editor = QsciScintilla(self)

        self.__lexer = My(editor)
        editor.setLexer(self.__lexer)
        self.__lyt.addWidget(editor)

        self.setWindowTitle("frontend-for-free")


app = QApplication(sys.argv)
QApplication.setStyle(QStyleFactory.create('Fusion'))
test = TestApp()
test.show()
sys.exit(app.exec_())
