#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 12:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   02_layout_05_grid.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QGridLayout,
                               QLabel, QLineEdit, QPushButton)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._label_name = QLabel("Username", self)
        self._entry_name = QLineEdit(self)
        self._label_pwd = QLabel("Password", self)
        self._entry_pwd = QLineEdit(self)
        self._login = QPushButton("Login", self)
        self._register = QPushButton("Register", self)
        self._exit = QPushButton("Exit", self)

        self.setWindowTitle("GridLayout Example")

        self._setup()

    def _setup(self):
        _layout = QGridLayout()

        self._label_name.setAlignment(Qt.AlignmentFlag.AlignRight)
        self._entry_name.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._label_pwd.setAlignment(Qt.AlignmentFlag.AlignRight)
        self._entry_pwd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._exit.clicked.connect(self._click2exit)
        self._login.clicked.connect(self._click2login)

        _layout.addWidget(self._label_name, 0, 0)
        _layout.addWidget(self._entry_name, 0, 1)
        _layout.addWidget(self._label_pwd, 1, 0)
        _layout.addWidget(self._entry_pwd, 1, 1)
        _layout.addWidget(self._login, 2, 0)
        _layout.addWidget(self._register, 2, 1)

        _layout.addWidget(self._exit, 3, 0, 1, 2)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self):
        self.close()

    def _click2login(self):
        pass


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    win = MainWindow()
    win.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
