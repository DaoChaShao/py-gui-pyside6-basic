#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 12:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   15_slider_02_double.py
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
        self._label = QLabel("Total: 0", self)
        self._label_max = QLabel("Max: 0", self)
        self._label_min = QLabel("Min: 0", self)
        self._slider_max = QSlider(Qt.Orientation.Vertical, self)
        self._slider_min = QSlider(Qt.Orientation.Vertical, self)
        self._buttons = ["Reset", "Exit"]

        self.setWindowTitle("Double Slider Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row_labels = QHBoxLayout()
        _row_sliders = QHBoxLayout()
        _row_buttons = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._label)

        self._label_max.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._label_min.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _row_labels.addWidget(self._label_max)
        _row_labels.addWidget(self._label_min)

        self._slider_max.setMinimum(0)
        self._slider_max.setMaximum(9)
        self._slider_max.setValue(0)
        self._slider_max.setTickPosition(QSlider.TickPosition.TicksLeft)
        self._slider_max.setTickInterval(10)
        self._slider_max.valueChanged.connect(self._changed)
        _row_sliders.addWidget(self._slider_max)

        self._slider_min.setMinimum(0)
        self._slider_min.setMaximum(10)
        self._slider_min.setValue(0)
        self._slider_min.setTickPosition(QSlider.TickPosition.TicksRight)
        self._slider_min.setTickInterval(10)
        self._slider_min.valueChanged.connect(self._changed)
        _row_sliders.addWidget(self._slider_min)

        funcs = [
            self._click2reset,
            self._click2exit,
        ]
        for i in range(len(self._buttons)):
            btn = QPushButton(self._buttons[i], self)
            btn.clicked.connect(funcs[i])
            _row_buttons.addWidget(btn)
        _layout.addLayout(_row_sliders)
        _layout.addLayout(_row_labels)
        _layout.addLayout(_row_buttons)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _changed(self, value):
        if self.sender() == self._slider_max:
            self._label_max.setText(f"Max: {value * 10}")
        elif self.sender() == self._slider_min:
            self._label_min.setText(f"Min: {value * 1}")
        total = self._slider_max.value() * 10 + self._slider_min.value() * 1
        self._label.setText(f"Total: {total}")

    def _click2reset(self, value):
        self._slider_min.setValue(0)
        self._slider_max.setValue(0)

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
