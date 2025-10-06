#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/6 19:42
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   24_tabWidget.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QTabWidget)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._tab = QTabWidget(self)
        self._tab_labels = ["Home", "Profile", "Settings", "About"]

        self.setWindowTitle("Tab Bar Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)

        for i in range(len(self._tab_labels)):
            tab = QWidget()
            _col = QVBoxLayout()

            label = QLabel(self._tab_labels[i], self)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            button = QPushButton(self._tab_labels[i], self)
            _col.addWidget(label)
            _col.addWidget(button)

            tab.setLayout(_col)
            _layout.addWidget(tab)
            self._tab.addTab(tab, self._tab_labels[i])
        _layout.addWidget(self._tab)

        self._tab.setTabsClosable(True)
        self._tab.tabCloseRequested.connect(self._click2close)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2close(self, index: int) -> None:
        self._tab.removeTab(index)


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
