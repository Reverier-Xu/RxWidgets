import sys

from PyQt5 import QtWidgets, QtCore


class RPushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, style='Dark', text=''):
        super(RPushButton, self).__init__(text, parent=parent)
        if style == 'Dark':
            self.setStyleSheet(RPushButtonDarkStyle)
        elif style == 'Light':
            self.setStyleSheet(RPushButtonLightStyle)


class RMenuButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, style='Dark', text=''):
        super(RMenuButton, self).__init__(text, parent=parent)
        if style == 'Dark':
            self.setStyleSheet(RMenuButtonDarkStyle)
        elif style == 'Light':
            self.setStyleSheet(RMenuButtonLightStyle)


RMenuButtonDarkStyle = '''
QPushButton{
    background-color: transparent;
    color: white;
    font: 18px;
    border-radius: 0px;
    border: 0px solid rgb(40, 40, 40);
}
QPushButton:hover{
    background-color: rgb(50, 90, 150);
}
QPushButton:pressed{
    background-color: rgb(80, 140, 250);
}
'''

RMenuButtonLightStyle = '''
QPushButton{
    background-color: transparent;
    color: black;
    font: 18px;
    border-radius: 0px;
    border: 0px solid rgb(40, 40, 40);
}
QPushButton:hover{
    background-color: rgb(50, 50, 220);
}
QPushButton:pressed{
    background-color: rgb(70, 70, 250);
}
'''

RPushButtonDarkStyle = '''
QPushButton{
    background-color: rgb(50, 90, 170);
    color: white;
    font: 18px;
    border-radius: 5px;
    border: 1px solid rgb(40, 40, 40);
}
QPushButton:hover{
    background-color: rgb(50, 90, 200);
    border: 1px solid rgb(40, 40, 40);
}
QPushButton:pressed{
    background-color: rgb(100, 100, 100);
    border: 1px solid rgb(60, 60, 60);
}
'''

RPushButtonLightStyle = '''
QPushButton{
    background-color: rgb(80, 120, 255);
    color: black;
    font: 18px;
    border-radius: 5px;
    border: 1px solid rgb(80, 120, 255);
}
QPushButton:hover{
    background-color: rgb(50, 50, 220);
    border: 3px solid rgb(50, 50, 220);
}
QPushButton:pressed{
    background-color: rgb(70, 70, 250);
    border: 3px solid rgb(70, 70, 250);
}
'''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    Win = QtWidgets.QMainWindow()
    Win.setWindowTitle('RPushButton')
    widget = QtWidgets.QWidget()
    button = RPushButton(widget, 'Light', 'hello')
    button.setGeometry(QtCore.QRect(100, 100, 100, 40))
    button2 = RMenuButton(widget, 'Light', 'menu')
    button2.setGeometry(QtCore.QRect(100, 200, 100, 40))

    Win.setCentralWidget(widget)
    Win.resize(400, 400)
    # Win.TypeStack.setCurrentWidget(Win.WelcomeLabel)
    Win.show()
    sys.exit(app.exec_())
