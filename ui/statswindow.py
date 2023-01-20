# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statsdatawindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StatsWindow(object):
    def setupUi(self, StatsWindow):
        if not StatsWindow.objectName():
            StatsWindow.setObjectName(u"StatsWindow")
        StatsWindow.resize(595, 416)
        self.centralwidget = QWidget(StatsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plotMinutesButton = QPushButton(self.centralwidget)
        self.plotMinutesButton.setObjectName(u"plotMinutesButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotMinutesButton.sizePolicy().hasHeightForWidth())
        self.plotMinutesButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.plotMinutesButton)

        self.plotTestSessionsButton = QPushButton(self.centralwidget)
        self.plotTestSessionsButton.setObjectName(u"plotTestSessionsButton")
        sizePolicy.setHeightForWidth(self.plotTestSessionsButton.sizePolicy().hasHeightForWidth())
        self.plotTestSessionsButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.plotTestSessionsButton)

        self.plotCardsReviewedButton = QPushButton(self.centralwidget)
        self.plotCardsReviewedButton.setObjectName(u"plotCardsReviewedButton")
        sizePolicy.setHeightForWidth(self.plotCardsReviewedButton.sizePolicy().hasHeightForWidth())
        self.plotCardsReviewedButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.plotCardsReviewedButton)

        self.plotReviewSessionsButton = QPushButton(self.centralwidget)
        self.plotReviewSessionsButton.setObjectName(u"plotReviewSessionsButton")
        sizePolicy.setHeightForWidth(self.plotReviewSessionsButton.sizePolicy().hasHeightForWidth())
        self.plotReviewSessionsButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.plotReviewSessionsButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.statsDataLabel = QLabel(self.centralwidget)
        self.statsDataLabel.setObjectName(u"statsDataLabel")

        self.verticalLayout_2.addWidget(self.statsDataLabel)

        self.currentMonthsDataLabel = QLabel(self.centralwidget)
        self.currentMonthsDataLabel.setObjectName(u"currentMonthsDataLabel")

        self.verticalLayout_2.addWidget(self.currentMonthsDataLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        StatsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StatsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 595, 22))
        StatsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StatsWindow)
        self.statusbar.setObjectName(u"statusbar")
        StatsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StatsWindow)

        QMetaObject.connectSlotsByName(StatsWindow)
    # setupUi

    def retranslateUi(self, StatsWindow):
        StatsWindow.setWindowTitle(QCoreApplication.translate("StatsWindow", u"Stats", None))
        self.plotMinutesButton.setText(QCoreApplication.translate("StatsWindow", u"Plot current month's daily minutes count", None))
        self.plotTestSessionsButton.setText(QCoreApplication.translate("StatsWindow", u"Plot current month's daily test sessions count", None))
        self.plotCardsReviewedButton.setText(QCoreApplication.translate("StatsWindow", u"Plot current month's daily cards review count", None))
        self.plotReviewSessionsButton.setText(QCoreApplication.translate("StatsWindow", u"Plot current month's daily review session count", None))
        self.statsDataLabel.setText("")
        self.currentMonthsDataLabel.setText("")
    # retranslateUi

