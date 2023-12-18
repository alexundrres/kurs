from avtorizacia import Ui_avtorizacia
from prepodavatel import Ui_prepodavatel
from ychenik import Ui_ychenik
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
import sys
from bd import BD
from PyQt6.QtSql import QSqlTableModel


class Main(QMainWindow):
    def __init__(self):
        super().__init__()


        self.avtorizacia = QMainWindow()
        self.ui_avtorizacia = Ui_avtorizacia()
        self.ui_avtorizacia.setupUi(self.avtorizacia)

        self.prepodavatel = QMainWindow()
        self.ui_prepodavatel = Ui_prepodavatel()
        self.ui_prepodavatel.setupUi(self.prepodavatel)

        self.ychenik = QMainWindow()
        self.ui_ychenik = Ui_ychenik()
        self.ui_ychenik.setupUi(self.ychenik)

        self.bd = BD()
        self.output_1()
        self.output_2()

    # вывод бд на экран
    def output_1(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("ученики")
        self.model.select()
        self.ui_prepodavatel.tableView_prep.setModel(self.model)
    def output_2(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("ученики")
        self.model.select()
        self.ui_ychenik.tableView.setModel(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = Main()
    x.avtorizacia.show()
    x.prepodavatel.show()
    x.ychenik.show()
    sys.exit(app.exec())
