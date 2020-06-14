import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from demo_2 import Ui_MainWindow


if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    # 向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    # 进入程序主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec())