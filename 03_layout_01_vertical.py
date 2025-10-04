#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 10:52
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   03_layout_01_vertical.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout,
                               QLabel, QLineEdit, QPushButton)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._label = QLabel("Click to display", self)
        self._entry = QLineEdit(self)
        self._confirm = QPushButton("Confirm", self)
        self._exit = QPushButton("Exit", self)

        self.setWindowTitle("Vertical Layout Example")

        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)

        self._label.setAlignment(Qt.AlignCenter)
        self._entry.setAlignment(Qt.AlignCenter)
        self._confirm.clicked.connect(self._click2display)
        self._exit.clicked.connect(self._click2exit)

        _layout.addWidget(self._label)
        _layout.addWidget(self._entry)
        _layout.addWidget(self._confirm)
        _layout.addWidget(self._exit)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self):
        self.close()

    def _click2display(self):
        text = self._entry.text()
        self._label.setText(text)


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
