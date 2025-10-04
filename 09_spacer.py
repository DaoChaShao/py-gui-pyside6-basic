#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 21:48
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   09_spacer.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QGridLayout,
                               QLCDNumber, QSpacerItem, QSizePolicy,
                               QPushButton)
from sys import argv, exit


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._display = QLCDNumber(self)
        self._button_1 = QPushButton("1", self)
        self._button_2 = QPushButton("2", self)
        self._button_3 = QPushButton("3", self)
        self._button_4 = QPushButton("4", self)
        self._button_5 = QPushButton("5", self)
        self._button_6 = QPushButton("6", self)
        self._button_7 = QPushButton("7", self)
        self._button_8 = QPushButton("8", self)
        self._button_9 = QPushButton("9", self)
        self._button_0 = QPushButton("0", self)
        self._button_add = QPushButton("+", self)
        self._button_sub = QPushButton("-", self)
        self._button_mul = QPushButton("*", self)
        self._button_div = QPushButton("/", self)
        self._button_equal = QPushButton("=", self)
        self._button_clear = QPushButton("C", self)
        self._button_back = QPushButton("←", self)
        self._button_dot = QPushButton(".", self)
        self._button_exit = QPushButton("Quit", self)

        self.setWindowTitle("Calculator")

        self._setup()

    def _setup(self) -> None:
        """ Set up the GUI """
        _layout = QGridLayout()

        self._button_exit.clicked.connect(self._click2exit)
        ver_spacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        # Row 1
        _layout.addWidget(self._display, 0, 0, 3, 4)
        _layout.addItem(ver_spacer, 3, 0, 1, 4)
        # Row 2
        _layout.addWidget(self._button_clear, 4, 0, 1, 1)
        _layout.addWidget(self._button_back, 4, 1, 1, 1)
        _layout.addWidget(self._button_equal, 4, 2, 1, 2)
        # Row 3
        _layout.addWidget(self._button_7, 5, 0, 1, 1)
        _layout.addWidget(self._button_8, 5, 1, 1, 1)
        _layout.addWidget(self._button_9, 5, 2, 1, 1)
        _layout.addWidget(self._button_add, 5, 3, 1, 1)
        # Row 4
        _layout.addWidget(self._button_4, 6, 0, 1, 1)
        _layout.addWidget(self._button_5, 6, 1, 1, 1)
        _layout.addWidget(self._button_6, 6, 2, 1, 1)
        _layout.addWidget(self._button_sub, 6, 3, 1, 1)
        # Row 5
        _layout.addWidget(self._button_1, 7, 0, 1, 1)
        _layout.addWidget(self._button_2, 7, 1, 1, 1)
        _layout.addWidget(self._button_3, 7, 2, 1, 1)
        _layout.addWidget(self._button_mul, 7, 3, 1, 1)
        # Row 6
        _layout.addWidget(self._button_0, 8, 0, 1, 2)
        _layout.addWidget(self._button_dot, 8, 2, 1, 1)
        _layout.addWidget(self._button_div, 8, 3, 1, 1)
        # Row 7
        _layout.addWidget(self._button_exit, 9, 0, 1, 4)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self) -> None:
        self.close()


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = Calculator()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
