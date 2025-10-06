#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/7 01:08
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   28_chart_bar.py
# @Desc     :   

from pandas import DataFrame
from PySide6.QtCharts import QBarSet, QChart, QBarSeries, QChartView
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, )
from random import randint
from sys import argv, exit


def data_builder(amount: int) -> DataFrame:
    """ Generate random data points """
    points: list[dict[str, int]] = []
    for i in range(amount):
        point = {
            "index": i,
            "Tom": randint(0, 100),
            "Jerry": randint(0, 100),
        }
        points.append(point)
    return DataFrame(points)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._chart = QChart()
        self._view = QChartView(self._chart)
        self._btn_labels = ["Plot", "Clear", "Exit"]
        self._buttons = []

        self.setWindowTitle("Bar Chart Example")
        self.resize(800, 400)
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row = QHBoxLayout()

        # Chart View
        self._view.setRenderHint(QPainter.RenderHint.Antialiasing)
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
        self.setCentralWidget(self._widget)

    def _click2plot(self) -> None:
        """ Plot random data points """
        """ Plot random data points """
        # Delete previous series
        self._chart.removeAllSeries()

        series = QBarSeries()
        scores: DataFrame = data_builder(20)
        print(scores, type(scores), scores.shape)
        lines: list[str] = ["Tom", "Jerry"]
        for line in lines:
            bar = QBarSet(line)
            for _, row in scores.iterrows():
                bar.append(row[line])
            series.append(bar)

        self._chart.addSeries(series)
        self._chart.setTitle(f"{lines[0]} vs {lines[1]} Scores")
        self._chart.createDefaultAxes()

        for button in self._buttons:
            if button.text() == "Clear":
                button.setEnabled(True)
        for button in self._buttons:
            if button.text() == "Plot":
                button.setEnabled(False)

    def _click2clear(self) -> None:
        """ Clear the chart """
        self._chart.setTitle("")
        self._chart.removeAllSeries()
        for axis in self._chart.axes():
            self._chart.removeAxis(axis)

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
