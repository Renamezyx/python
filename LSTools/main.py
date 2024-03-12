import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from tools.studio_control import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("tools")
        self.resize(1200, 800)

        # 创建文本标签和按钮
        self.bt_open_log = QPushButton("日志文件夹", self)
        self.bt_language = QPushButton("多语言文件夹", self)
        self.bt_branch = QPushButton("branch切换", self)
        self.bt_update_effects = QPushButton("清除美颜", self)
        self.bt_clear_screen = QPushButton("清除场景", self)

        # 将按钮点击事件与自定义方法连接
        self.bt_open_log.clicked.connect(open_logs_dir)
        self.bt_language.clicked.connect(open_language_dir)
        self.bt_branch.clicked.connect(switch_branch)
        self.bt_update_effects.clicked.connect(update_effects)
        self.bt_clear_screen.clicked.connect(clear_screen)

        # 使用垂直布局管理器来安排组件
        layout = QVBoxLayout()
        layout.addWidget(self.bt_open_log)
        layout.addWidget(self.bt_language)
        layout.addWidget(self.bt_branch)
        layout.addWidget(self.bt_update_effects)
        layout.addWidget(self.bt_clear_screen)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
