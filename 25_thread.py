#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/6 20:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   25_thread.py
# @Desc     :   

from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel)
from random import uniform
from sys import argv, exit
from time import sleep


class WorkThread(QThread):
    process = Signal(str, float, int)

    def __init__(self, player: str):
        super().__init__()
        self._player = player
        self._time: float = 0.0
        self._total: int = 0

    def run(self):
        """ Calculate the sum from 1 to 100 """
        for i in range(1, 101):
            self._total += i
            # Simulate time-consuming calculation
            delay: float = uniform(0, 0.3)
            sleep(delay)
            self._time += delay
            print(f"Sum {self._total} took {self._time:.2f}s for {self._player}")
            self.process.emit(self._player, self._time, self._total)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self._names = ["Tom", "Jerry"]
        self._players = {}
        self._btn_labels = ["Start", "Reset", "Exit"]
        self._buttons = []

        self.setWindowTitle("Thread Example")
        self._setup()

    def _setup(self) -> None:
        _layout = QVBoxLayout(self._widget)
        _row_labels = QHBoxLayout()
        _row_buttons = QHBoxLayout()

        for name in self._names:
            # Create a label displayer for each player
            label = QLabel(name, self)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            _row_labels.addWidget(label)
            # Create a thread worker for each player
            thread = WorkThread(name)
            thread.process.connect(self._label_updater)

            self._players[name] = {
                "label": label,
                "thread": thread,
            }

        funcs = [
            self._click2start,
            self._click2reset,
            self._click2exit,
        ]
        for i in range(len(funcs)):
            btn = QPushButton(self._btn_labels[i], self)
            btn.clicked.connect(funcs[i])
            if btn.text() == "Reset":
                btn.setEnabled(False)
            self._buttons.append(btn)
            _row_buttons.addWidget(btn)
        _layout.addLayout(_row_labels)
        _layout.addLayout(_row_buttons)

        self._widget.setLayout(_layout)
        self.setCentralWidget(self._widget)

    def _label_updater(self, player: str, time: float, total: int) -> None:
        info = self._players.get(player)
        if info:
            info["label"].setText(f"{player} finished in {time:.2f}s with sum {total}")

    def _click2start(self):
        for name, info in self._players.items():
            thread = info["thread"]
            if not thread.isRunning():
                thread.started.connect(lambda player=name: print(f"{player} started"))
                thread.finished.connect(lambda player=name: print(f"{player} finished"))
                thread.finished.connect(thread.deleteLater)
                thread.start()

        for btn in self._buttons:
            if btn.text() == "Start":
                btn.setEnabled(False)
        for btn in self._buttons:
            if btn.text() == "Reset":
                btn.setEnabled(True)

    def _click2exit(self):
        self.close()

    def _click2reset(self):
        for name, info in self._players.items():
            label = info["label"]
            thread = info["thread"]
            if thread.isRunning():
                thread.terminate()
                thread.wait()
            label.setText(name)

        for btn in self._buttons:
            if btn.text() == "Start":
                btn.setEnabled(True)
        for btn in self._buttons:
            if btn.text() == "Reset":
                btn.setEnabled(False)


def main() -> None:
    """ Main Function """
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
