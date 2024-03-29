from PyQt5.Qt import *
import sys
from function import get_all_net_card_info


class MainPage(QMainWindow):
    def __init__(self, title=" "):
        super().__init__()
        self.title = title
        self.x = 400
        self.y = 100
        self.width = 1300
        self.height = 800
        self.menubar = self.menuBar()
        self.frame1 = ButtonFrame()
        self.frame2 = SplitterFrame()
        self.fileMenu = self.menubar.addMenu('&文件')
        self.openaction = self.fileMenu.addAction('&打开')
        self.exitaction = self.fileMenu.addAction('&退出')
        self.saveaction = self.fileMenu.addAction('&保存')

        self.captureMenu = self.menubar.addMenu('&捕获')
        self.startaction = self.captureMenu.addAction('&开始')
        self.stopaction = self.captureMenu.addAction('&停止')

        self.analyseMenu = self.menubar.addMenu('&分析')
        self.helpMenu = self.menubar.addMenu('&帮助')
        self.aboutaction = self.helpMenu.addAction('&关于')

        self.widget()

    def widget(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.deal_menubar()

        self.frame1.setParent(self)

        self.frame2.setParent(self)

        self.show()

    def deal_menubar(self):

        self.openaction.setShortcut("Ctrl+O")

        self.exitaction.setShortcut("Ctrl+Q")

        self.saveaction.setShortcut("Ctrl+S")

        self.startaction.setShortcut("Ctrl+E")

        self.stopaction.setShortcut("Ctrl+T")

        # TODO

        self.aboutaction.setShortcut("F11")


class ButtonFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.button_width = 50
        self.button_height = 21
        self.start_button = QPushButton(self)
        self.stop_button = QPushButton(self)
        self.save_button = QPushButton(self)
        self.frame()

    def frame(self):
        self.setGeometry(0, 25, 1928, 25)
        self.setStyleSheet("background-color:#ffffff")
        self.setFrameRect(QRect(0, 0, 1928, 25))

        self.start_button.setText("Start")
        self.start_button.setGeometry(2, 2, self.button_width, self.button_height)
        self.start_button.setStyleSheet("background-color:blue;color:#ffffff")

        self.stop_button.setText("Stop")
        self.stop_button.setGeometry(56, 2, self.button_width, self.button_height)
        self.stop_button.setStyleSheet("background-color:red;color:#ffffff")

        self.save_button.setText("Save")
        self.save_button.setGeometry(110, 2, self.button_width, self.button_height)
        self.save_button.setStyleSheet("background-color:green;color:#ffffff")


class SplitterFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.setParent(self)
        self.table = QTableWidget(0, 7)
        self.splitter.addWidget(self.table)
        # self.tree = QTreeWidget(self.splitter)
        self.label = QLabel(self.splitter)
        self.label1 = QLabel(self.splitter)
        self.frame()

    def frame(self):
        self.setGeometry(0, 50, 1928, 750)
        self.splitter.setGeometry(0, 0, 1300, 750)
        self.table.setHorizontalHeaderLabels(["No.", "Time", "Source", "Destination", "Protocol", "Length", "Info"])
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.verticalHeader().hide()

        # self.tree.setHeaderHidden(True)
        # for i in range(5):
        #     root = QTreeWidgetItem(self.tree)
        #     root.setText(0, "Root" + str(i))
        #     child1 = QTreeWidgetItem()
        #     child1.setText(0, "child1" + str(i))
        #     child2 = QTreeWidgetItem()
        #     child2.setText(0, "child2" + str(i))
        #     root.addChild(child1)
        #     root.addChild(child2)
        self.label.setStyleSheet("background-color:white")

        self.label1.setStyleSheet("background-color:white")

        self.splitter.setSizes([1000, 1000, 1000])


class StartPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.card = ""
        self.frame()

    def frame(self):
        netcard = [card for card in sorted(get_all_net_card_info())]
        item, ok = QInputDialog.getItem(self, "choose your net card", '网卡列表', netcard, 0, False)
        if not ok or not item:
            exit(0)
        self.card = item


# def main():
#     app = QApplication(sys.argv)
#
#     startpage = StartPage()
#     global mainpage
#     mainpage = MainPage("my_sniffer--" + card)
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     main()
