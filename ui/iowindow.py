# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iowindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_deckIOWindow(object):
    def setupUi(self, deckIOWindow):
        if not deckIOWindow.objectName():
            deckIOWindow.setObjectName(u"deckIOWindow")
        deckIOWindow.resize(671, 267)
        self.centralwidget = QWidget(deckIOWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ioLabel = QLabel(self.centralwidget)
        self.ioLabel.setObjectName(u"ioLabel")

        self.verticalLayout.addWidget(self.ioLabel)

        self.pathParser = QLineEdit(self.centralwidget)
        self.pathParser.setObjectName(u"pathParser")

        self.verticalLayout.addWidget(self.pathParser)

        self.deckIOButton = QPushButton(self.centralwidget)
        self.deckIOButton.setObjectName(u"deckIOButton")

        self.verticalLayout.addWidget(self.deckIOButton)

        deckIOWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(deckIOWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 671, 22))
        deckIOWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(deckIOWindow)
        self.statusbar.setObjectName(u"statusbar")
        deckIOWindow.setStatusBar(self.statusbar)

        self.retranslateUi(deckIOWindow)

        QMetaObject.connectSlotsByName(deckIOWindow)
    # setupUi

    def retranslateUi(self, deckIOWindow):
        deckIOWindow.setWindowTitle(QCoreApplication.translate("deckIOWindow", u"Deck IO Window", None))
        self.ioLabel.setText("")
        self.deckIOButton.setText("")
    # retranslateUi

