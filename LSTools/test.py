import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Toast')
        self.setGeometry(100, 100, 300, 200)

        self.toast_label = QLabel(self)
        self.toast_label.setStyleSheet("background-color: rgba(0, 0, 0, 0.7); color: white; padding: 10px; border-radius: 5px;")
        self.toast_label.hide()

        MainWindow.showToast("Hello, PyQt5 Toast!", duration=2000)

    @staticmethod
    def showToast(message, duration=2000):
        toast_label = QLabel()
        toast_label.setText(message)
        toast_label.setStyleSheet("background-color: rgba(0, 0, 0, 0.7); color: white; padding: 10px; border-radius: 5px;")
        toast_label.adjustSize()
        toast_label.move((MainWindow.width() - toast_label.width()) // 2, MainWindow.height() - toast_label.height() - 20)
        toast_label.show()

        QTimer.singleShot(duration, toast_label.hide)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
