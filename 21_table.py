#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/5 19:36
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   21_table.py
# @Desc     :   

from faker import Faker
from math import ceil
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit,
                               QTableWidget, QTableWidgetItem, QHeaderView)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._faker = Faker()
        self._widget = QWidget(self)
        self._disp = QLabel(self)
        self._line = QLineEdit(self)
        self._table = QTableWidget(self)
        self._btn_search = QPushButton("Search", self)
        self._btn_clean = QPushButton("Clean", self)
        self._data = [
            [self._faker.first_name(), self._faker.phone_number(), self._faker.email(), self._faker.address()]
            for _ in range(105)
        ]
        self._func_labels = ["Create", "Insert", "Clear", "Update", "Delete", "Exit"]
        self._func_buttons = []
        self._page_labels = ["First", "Previous", "Next", "Last"]
        self._page_buttons = []
        self._page_disp = QLabel(self)
        self._page_size = 10
        self._page_curr = 1
        self._page_count = 0

        self.setWindowTitle("Table Widget Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row_search = QHBoxLayout()
        _row_pages = QHBoxLayout()
        _row_funcs = QHBoxLayout()

        self._disp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._disp)

        self._line.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._line.setPlaceholderText("Search Here...")
        self._btn_search.setEnabled(False)
        self._btn_clean.setEnabled(False)
        self._btn_search.clicked.connect(self._click2search)
        self._btn_clean.clicked.connect(self._clear_highlight)
        _row_search.addWidget(self._line)
        _row_search.addWidget(self._btn_search)
        _row_search.addWidget(self._btn_clean)
        _layout.addLayout(_row_search)

        self._table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._table.setSortingEnabled(True)
        _layout.addWidget(self._table)

        self._page_disp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _row_pages.addWidget(self._page_disp)
        func_pages = [
            self._page_first,
            self._page_prev,
            self._page_next,
            self._page_last,
        ]
        for i in range(len(self._page_labels)):
            btn = QPushButton(self._page_labels[i], self)
            btn.clicked.connect(func_pages[i])
            btn.setEnabled(False)
            self._page_buttons.append(btn)
            _row_pages.addWidget(btn)
        _layout.addLayout(_row_pages)

        funcs = [
            self._click2create,
            self._click2insert,
            self._click2clear,
            self._click2update,
            self._click2delete,
            self._click2exit,
        ]
        for i in range(len(self._func_labels)):
            btn = QPushButton(self._func_labels[i], self)
            btn.clicked.connect(funcs[i])
            if self._func_labels[i] in ["Insert", "Clear", "Update", "Delete", ]:
                btn.setEnabled(False)
            self._func_buttons.append(btn)
            _row_funcs.addWidget(btn)
        _layout.addLayout(_row_funcs)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _page_updater(self) -> None:
        # Calculate start and end indices for the current page
        index_start = (self._page_curr - 1) * self._page_size
        index_end = index_start + self._page_size
        page_data = self._data[index_start:index_end]

        # Update the page display
        self._page_disp.setText(f"Page {self._page_curr} of {self._page_count}")

        # Update the table with the current page data
        self._table.setRowCount(len(page_data))
        self._table.setColumnCount(len(page_data[0]))
        for rowIndex, row in enumerate(page_data):
            for colIndex, item in enumerate(row):
                self._table.setItem(rowIndex, colIndex, QTableWidgetItem(item))

    def _click2create(self) -> None:
        self._page_count = ceil(len(self._data) / self._page_size)
        self._page_disp.setText(f"Page 1 of {self._page_count}")

        # load the page
        self._page_updater()

        self._disp.setText(f"Total {len(self._data)} records.")
        self._table.setHorizontalHeaderLabels(["Name", "Phone", "Email", "Address", ])

        for btn in self._func_buttons:
            if btn.text() in ["Insert", "Clear", "Update", "Delete", ]:
                btn.setEnabled(True)

        for btn in self._func_buttons:
            if btn.text() == "Create":
                btn.setEnabled(False)

        for btn in self._page_buttons:
            if btn.text() in ["First", "Previous", "Next", "Last"]:
                btn.setEnabled(True)

        self._btn_search.setEnabled(True)
        self._btn_clean.setEnabled(True)

    def _page_first(self) -> None:
        if self._page_curr != 1:
            self._page_curr = 1
            self._page_updater()

    def _page_prev(self) -> None:
        if self._page_curr > 1:
            self._page_curr -= 1
            self._page_updater()

    def _page_next(self) -> None:
        if self._page_curr < self._page_count:
            self._page_curr += 1
            self._page_updater()

    def _page_last(self) -> None:
        if self._page_curr != self._page_count:
            self._page_curr = self._page_count
            self._page_updater()

    def _click2insert(self) -> None:
        row_position = self._table.rowCount()
        pass

    def _click2clear(self) -> None:
        self._disp.setText("")
        self._table.clear()
        self._table.setRowCount(0)
        self._table.setColumnCount(0)

        for btn in self._func_buttons:
            if btn.text() in ["Insert", "Clear", "Update", "Delete", ]:
                btn.setEnabled(False)

        self._btn_search.setEnabled(False)
        self._btn_clean.setEnabled(False)

    def _click2update(self) -> None:
        pass

    def _click2delete(self) -> None:
        pass

    def _click2search(self) -> None:
        content = self._line.text().strip()
        items = self._table.findItems(content, Qt.MatchFlag.MatchContains)

        # Clear previous highlights
        self._clear_highlight()

        if items:
            for item in items:
                # item.setSelected(True)
                item.setBackground(Qt.GlobalColor.yellow)
            self._disp.setText(f"Found {len(items)} records matching '{content}'.")
        else:
            self._disp.setText(f"No records found matching '{content}'.")

        self._table.scrollToItem(items[0], QTableWidget.ScrollHint.PositionAtCenter)

    def _clear_highlight(self) -> None:
        for row in range(self._table.rowCount()):
            for col in range(self._table.columnCount()):
                item = self._table.item(row, col)
                if item:
                    item.setBackground(Qt.GlobalColor.transparent)

        self._line.clear()

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
