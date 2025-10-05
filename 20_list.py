#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 17:30
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   20_list.py
# @Desc     :   

from faker import Faker
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QSlider, QLabel, QLineEdit,
                               QListWidget, QListWidgetItem, )
from random import randint
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._faker = Faker()
        self._label = QLabel(self)
        self._list = QListWidget(self)
        self._slider = QSlider(self)
        self._line = QLineEdit(self)
        self._btn_names = ["Create", "Insert", "Clear", "Update", "Delete", "Read", "Exit"]
        self._sort = ["Ascending", "Descending"]
        self._buttons = []
        self._amount = 10

        self.setWindowTitle("List Widget Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row_sort = QHBoxLayout()
        _row_func = QHBoxLayout()

        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._label)

        self._slider.setMinimum(0)
        self._slider.setMaximum(100)
        self._slider.setValue(10)

        self._slider.setOrientation(Qt.Orientation.Horizontal)
        self._slider.valueChanged.connect(self._value_updater)
        _layout.addWidget(self._list)
        _layout.addWidget(self._slider)

        self._line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._line)

        func_sort = [
            lambda: self._list.sortItems(Qt.SortOrder.AscendingOrder),
            lambda: self._list.sortItems(Qt.SortOrder.DescendingOrder),
        ]
        for i in range(len(self._sort)):
            btn = QPushButton(self._sort[i], self)
            btn.clicked.connect(func_sort[i])
            _row_sort.addWidget(btn)
        _layout.addLayout(_row_sort)

        funcs = [
            self._click2create,
            self._click2insert,
            self._click2clear,
            self._click2update,
            self._click2delete,
            self._click2search,
            self._click2exit,
        ]
        for i in range(len(self._btn_names)):
            btn = QPushButton(self._btn_names[i], self)
            btn.clicked.connect(funcs[i])
            if (
                    self._btn_names[i] == "Insert"
                    or self._btn_names[i] == "Clear"
                    or self._btn_names[i] == "Update"
                    or self._btn_names[i] == "Delete"
                    or self._btn_names[i] == "Read"
            ):
                btn.setVisible(False)
            self._buttons.append(btn)
            _row_func.addWidget(btn)
        _layout.addLayout(_row_func)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self) -> None:
        self.close()

    def _click2clear(self) -> None:
        self._list.clear()
        self._buttons[1].setVisible(False)
        self._buttons[2].setVisible(False)
        self._buttons[3].setVisible(False)
        self._buttons[4].setVisible(False)
        self._buttons[5].setVisible(False)

    def _click2create(self) -> None:
        count = self._slider.value()
        self._list.addItems([self._faker.first_name() for _ in range(count)])
        self._buttons[1].setVisible(True)
        self._buttons[2].setVisible(True)
        self._buttons[3].setVisible(True)
        self._buttons[4].setVisible(True)
        self._buttons[5].setVisible(True)

    def _value_updater(self, value: int) -> None:
        self._amount = value
        self._label.setText(f"Amount: {str(self._amount)}")
        # Update list to match the slider value
        self._list.clear()
        self._list.addItems([self._faker.first_name() for _ in range(self._amount)])

    def _click2insert(self) -> None:
        current_index = self._list.currentRow()
        value = self._slider.value()
        entry = self._line.text().strip()
        if entry:
            item = QListWidgetItem(entry)
            index = current_index
        else:
            item = QListWidgetItem(self._faker.first_name())
            index = randint(0, value - 1) if value > 0 else 0
        self._line.clear()
        self._list.insertItem(index, item)

    def _click2update(self) -> None:
        current_index = self._list.currentRow()
        entry = self._line.text().strip()
        if entry and current_index != -1:
            self._list.item(current_index).setText(entry)
            self._line.clear()

    def _click2delete(self) -> None:
        current_index = self._list.currentRow()
        if current_index != -1:
            self._list.takeItem(current_index)

    def _click2search(self) -> None:
        entry = self._line.text().strip()
        if not entry:
            return
        items = self._list.findItems(entry, Qt.MatchFlag.MatchContains)
        if items:
            # Hide all items first
            for i in range(self._list.count()):
                self._list.item(i).setHidden(True)

            # Show and select found items
            for item in items:
                item.setHidden(False)
                item.setSelected(True)

            self._label.setText(f"Found {len(items)} item(s)")
        else:
            # No items found
            for i in range(self._list.count()):
                self._list.item(i).setHidden(True)
            self._label.setText("Not Found")


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
