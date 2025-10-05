#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 11:15
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   14_image_and_timer.py
# @Desc     :   

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, )
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._label = QLabel(self)
        self._buttons = ["Start", "Stop", "Exit"]
        self._index = 0
        self._timer = QTimer(self)
        self._pics = [
            QPixmap("./images/tree blue.png"),
            QPixmap("./images/tree green.png"),
            QPixmap("./images/tree yellow.png"),
        ]

        self.setWindowTitle("Image and Timer Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._label)

        func = [
            self._click2start,
            self._click2stop,
            self._click2exit,
        ]
        for i in range(len(self._buttons)):
            btn = QPushButton(self._buttons[i], self)
            btn.clicked.connect(func[i])
            _row.addWidget(btn)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2start(self):
        self._timer.timeout.connect(self._update_image)
        self._timer.start(500)

    def _click2stop(self):
        self._timer.stop()

    def _click2exit(self):
        self.close()

    def _update_image(self) -> None:
        pixmap = self._pics[self._index].scaledToWidth(
            self._label.width(),
            Qt.TransformationMode.SmoothTransformation
        )
        self._label.setPixmap(pixmap)
        self._index = (self._index + 1) % len(self._pics)


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
