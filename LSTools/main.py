import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tools_view import Ui_mainWindow
from tools.studio_control import *


class MainWindow(QMainWindow):
    def __init__(self, bts: list):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow(bts)
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bts = [
        {"text": "日志文件夹", "func": open_logs_dir},
        {"text": "多语言文件夹", "func": open_language_dir},
        {"text": "branch切换", "func": switch_branch},
        {"text": "清除美颜", "func": update_effects},
        {"text": "清除场景", "func": clear_screen},
        {"text": "生成完成PK参数", "func": generate_finsh_pk}
    ]
    mainWindow = MainWindow(bts=bts)
    mainWindow.show()
    sys.exit(app.exec_())
