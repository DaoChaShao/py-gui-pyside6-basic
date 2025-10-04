#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 00:47
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   02_button.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout,
                               QPushButton, QLabel, )
from random import choice
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set a container
        self._widget = QWidget(self)
        self._default = "Please click the button"
        self._label = QLabel(self._default, self)
        self._greet = QPushButton("Greet", self)
        self._clear = QPushButton("Clear", self)
        self._exit = QPushButton("Exit", self)

        self.setWindowTitle("Random Greet")

        self._setup()

    def _setup(self) -> None:
        # Set a layout in the container
        _layout = QVBoxLayout(self._widget)

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._greet.clicked.connect(self._click2greet)
        self._clear.clicked.connect(self._click2clear)
        self._exit.clicked.connect(self._click2exit)

        _layout.addWidget(self._label)
        _layout.addWidget(self._greet)
        _layout.addWidget(self._clear)
        _layout.addWidget(self._exit)

        # Set the container as the central widget of the main window
        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2greet(self):
        options: list[str] = ["Hello World!", "Hello PySide6!", "Hello Python!"]
        self._label.setText(choice(options))

    def _click2exit(self):
        self.close()

    def _click2clear(self):
        self._label.setText(self._default)


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
