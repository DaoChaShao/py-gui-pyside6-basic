#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 22:41
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   11_textEdit.py
# @Desc     :

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QHBoxLayout, QVBoxLayout,
                               QLabel, QTextEdit, QPushButton)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._btn_names = ["Submit", "Clear", "Exit"]
        self._input = QTextEdit(self)
        self._output = QTextEdit(self)

        self.setWindowTitle("Text Edit Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row_text = QHBoxLayout()
        _row_btn = QHBoxLayout()

        self._input.setPlaceholderText("Input Area Here...")
        self._output.setPlaceholderText("Output Area Here...")
        self._output.setReadOnly(True)
        _row_text.addWidget(self._input)
        _row_text.addWidget(self._output)

        funcs = [
            self._click2submit,
            self._click2clear,
            self._click2exit,
        ]
        for i in range(len(self._btn_names)):
            btn = QPushButton(self._btn_names[i], self)
            btn.clicked.connect(funcs[i])
            _row_btn.addWidget(btn)

        _layout.addLayout(_row_text)
        _layout.addLayout(_row_btn)
        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2submit(self) -> None:
        text = self._input.toPlainText()
        self._output.append(text)

    def _click2clear(self) -> None:
        self._input.clear()
        self._output.clear()

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
