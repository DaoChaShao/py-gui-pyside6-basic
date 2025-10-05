#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 12:50
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   17_intDialog.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout,
                               QPushButton, QInputDialog, QLabel, QHBoxLayout)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._label = QLabel("No input yet", self)
        self._btn_names = ["Get Integer", "Exit"]

        self.setWindowTitle("Input Dialog Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._label)

        funcs = [
            self._click2getInt,
            self._click2exit
        ]

        for i in range(len(self._btn_names)):
            btn = QPushButton(self._btn_names[i], self)
            btn.clicked.connect(funcs[i])
            _row.addWidget(btn)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2getInt(self) -> None:
        num, ok = QInputDialog.getInt(self, "Input Integer", "Enter an integer:", 0, -100, 100, 1)
        if ok:
            self._label.setText(f"You entered: {num}")

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
