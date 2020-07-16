from lib import *
import rbnf_lex
import rbnf_parser
app = QApplication(sys.argv)
QApplication.setStyle(QStyleFactory.create('Fusion'))
test = MyEditor(rbnf_parser, rbnf_lex)
test.show()
sys.exit(app.exec_())
