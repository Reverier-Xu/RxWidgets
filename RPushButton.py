import sys

from PyQt5 import QtWidgets, QtCore, QtGui


class RPushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(RPushButton, self).__init__(parent)
        self.setStyleSheet(RPushButtonDarkStyle)


RPushButtonDarkStyle = '''
QPushButton{
    background-color: rgb(35, 35, 35);
    color: white;
    border-radius: 10px;
    border: 5px solid rgb(35, 35, 35);
}
QPushButton:hover{
    background-color: rgb(50, 90, 150);
    border: 5px solid rgb(50, 90, 150);
    }
QPushButton:pressed{
    background-color: rgb(80, 140, 250);
    border: 5px solid rgb(80, 140, 250);
}
'''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    Win = QtWidgets.QMainWindow()
    Win.setWindowTitle('RPushButton')
    widget = QtWidgets.QWidget()
    button = RPushButton(widget)
    button.setText('Hello')
    button.setGeometry(QtCore.QRect(120, 45, 100, 100))
    Win.setCentralWidget(widget)
    Win.resize(400, 400)
    # Win.TypeStack.setCurrentWidget(Win.WelcomeLabel)
    Win.show()
    sys.exit(app.exec_())
