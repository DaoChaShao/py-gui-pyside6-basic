#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/4 00:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   01_window.py
# @Desc     :

from PySide6.QtWidgets import QApplication, QMainWindow
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New App")


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
