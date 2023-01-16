# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createdeckwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DeckCreationWindow(object):
    def setupUi(self, DeckCreationWindow):
        if not DeckCreationWindow.objectName():
            DeckCreationWindow.setObjectName(u"DeckCreationWindow")
        DeckCreationWindow.resize(632, 238)
        self.centralwidget = QWidget(DeckCreationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.enterDeckLabel = QLabel(self.centralwidget)
        self.enterDeckLabel.setObjectName(u"enterDeckLabel")

        self.verticalLayout.addWidget(self.enterDeckLabel)

        self.deckNameEdit = QLineEdit(self.centralwidget)
        self.deckNameEdit.setObjectName(u"deckNameEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deckNameEdit.sizePolicy().hasHeightForWidth())
        self.deckNameEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(23)
        self.deckNameEdit.setFont(font)

        self.verticalLayout.addWidget(self.deckNameEdit)

        self.createDeckButton = QPushButton(self.centralwidget)
        self.createDeckButton.setObjectName(u"createDeckButton")

        self.verticalLayout.addWidget(self.createDeckButton)

        DeckCreationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DeckCreationWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 632, 22))
        DeckCreationWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DeckCreationWindow)
        self.statusbar.setObjectName(u"statusbar")
        DeckCreationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DeckCreationWindow)

        QMetaObject.connectSlotsByName(DeckCreationWindow)
    # setupUi

    def retranslateUi(self, DeckCreationWindow):
        DeckCreationWindow.setWindowTitle(QCoreApplication.translate("DeckCreationWindow", u"Create Deck", None))
        self.enterDeckLabel.setText(QCoreApplication.translate("DeckCreationWindow", u"Enter deck's name:", None))
        self.createDeckButton.setText(QCoreApplication.translate("DeckCreationWindow", u"Create Deck", None))
    # retranslateUi

