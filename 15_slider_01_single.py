#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 12:08
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   15_slider_01_single.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QSlider)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._label = QLabel("Value: 0", self)
        self._slider = QSlider(Qt.Orientation.Horizontal, self)
        self._buttons = ["Reset", "Exit"]

        self.setWindowTitle("Slider Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._label)

        self._slider.setMinimum(0)
        self._slider.setMaximum(100)
        self._slider.setValue(0)
        self._slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self._slider.setTickInterval(10)
        self._slider.valueChanged.connect(self._changed)
        _layout.addWidget(self._slider)

        funcs = [
            self._click2reset,
            self._click2exit,
        ]
        for i in range(len(self._buttons)):
            btn = QPushButton(self._buttons[i], self)
            btn.clicked.connect(funcs[i])
            _row.addWidget(btn)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _changed(self, value):
        self._label.setText(f"Value: {value}")

    def _click2reset(self):
        self._slider.setValue(0)

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
