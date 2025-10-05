#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 15:45
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   18_signal.py
# @Desc     :   

from faker import Faker
from PySide6.QtCore import Qt, Signal, QObject, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLineEdit, QLabel)
from sys import argv, exit


class Signals(QObject):
    login = Signal(str)


class MainWindow(QMainWindow):
    def __init__(self, signals):
        super().__init__()
        self._widget = QWidget(self)
        self._faker = Faker()
        self._signals = signals
        self._line = QLineEdit(self)
        self._buttons = ["Login", "Clear", "Exit"]
        self._sub_win = None

        self.setWindowTitle("Signal Example - Main Window")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        self._line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._line.setDisabled(True)
        _layout.addWidget(self._line)

        funcs = [
            self._click2login,
            self._click2clear,
            self._click2exit
        ]

        for i in range(len(self._buttons)):
            btn = QPushButton(self._buttons[i], self)
            btn.clicked.connect(funcs[i])
            _row.addWidget(btn)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self) -> None:
        self.close()

    def _click2clear(self) -> None:
        self._line.clear()

    def _click2login(self) -> None:
        name = self._faker.first_name()
        self._line.setText(name)

        self._sub_win = SubWindow(self, self._signals)
        self._signals.login.emit(name)

        self._sub_win.show()
        self.hide()


class SubWindow(QMainWindow):
    def __init__(self, main_win, signals):
        super().__init__()
        self._widget = QWidget(self)
        self._label = QLabel(self)
        self._main_win = main_win
        self._signals = signals
        self._buttons = ["Back", "Exit"]

        self.setWindowTitle("Signal Example - Sub Window")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._signals.login.connect(self._slot4name)
        _layout.addWidget(self._label)

        func = [
            self._click2back,
            self._click2exit,
        ]
        for i in range(len(self._buttons)):
            btn = QPushButton(self._buttons[i], self)
            btn.clicked.connect(func[i])
            _row.addWidget(btn)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self) -> None:
        self.close()
        self._main_win.close()

    def _click2back(self) -> None:
        self.close()
        self._main_win.show()

    @Slot(str)
    def _slot4name(self, name: str) -> None:
        self._label.setText(f"Welcome {name} to the Sub Window!")


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    signals = Signals()
    window = MainWindow(signals)
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
