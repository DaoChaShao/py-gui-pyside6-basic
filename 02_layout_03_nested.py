#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 11:19
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   02_layout_03_nested.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
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
        self._exit = QPushButton("Exit", self)

        self.setWindowTitle("Nested Layout Example")

        self._setup()

    def _setup(self):
        _layout = QVBoxLayout()
        _row4name = QHBoxLayout()
        _row4pwd = QHBoxLayout()
        _row4func = QHBoxLayout()

        self._label_name.setAlignment(Qt.AlignmentFlag.AlignRight)
        self._label_pwd.setAlignment(Qt.AlignmentFlag.AlignRight)
        self._entry_name.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._entry_pwd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._exit.clicked.connect(self._click2exit)

        _row4name.addWidget(self._label_name)
        _row4name.addWidget(self._entry_name)
        _row4pwd.addWidget(self._label_pwd)
        _row4pwd.addWidget(self._entry_pwd)
        _row4func.addWidget(self._login)
        _row4func.addWidget(self._exit)

        _layout.addLayout(_row4name)
        _layout.addLayout(_row4pwd)
        _layout.addLayout(_row4func)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self):
        self.close()


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    win = MainWindow()
    win.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()
