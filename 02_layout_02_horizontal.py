#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 11:07
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   02_layout_02_horizontal.py
# @Desc     :   

from faker import Faker
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QHBoxLayout,
                               QLabel, QPushButton)
from random import choice
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._faker = Faker()
        self._label = QLabel("Click to display", self)
        self._confirm = QPushButton("Get", self)
        self._exit = QPushButton("Exit", self)

        self.setWindowTitle("Horizontal Layout Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QHBoxLayout()

        self._label.setAlignment(Qt.AlignCenter)
        self._confirm.clicked.connect(self._click2display)
        self._exit.clicked.connect(self._click2exit)

        _layout.addWidget(self._label)
        _layout.addWidget(self._confirm)
        _layout.addWidget(self._exit)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2display(self) -> None:
        names: list[str] = [self._faker.first_name() for _ in range(10)]
        self._label.setText(choice(names))

    def _click2exit(self) -> None:
        self.close()


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
