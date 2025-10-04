#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 18:33
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   07_checkBox.py
# @Desc     :

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QHBoxLayout, QVBoxLayout,
                               QCheckBox, QLabel, QPushButton)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._default = "What is your favourite language?"
        self._label = QLabel(self._default, self)
        self._buttons = []
        self._btn_names = ["Reset", "Exit"]
        self._box = []
        self.check_options = ["Python", "Java", "JavaScript", "C++"]

        self.setWindowTitle("Check Box Example")
        self._setup()

    def _setup(self):
        _layout = QHBoxLayout()
        _row_box = QVBoxLayout()
        _row_btn = QVBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._label)

        for i, check in enumerate(self.check_options):
            checkbox = QCheckBox(check, self)
            checkbox.setChecked(False)
            checkbox.stateChanged.connect(self._selected)
            self._box.append(checkbox)
            _row_box.addWidget(checkbox)

        funcs = [
            self._click2reset,
            self._click2exit
        ]

        for i in range(len(self._btn_names)):
            button = QPushButton(self._btn_names[i], self)
            button.clicked.connect(funcs[i])
            self._buttons.append(button)
            _row_btn.addWidget(button)

        _layout.addLayout(_row_box)
        _layout.addLayout(_row_btn)
        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2reset(self):
        for check in self._box:
            check.setChecked(False)
        self._label.setText(self._default)

    def _click2exit(self):
        self.close()

    def _selected(self):
        selection = [check.text() for check in self._box if check.isChecked()]
        print(selection)

        if len(selection) == 1:
            self._label.setText(f"Your favourite is {selection[0]}")
        else:
            self._label.setText(f"Your favourite are {", ".join(selection)}")


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
