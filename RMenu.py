import sys

from PyQt5 import QtWidgets, QtCore, QtGui

QMenuDarkStyle = '''
QMenu {
    background-color: rgb(28, 28, 28);
    color: rgb(200, 200, 200);
    border: 1px solid rgb(40, 40, 40); 
    margin: 2px; /* some spacing around the menu */
}

QMenu::item {
    padding: 2px 2px 2px 2px;
    border: 1px solid transparent; /* reserve space for selection border */
}

QMenu::item:selected {
    border-color: darkblue;
    background: rgba(100, 100, 100, 150);
    border-radius: 5px;
}

QMenu::item:hover {
    border-color: darkblue;
    background: rgba(100, 100, 100, 150);
    border-radius: 5px;
}

QMenu::icon:checked { /* appearance of a 'checked' icon */
    background: gray;
    border: 1px inset gray;
    position: absolute;
    top: 1px;
    right: 1px;
    bottom: 1px;
    left: 1px;
}

QMenu::separator {
    height: 1px;
    background: rgb(40, 40, 40);
}

QMenu::indicator {
    width: 13px;
    height: 13px;
}
'''