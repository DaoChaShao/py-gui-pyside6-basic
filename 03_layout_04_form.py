#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 11:34
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   03_layout_04_form.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QFormLayout,
                               QPushButton, QLabel, QLineEdit)
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

        self.setWindowTitle("Form Layout Example")

        self._setup()

    def _setup(self):
        _layout = QFormLayout(self._widget)

        self._label_name.setAlignment(Qt.AlignmentFlag.AlignRight)
        self._entry_name.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._label_pwd.setAlignment(Qt.AlignmentFlag.AlignRight)
        self._entry_pwd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._exit.clicked.connect(self._click2exit)

        _layout.addRow(self._label_name, self._entry_name)
        _layout.addRow(self._label_pwd, self._entry_pwd)
        _layout.addRow(self._login, self._exit)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self):
        self.close()


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    win = MainWindow()
    win.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
