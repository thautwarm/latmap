import sys

from itertools import islice
from grammar_parser import mk_parser, Tokens, handler
from grammar_lex import lexer, lexer_lazy_bytes, BOF, EOF

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

from sortedcollections import SortedList
from theme import Theme
import theme

parser = mk_parser()

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

        parent.SCN_MODIFIED.connect(self._modify)

        self.last_end = None
        self.filename = filename
        self.intervals = SortedList()
        self.modified_point = None

    def description(self, style):
        return f"style_{style}" # + Theme.name_of_style_id(style, "")

    def language(self):
        return "SimpleLanguage"

    def _modify(self, start, *_):
        if self.modified_point is None:
            self._style_set(0, self.parent().length())
        else:
            self.modified_point = start

    def styleText(self, _, block_end):
        self.modified_point > 0 and self._style_set(
            self.modified_point, block_end)

    def _style_set(self, start, block_end):
        print(start, self.intervals)
        editor = self.parent()
        end = editor.length()  # drop \x00
        last_end = self.last_end
        if last_end is None:
            assert start == 0
        else:
            p = last_end if last_end < start else start
            intervals = self.intervals
            n = intervals.bisect_left(p) - 1
            while len(intervals) != n:
                start = intervals.pop()

        def _handler(tk, s):
            print(f'{tk.offset} : {tk.value} <- {s}')
            self.startStyling(tk.offset)
            self.setStyling(len(tk.value), s.style_id)

        handler[0] = _handler

        qt_bytes = editor.bytes(0, end)
        print(qt_bytes)
        token_generator = lexer_lazy_bytes(self.filename, qt_bytes, pos=start)
        lazy_array = LazyArray(token_generator)

        intervals = self.intervals

        tokens = Tokens(lazy_array)
        token_offset = 0
        last_end = start
        last_start = start
        bof_token = tokens.array[0]
        maybe_error_token = bof_token

        while True:
            status, result = parser(None, tokens)

            # print(maybe_error_token)
            print(result)
            if status:
                
                last_end = tokens.array[tokens.offset - 1].offset
                intervals.add(last_start)
                break
            

            if token_offset + 1 == tokens.offset:
                err_span = len(maybe_error_token.value)
                err_str_offset = maybe_error_token.offset
                last_end = err_str_offset + err_span
                bof_token.offset = last_end + 1
                self.startStyling(err_str_offset)
                self.setStyling(
                    err_span,
                    Theme.Error.style_id
                )
                maybe_error_token = tokens.array[tokens.offset]
                token_offset += 1
                tokens.offset = token_offset
                tokens.array[token_offset] = bof_token

                if err_str_offset > block_end:
                    intervals.add(last_start)
                    break
            else:
                maybe_error_token = tokens.array[tokens.offset]
                last_token = tokens.array[tokens.offset]

                last_end = last_token.offset + len(last_token.value)
                intervals.add(last_start)
                last_start = last_end + 1

                bof_token.offset = last_start
                token_offset = tokens.offset - 1
                tokens.offset = token_offset
                tokens.array[token_offset] = bof_token

        self.modified_point = -1
        self.last_end = last_end

    #     prev_span = self.prev_span
    #     if not prev_span:
    #         prev_span = self.prev_span = start, end
    #     prev_start, prev_end = prev_span

    #     if start < self.prev_start
    #     editor = self.parent()
    #     token_gen = self.lexer(
    #         "filename", editor.bytes(start, editor.length()))
    #     lazy_array = LazyArray(token_gen)
    #     tokens = Tokens(lazy_array)
    #     self.parser(tokens)

    #     self.objs

        # text = self.parent().text()
        # _caches.add(text)
        # print(id(text))
        # def token(x, s):
        #     n = len(bytearray(x.value, "utf-8"))
        #     print('format: ', x.offset, n, s)
        #     self.setFormat(x.offset, n, s)

        # def tokens(*args):
        #     for i in range(0, len(args), 2):
        #         tk = args[i]
        #         s = args[i+1]
        #         token(tk, s)

    # def highlightBlock(self, text):
    #     def token(x, s):
    #         n = len(bytearray(x.value, "utf-8"))
    #         print('format: ', x.offset, n, s)
    #         self.setFormat(x.offset, n, s)
    #     def tokens(*args):
    #         for i in range(0, len(args), 2):
    #             tk = args[i]
    #             s = args[i+1]
    #             token(tk, s)
    #     p = mk_parser(token, tokens, keyword, lead, literal)
    #     print(text)
    #     st, x = p(None, Tokens(lexer("filename", text)))
    #     if not st:
    #         off, x = x

    #     print(x)


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
