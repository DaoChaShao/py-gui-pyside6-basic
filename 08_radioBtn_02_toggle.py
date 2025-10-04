#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 21:41
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   08_radioBtn_02_toggle.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QHBoxLayout, QVBoxLayout,
                               QButtonGroup, QRadioButton, QLabel, QPushButton)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._default = "What is your Gender?"
        self._label = QLabel(self._default, self)
        self._buttons = []
        self._btn_names = ["Reset", "Exit"]
        self._radio = []
        self._genders = ["Female", "Male"]
        self._group = QButtonGroup(self)

        self.setWindowTitle("Radio Button Example")
        self._setup()

    def _setup(self):
        _layout = QHBoxLayout()
        _row_box = QVBoxLayout()
        _row_btn = QVBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._label)

        for i, radio_btn in enumerate(self._genders):
            radio_btn = QRadioButton(self._genders[i], self)
            radio_btn.setChecked(False)
            self._radio.append(radio_btn)
            self._group.addButton(radio_btn)
            # radio_btn.clicked.connect(self._clicked)
            radio_btn.toggled.connect(self._toggled)
            _row_box.addWidget(radio_btn)

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
        self._group.setExclusive(False)
        for radio in self._radio:
            radio.setChecked(False)
        self._group.setExclusive(True)
        self._label.setText(self._default)

    def _click2exit(self):
        self.close()

    def _clicked(self):
        selection = [radio.text() for radio in self._radio if radio.isChecked()]
        print(selection)

        if selection:
            self._label.setText(f"Your gender is {selection[0]}")

    def _toggled(self, state):
        sender = self.sender()
        if isinstance(sender, QRadioButton):
            text = sender.text()
            if state:
                self._label.setText(f"You gender is {text}")


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
