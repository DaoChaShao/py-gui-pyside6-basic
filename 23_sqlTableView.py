#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/6 16:54
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   23_sqlTableView.py
# @Desc     :   

from os import path
from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtSql import (
    QSqlDatabase,  # Database Connection
    QSqlQueryModel,  # Read-Only Data Model
    QSqlTableModel,  # Read-Write Data Model
)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit,
                               QTableView, QHeaderView, QAbstractItemView, )
from sys import argv, exit


def sqlite_loader(db_path: str, label) -> None | QSqlDatabase:
    if not path.exists(db_path):
        label.setText("Database file not found.")
        print(f"Database file not found: {db_path}")
        return None

    if "QSQLITE" not in QSqlDatabase.drivers():
        label.setText("QSQLITE driver not available.")
        print("QSQLITE driver not available")
        return None

    # Initialize and open the database connection:
    # - "QSQLITE": SQLite
    # - "QODBC": ODBC
    # - "QPSQL": PostgresSQL
    # - "QMYSQL": MySQL
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(db_path)
    if not db.open():
        label.setText("Failed to connect to database.")
        return None
    label.setText("Database connected successfully.")
    return db


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._disp = QLabel(self)
        self._line = QLineEdit(self)

        self._db_path: str = "./data/sql3.db"
        self._db_name: str = "fake_data"
        self._db: QSqlDatabase = sqlite_loader(self._db_path, self._disp)

        self._model = QSqlTableModel(self, self._db)
        self._agent = QSortFilterProxyModel(self)
        self._table = QTableView(self)

        self._func_labels: list[str] = ["Create", "Clear", "Exit"]
        self._func_buttons: list = []
        self.setWindowTitle("SQL Table View Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row_funcs = QHBoxLayout()

        self._disp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._disp)

        self._line.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._line.setEnabled(False)
        self._line.setPlaceholderText("Search Here...")
        self._line.textChanged.connect(lambda text: self._agent.setFilterFixedString(text))
        _layout.addWidget(self._line)

        self._agent.setSourceModel(self._model)
        # Search all columns
        self._agent.setFilterKeyColumn(-1)

        self._table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self._table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._table.setSortingEnabled(True)
        self._table.setModel(self._agent)
        _layout.addWidget(self._table)

        funcs: list = [
            self._click2load,
            self._click2clear,
            self._click2exit,
        ]
        for i in range(len(self._func_labels)):
            btn = QPushButton(self._func_labels[i], self)
            btn.clicked.connect(funcs[i])
            if self._func_labels[i] == "Clear":
                btn.setEnabled(False)
            self._func_buttons.append(btn)
            _row_funcs.addWidget(btn)
        _layout.addLayout(_row_funcs)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2exit(self):
        self.close()

    def _click2clear(self):
        self._disp.setText("")
        self._model.setTable("")
        self._model.removeRows(0, self._model.rowCount())
        self._model.removeColumns(0, self._model.columnCount())

        self._line.setEnabled(False)
        for btn in self._func_buttons:
            if btn.text() in ["Clear", ]:
                btn.setEnabled(False)
        for btn in self._func_buttons:
            if btn.text() in ["Create", ]:
                btn.setEnabled(True)

    def _click2load(self):
        self._model.setTable(self._db_name)
        self._model.select()
        print(self._model.rowCount())

        header: list[str] = ["Name", "Phone", "Address", "Email"]
        for i in range(len(header)):
            self._model.setHeaderData(i, Qt.Orientation.Horizontal, header[i])

        self._line.setEnabled(True)
        for btn in self._func_buttons:
            if btn.text() in ["Clear", ]:
                btn.setEnabled(True)
        for btn in self._func_buttons:
            if btn.text() in ["Create", ]:
                btn.setEnabled(False)


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
