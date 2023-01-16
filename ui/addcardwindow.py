# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addcardwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddCardWindow(object):
    def setupUi(self, AddCardWindow):
        if not AddCardWindow.objectName():
            AddCardWindow.setObjectName(u"AddCardWindow")
        AddCardWindow.resize(480, 310)
        self.centralwidget = QWidget(AddCardWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cardFrontLabel = QLabel(self.centralwidget)
        self.cardFrontLabel.setObjectName(u"cardFrontLabel")

        self.verticalLayout.addWidget(self.cardFrontLabel)

        self.cardFrontEdit = QLineEdit(self.centralwidget)
        self.cardFrontEdit.setObjectName(u"cardFrontEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardFrontEdit.sizePolicy().hasHeightForWidth())
        self.cardFrontEdit.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.cardFrontEdit)

        self.cardBackLabel = QLabel(self.centralwidget)
        self.cardBackLabel.setObjectName(u"cardBackLabel")

        self.verticalLayout.addWidget(self.cardBackLabel)

        self.cardBackEdit = QLineEdit(self.centralwidget)
        self.cardBackEdit.setObjectName(u"cardBackEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cardBackEdit.sizePolicy().hasHeightForWidth())
        self.cardBackEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.cardBackEdit)

        self.addCardButton = QPushButton(self.centralwidget)
        self.addCardButton.setObjectName(u"addCardButton")

        self.verticalLayout.addWidget(self.addCardButton)

        AddCardWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AddCardWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        AddCardWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddCardWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddCardWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddCardWindow)

        QMetaObject.connectSlotsByName(AddCardWindow)
    # setupUi

    def retranslateUi(self, AddCardWindow):
        AddCardWindow.setWindowTitle(QCoreApplication.translate("AddCardWindow", u"Add Card", None))
        self.cardFrontLabel.setText(QCoreApplication.translate("AddCardWindow", u"Card front:", None))
        self.cardBackLabel.setText(QCoreApplication.translate("AddCardWindow", u"Card back:", None))
        self.addCardButton.setText(QCoreApplication.translate("AddCardWindow", u"Add card", None))
    # retranslateUi

