#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 16:35
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   06_comboBox_02_double.py
# @Desc     :   

from faker import Faker
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QComboBox, QLabel, QPushButton)
from sys import exit, argv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._faker = Faker()
        self._default = "Display Area"
        self._label = QLabel(self._default, self)
        self._options = [self._faker.first_name() for _ in range(5)]
        self._main = QComboBox(self)
        self._sub = QComboBox(self)
        self._submit = QPushButton("Submit", self)
        self._reset = QPushButton("Reset", self)
        self._exit = QPushButton("Exit", self)

        self.setWindowTitle("Double linked ComboBox Example")

        self._setup()

    def _setup(self):
        _layout = QVBoxLayout()
        _row = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._main.addItems(self._options)
        self._update_sub()

        self._main.currentIndexChanged.connect(self._update_sub)
        self._submit.clicked.connect(self._click2submit)
        self._reset.clicked.connect(self._click2reset)
        self._exit.clicked.connect(self._click2exit)

        _layout.addWidget(self._label)
        _layout.addWidget(self._main)
        _layout.addWidget(self._sub)
        _row.addWidget(self._submit)
        _row.addWidget(self._reset)
        _row.addWidget(self._exit)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self) -> None:
        self.close()

    def _update_sub(self):
        _item = self._main.currentText()
        self._sub.clear()
        _left = [option for option in self._options if option != _item]
        self._sub.addItems(_left)

    def _click2submit(self) -> None:
        name = self._sub.currentText()
        self._label.setText(name)

    def _click2reset(self) -> None:
        self._label.setText(self._default)
        self._main.setCurrentIndex(0)
        self._update_sub()


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
