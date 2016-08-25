#!/usr/bin/python3

import sys

# This code is needed to respond to ctrl-c
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import (Qt, QUrl, QTimer, QDateTime)
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QHBoxLayout, QVBoxLayout)
from PyQt5.QtMultimedia import (QSoundEffect)
from PyQt5.QtGui import (QPalette)

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

		palette = QPalette()
		palette.setColor(QPalette.Window, Qt.black)
		self.setPalette(palette)

		self.clock = Clock()


		vlayout = QVBoxLayout()
		vlayout.addWidget(self.clock, 2, Qt.AlignVCenter)
		self.clock.setFixedSize(800, 200)

		hlayout = QHBoxLayout()
		hlayout.addLayout(vlayout)

		self.setLayout(hlayout)

		self.showFullScreen()

class Clock(QLCDNumber):
	def __init__(self, QParent = None):
		super().__init__(8, QParent)

		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.update)
		self.timer.start()

		self.update()

	def update(self):
		time = QDateTime.currentDateTime()
		self.display(time.toString('hh:mm:ss'))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	sys.exit(app.exec_())
