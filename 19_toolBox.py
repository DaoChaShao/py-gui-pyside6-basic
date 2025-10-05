#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 16:56
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   19_toolBox.py
# @Desc     :   

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout,
                               QLabel, QPushButton,
                               QToolBox, QStyle)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._buttons = ["Exit"]
        self._width = 240
        self._height = 400
        self._tools = ["ToolBox I", "ToolBox II", "ToolBox III"]

        self.setWindowTitle("ToolBox Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout()

        tool = QToolBox(self)
        tool.setFixedSize(self._width, self._height)
        tool.currentChanged.connect(self._icon_switch)

        for i in range(len(self._tools)):
            label = QLabel(self._tools[i])
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            tool.addItem(label, self._tools[i])
            self._icon_init(tool, i)
        _layout.addWidget(tool)

        funcs = [
            self._click2exit,
        ]
        for i in range(len(self._buttons)):
            btn = QPushButton(self._buttons[i], self)
            btn.clicked.connect(funcs[i])
            _layout.addWidget(btn)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self) -> None:
        self.close()

    def _icon_switch(self) -> None:
        sender = self.sender()
        if isinstance(sender, QToolBox):
            current_index = sender.currentIndex()

            for index in range(sender.count()):
                if index != current_index:
                    icon = self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowRight)
                else:
                    icon = self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowDown)
                sender.setItemIcon(index, icon)

    def _icon_init(self, tool_box, index) -> None:
        if index == 0:
            icon = self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowDown)
        else:
            icon = self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowRight)
        tool_box.setItemIcon(index, icon)


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
