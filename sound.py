#!/usr/bin/python3

import sys

# This code is needed to respond to ctrl-c
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import (QUrl, QTimer)
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtMultimedia import (QSoundEffect)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	sound = QSoundEffect()
	sound.setSource(QUrl.fromLocalFile('beep-06.wav'))
	sound.setVolume(1)

	timer = QTimer()
	timer.setInterval(500)
	timer.timeout.connect(sound.play)
	timer.start()

	sys.exit(app.exec_())
