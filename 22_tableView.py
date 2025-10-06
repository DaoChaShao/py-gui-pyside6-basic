#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/6 16:03
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   22_tableView.py
# @Desc     :   

from faker import Faker
from math import ceil
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit,
                               QHeaderView, QTableView)
from sys import argv, exit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._faker = Faker()
        self._widget = QWidget(self)
        self._disp = QLabel(self)
        self._line = QLineEdit(self)
        self._model = QStandardItemModel(self)
        self._agent = QSortFilterProxyModel(self)
        self._table = QTableView(self)
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
        self._line.setEnabled(False)
        self._line.textChanged.connect(lambda text: self._agent.setFilterFixedString(text))
        # Set case-insensitive filtering
        self._agent.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        # Search all columns
        self._agent.setFilterKeyColumn(-1)
        _row_search.addWidget(self._line)
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
        for rowIndex, row in enumerate(page_data):
            for colIndex, item in enumerate(row):
                self._model.setItem(rowIndex, colIndex, QStandardItem(item))

    def _click2create(self) -> None:
        self._page_count = ceil(len(self._data) / self._page_size)
        self._page_disp.setText(f"Page 1 of {self._page_count}")

        # load the page
        self._page_updater()
        self._disp.setText(f"Total {len(self._data)} records.")

        # Set up the model and proxy
        self._agent.setSourceModel(self._model)
        self._table.setModel(self._agent)

        header = ["Name", "Phone", "Email", "Address", ]
        for i in range(len(header)):
            self._model.setHorizontalHeaderItem(i, QStandardItem(header[i]))

        for btn in self._func_buttons:
            if btn.text() in ["Insert", "Clear", "Update", "Delete", ]:
                btn.setEnabled(True)

        for btn in self._func_buttons:
            if btn.text() == "Create":
                btn.setEnabled(False)

        for btn in self._page_buttons:
            if btn.text() in ["First", "Previous", "Next", "Last"]:
                btn.setEnabled(True)

        self._line.setEnabled(True)

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
        pass

    def _click2clear(self) -> None:
        self._disp.setText("")
        self._page_disp.setText("")
        self._model.removeRows(0, self._model.rowCount())
        self._model.removeRows(0, self._model.columnCount())

        for btn in self._func_buttons:
            if btn.text() in ["Insert", "Clear", "Update", "Delete", ]:
                btn.setEnabled(False)

        for btn in self._page_buttons:
            if btn.text() in ["First", "Previous", "Next", "Last", ]:
                btn.setEnabled(False)

        for btn in self._func_buttons:
            if btn.text() == "Create":
                btn.setEnabled(True)

        self._line.setEnabled(False)

    def _click2update(self) -> None:
        pass

    def _click2delete(self) -> None:
        pass

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
