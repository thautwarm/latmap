from lib import *
import mylisp_lex
import mylisp_parser
app = QApplication(sys.argv)
QApplication.setStyle(QStyleFactory.create('Fusion'))
test = MyEditor(mylisp_parser, mylisp_lex)
test.show()
sys.exit(app.exec_())
