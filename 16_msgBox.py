#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 12:40
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   16_msgBox.py
# @Desc     :   

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout,
                               QPushButton, QMessageBox, )
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._buttons = ["Info", "Warning", "Error", "Question", "About", "AboutQt", "Exit"]

        self.setWindowTitle("Message Box Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)

        funcs = [
            self._click2info,
            self._click2warning,
            self._click2error,
            self._click2question,
            self._click2about,
            self._click2aboutQt,
            self._click2exit
        ]

        for i in range(len(self._buttons)):
            btn = QPushButton(self._buttons[i], self)
            btn.clicked.connect(funcs[i])
            _layout.addWidget(btn)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2info(self) -> None:
        QMessageBox.information(self, "Information", "This is an information message box.")

    def _click2warning(self) -> None:
        QMessageBox.warning(self, "Warning", "This is an warning message box.")

    def _click2error(self) -> None:
        QMessageBox.critical(self, "Error", "This is an error message box.")

    def _click2question(self) -> None:
        reply = QMessageBox.question(
            self, "Question", "Do you want to continue?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Response", "You chose Yes.")
        else:
            QMessageBox.information(self, "Response", "You chose No.")

    def _click2about(self) -> None:
        QMessageBox.about(self, "About", "This is a simple PySide6 application demonstrating message boxes.")

    def _click2aboutQt(self) -> None:
        QMessageBox.aboutQt(self, "About Qt")

    def _click2exit(self) -> None:
        self.close()


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
