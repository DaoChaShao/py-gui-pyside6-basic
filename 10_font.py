#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 22:09
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   10_font.py
# @Desc     :   

from os import path
from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout,
                               QPushButton, QComboBox, QLabel, )
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._default = "Please select a font"
        self._label = QLabel(self._default, self)
        self._combo = QComboBox(self)
        self._btn_names = ["Clear", "Exit"]
        self._buttons = []

        self.setWindowTitle("Font Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._combo.addItems(["Chinese", "English"])
        self._combo.currentIndexChanged.connect(self._selected)

        _layout.addWidget(self._label)
        _layout.addWidget(self._combo)

        funcs = [
            self._click2clear,
            self._click2exit
        ]

        for i in range(len(self._btn_names)):
            btn = QPushButton(self._btn_names[i], self)
            btn.clicked.connect(funcs[i])
            self._buttons.append(btn)
            _layout.addWidget(btn)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self) -> None:
        self.close()

    def _click2clear(self) -> None:
        # Reset to default font
        self._label.setFont(QFont())
        self._label.setText(self._default)

    def _selected(self) -> None:
        choice: str = self._combo.currentText()

        fonts = {
            "Chinese": "站酷庆科黄油体.ttf",
            "English": "Amadeus.ttf"
        }

        font_path = path.join(path.dirname(__file__), "fonts", fonts[choice])
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            self._label.setText(f"Failed to load {fonts[choice]}")
            return

        # Apply the selected font
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(family, 24)
        self._label.setFont(font)
        self._label.setText(f"abcdeABCDE12345")


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
