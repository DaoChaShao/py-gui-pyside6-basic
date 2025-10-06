#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/7 01:48
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   30_chart_plotly.py
# @Desc     :   

from pandas import DataFrame
from plotly.graph_objects import Figure, Scatter
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, )
from random import randint
from sys import argv, exit
from tempfile import NamedTemporaryFile


def data_builder(amount: int) -> DataFrame:
    """ Generate random data points """
    points = []
    for i in range(amount):
        point = {
            "x": i,
            "y": randint(0, 100),
        }
        points.append(point)
    return DataFrame(points)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._view = QWebEngineView()
        self._btn_labels = ["Plot", "Clear", "Exit"]
        self._buttons = []

        self.setWindowTitle("Plotly Line Chart Example")
        self.resize(400, 400)
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        # Chart View
        _layout.addWidget(self._view)

        funcs = [
            self._click2plot,
            self._click2clear,
            self.close,
        ]
        for i, label in enumerate(self._btn_labels):
            button = QPushButton(label, self)
            button.clicked.connect(funcs[i])
            if button.text() == "Clear":
                button.setEnabled(False)
            self._buttons.append(button)
            _row.addWidget(button)
        _layout.addLayout(_row)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _click2plot(self) -> None:
        """ Plot random data points """
        # Delete previous series
        points = data_builder(randint(10, 30))

        # Create a Plotly figure with lines and markers
        scatter = Scatter(
            x=points["x"],
            y=points["y"],
            mode="lines+markers",
        )
        fig = Figure(data=[scatter])
        fig.update_layout(
            title="Random Data Points",
            xaxis_title="Weeks",
            yaxis_title="Scores",
        )

        # Create a temporary HTML file to save the plot
        temp_html = NamedTemporaryFile(suffix=".html", delete=False)
        fig.write_html(temp_html.name)
        self._view.load(QUrl.fromLocalFile(temp_html.name))

        for button in self._buttons:
            if button.text() == "Clear":
                button.setEnabled(True)
        for button in self._buttons:
            if button.text() == "Plot":
                button.setEnabled(False)

    def _click2clear(self) -> None:
        """ Clear the chart """
        self._view.setHtml("<html><body></body></html>")

        for button in self._buttons:
            if button.text() == "Clear":
                button.setEnabled(False)
        for button in self._buttons:
            if button.text() == "Plot":
                button.setEnabled(True)


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
