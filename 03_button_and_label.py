#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 00:47
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   03_button_and_label.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QVBoxLayout, QPushButton, QLabel, QWidget)
from random import choice
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set a container
        self._widget = QWidget(self)
        self.label = None
        self.button = None

        self._layout()

    def _layout(self) -> None:
        self.setWindowTitle("Random Greet")

        # Set a layout in the container
        layout = QVBoxLayout(self._widget)

        self.label = QLabel("Please click the button")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.greet = QPushButton("Click", self)
        self.greet.clicked.connect(self._greet)
        layout.addWidget(self.greet)
        self.exit = QPushButton("Quit", self)
        self.exit.clicked.connect(self._exit)
        layout.addWidget(self.exit)

        # Set the container as the central widget of the main window
        self.setCentralWidget(self._widget)

    def _greet(self):
        options: list[str] = ["Hello World!", "Hello PySide6!", "Hello Python!"]
        self.label.setText(choice(options))

    def _exit(self):
        self.close()


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
