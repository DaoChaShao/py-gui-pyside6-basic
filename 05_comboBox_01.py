#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 16:15
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   05_comboBox_01.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit)
from sys import exit, argv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._default = "Please enter your name"
        self._label = QLabel(self._default, self)
        self._entry = QLineEdit(self)
        self._submit = QPushButton("Submit", self)
        self._exit = QPushButton("Exit", self)

        self.setWindowTitle("Line Edit Example")
        self._setup()

    def _setup(self):
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._entry.setPlaceholderText(self._default)
        self._submit.clicked.connect(self._click2submit)
        self._exit.clicked.connect(self._click2exit)

        _layout.addWidget(self._label)
        _layout.addWidget(self._entry)
        _row.addWidget(self._submit)
        _row.addWidget(self._exit)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2submit(self):
        current: str = self._entry.text()
        if current and current != self._default:
            self._label.setText(f"Hello, {current}!")
        else:
            self._label.setText("Please enter a valid name.")

    def _click2exit(self):
        self.close()


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
