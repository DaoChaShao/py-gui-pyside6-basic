#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 09:32
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   13_fileDialog.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QFileDialog)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._default = ""
        self._label = QLabel(self._default, self)
        self._buttons = ["Display", "Clear", "Exit"]

        self.setWindowTitle("Image Display Example")

        self._setup()

    def _setup(self):
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._label)

        funcs = [
            self._click2display,
            self._click2clear,
            self._click2exit
        ]
        for i in range(len(self._buttons)):
            button = QPushButton(self._buttons[i], self)
            button.clicked.connect(funcs[i])
            _row.addWidget(button)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2display(self):
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Choose Image")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if dialog.exec():
            files = dialog.selectedFiles()
            if files:
                IMAGE_PATH = files[0]
                # IMAGE_PATH = "./images/image.png"
                self._label.setPixmap(QPixmap(IMAGE_PATH))
                self._label.setScaledContents(True)

    def _click2clear(self):
        self._label.clear()
        self._label.setText(self._default)

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
