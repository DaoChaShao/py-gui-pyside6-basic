#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 17:28
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   05_line_edit_02_timer.py
# @Desc     :   

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit)
from sys import exit, argv


class SubWindow(QMainWindow):
    def __init__(self, main_win):
        super().__init__()
        self._widget = QWidget(self)
        self._default = "Welcome!"
        self._label = QLabel(self._default, self)
        self._buttons = []
        self._names = ["Exit"]
        self._mian_win = main_win

        self.setWindowTitle("Sub Window")
        self._setup()

    def _setup(self):
        _layout = QVBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._label)

        funcs = [
            self._click2exit,
        ]

        for i in range(len(self._names)):
            button = QPushButton(self._names[i], self)
            button.clicked.connect(funcs[i])
            self._buttons.append(button)
            _layout.addWidget(button)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self):
        self._mian_win.show()
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._default = "Please enter your password!"
        self._label = QLabel(self._default, self)
        self._entry = QLineEdit(self)
        self._buttons = []
        self._names = ["Submit", "Clear", "Exit"]
        self._timer = QTimer()
        self._sub_win = None

        self.setWindowTitle("Main Window")
        self._setup()

    def _setup(self):
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._entry.setEchoMode(QLineEdit.EchoMode.Password)

        self._timer.timeout.connect(self._timer_checker)
        self._timer.start(10)

        funcs = [
            self._click2submit,
            self._click2clear,
            self._click2exit,
        ]

        for i in range(len(self._names)):
            button = QPushButton(self._names[i], self)
            button.clicked.connect(funcs[i])
            self._buttons.append(button)
            _row.addWidget(button)

        _layout.addWidget(self._label)
        _layout.addWidget(self._entry)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self):
        self.close()

    def _click2submit(self):
        pwd: str = self._entry.text()
        if len(pwd) > 8:
            self._label.setText("Password accepted.")
            if self._sub_win is None:
                self._sub_win = SubWindow(self)
            self._sub_win.show()
            self.close()

    def _click2clear(self):
        self._entry.clear()
        self._label.setText(self._default)
        self._label.setStyleSheet("")

    def _timer_checker(self):
        pwd = self._entry.text()
        if pwd == "":
            self._label.setText(self._default)
        else:
            if len(pwd) < 6:
                self._label.setText(f"WEAK")
                self._label.setStyleSheet("color: red; font: bold;")
            elif 6 <= len(pwd) <= 8:
                self._label.setText(f"MEDIUM")
                self._label.setStyleSheet("color: orange; font: bold;")
            else:
                self._label.setText(f"STRONG")
                self._label.setStyleSheet("color: green; font: bold;")


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
