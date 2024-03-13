import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from tools.studio_control import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle("tools")
        self.resize(800, 600)

        # label_toast = QLabel("status")

        # 创建按钮
        bt_open_log = QPushButton("日志文件夹", self)
        bt_language = QPushButton("多语言文件夹", self)
        bt_branch = QPushButton("branch切换", self)
        bt_update_effects = QPushButton("清除美颜", self)
        bt_clear_screen = QPushButton("清除场景", self)
        bt_generate_finsh_pk = QPushButton("生成完成PK参数", self)

        # 将按钮点击事件与自定义方法连接
        bt_open_log.clicked.connect(open_logs_dir)
        bt_language.clicked.connect(open_language_dir)
        bt_branch.clicked.connect(switch_branch)
        bt_update_effects.clicked.connect(update_effects)
        bt_clear_screen.clicked.connect(clear_screen)
        # self.bt_generate_finsh_pk.clicked.connect()

        # 使用网格布局管理器
        grid_layout = QGridLayout(self)
        # grid_layout.addWidget(label_toast, 0, 1)  # 第二行第二列
        grid_layout.addWidget(bt_open_log, 1, 0)  # 第一行第一列
        grid_layout.addWidget(bt_language, 1, 1)  # 第一行第二列
        grid_layout.addWidget(bt_branch, 1, 2)  # 第一行第三列
        grid_layout.addWidget(bt_update_effects, 2, 0)  # 第一行第四列
        grid_layout.addWidget(bt_clear_screen, 2, 1)  # 第二行第一列
        grid_layout.addWidget(bt_generate_finsh_pk, 2, 2)  # 第二行第二列

        self.setLayout(grid_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
