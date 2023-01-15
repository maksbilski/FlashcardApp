# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flashcards.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 757)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.DeckAdder = QAction(MainWindow)
        self.DeckAdder.setObjectName(u"DeckAdder")
        self.FlashcardAdder = QAction(MainWindow)
        self.FlashcardAdder.setObjectName(u"FlashcardAdder")
        self.StatsViewer = QAction(MainWindow)
        self.StatsViewer.setObjectName(u"StatsViewer")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.deckList = QListWidget(self.splitter)
        self.deckList.setObjectName(u"deckList")
        self.splitter.addWidget(self.deckList)
        self.deckStack = QStackedWidget(self.splitter)
        self.deckStack.setObjectName(u"deckStack")
        self.firstPage = QWidget()
        self.firstPage.setObjectName(u"firstPage")
        self.verticalLayout = QVBoxLayout(self.firstPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.firstPageLabel = QLabel(self.firstPage)
        self.firstPageLabel.setObjectName(u"firstPageLabel")
        self.firstPageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.firstPageLabel)

        self.deckStack.addWidget(self.firstPage)
        self.cardListPage = QWidget()
        self.cardListPage.setObjectName(u"cardListPage")
        self.verticalLayout_2 = QVBoxLayout(self.cardListPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cardList = QListWidget(self.cardListPage)
        self.cardList.setObjectName(u"cardList")

        self.verticalLayout_2.addWidget(self.cardList)

        self.testStartButton = QPushButton(self.cardListPage)
        self.testStartButton.setObjectName(u"testStartButton")

        self.verticalLayout_2.addWidget(self.testStartButton)

        self.reviewStartButton = QPushButton(self.cardListPage)
        self.reviewStartButton.setObjectName(u"reviewStartButton")

        self.verticalLayout_2.addWidget(self.reviewStartButton)

        self.deckStack.addWidget(self.cardListPage)
        self.cardDataPage = QWidget()
        self.cardDataPage.setObjectName(u"cardDataPage")
        self.verticalLayout_4 = QVBoxLayout(self.cardDataPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cardDataLabel = QLabel(self.cardDataPage)
        self.cardDataLabel.setObjectName(u"cardDataLabel")
        self.cardDataLabel.setLayoutDirection(Qt.LeftToRight)
        self.cardDataLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.cardDataLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.cardRemoveButton = QPushButton(self.cardDataPage)
        self.cardRemoveButton.setObjectName(u"cardRemoveButton")

        self.verticalLayout_4.addWidget(self.cardRemoveButton)

        self.goBackButton = QPushButton(self.cardDataPage)
        self.goBackButton.setObjectName(u"goBackButton")

        self.verticalLayout_4.addWidget(self.goBackButton)

        self.deckStack.addWidget(self.cardDataPage)
        self.cardReviewPage = QWidget()
        self.cardReviewPage.setObjectName(u"cardReviewPage")
        self.verticalLayout_3 = QVBoxLayout(self.cardReviewPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cardFrontLabel = QLabel(self.cardReviewPage)
        self.cardFrontLabel.setObjectName(u"cardFrontLabel")
        self.cardFrontLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.cardFrontLabel)

        self.cardBackLabel = QLabel(self.cardReviewPage)
        self.cardBackLabel.setObjectName(u"cardBackLabel")
        self.cardBackLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.cardBackLabel)

        self.verticalSpacer = QSpacerItem(138, 488, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.reviewButtonsStack = QStackedWidget(self.cardReviewPage)
        self.reviewButtonsStack.setObjectName(u"reviewButtonsStack")
        self.cardReviewingPage = QWidget()
        self.cardReviewingPage.setObjectName(u"cardReviewingPage")
        self.verticalLayout_8 = QVBoxLayout(self.cardReviewingPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.reviewNotifierLabel = QLabel(self.cardReviewingPage)
        self.reviewNotifierLabel.setObjectName(u"reviewNotifierLabel")
        self.reviewNotifierLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.reviewNotifierLabel)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.showAnswerButton = QPushButton(self.cardReviewingPage)
        self.showAnswerButton.setObjectName(u"showAnswerButton")

        self.verticalLayout_5.addWidget(self.showAnswerButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.answerParser = QLineEdit(self.cardReviewingPage)
        self.answerParser.setObjectName(u"answerParser")
        self.answerParser.setAutoFillBackground(False)
        self.answerParser.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.answerParser)

        self.submitAnswerButton = QPushButton(self.cardReviewingPage)
        self.submitAnswerButton.setObjectName(u"submitAnswerButton")

        self.horizontalLayout_2.addWidget(self.submitAnswerButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.reviewButtonsStack.addWidget(self.cardReviewingPage)
        self.recalledAnswerPage = QWidget()
        self.recalledAnswerPage.setObjectName(u"recalledAnswerPage")
        self.verticalLayout_6 = QVBoxLayout(self.recalledAnswerPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Q5Button = QPushButton(self.recalledAnswerPage)
        self.Q5Button.setObjectName(u"Q5Button")

        self.verticalLayout_6.addWidget(self.Q5Button)

        self.Q4Button = QPushButton(self.recalledAnswerPage)
        self.Q4Button.setObjectName(u"Q4Button")

        self.verticalLayout_6.addWidget(self.Q4Button)

        self.Q3Button = QPushButton(self.recalledAnswerPage)
        self.Q3Button.setObjectName(u"Q3Button")

        self.verticalLayout_6.addWidget(self.Q3Button)

        self.reviewButtonsStack.addWidget(self.recalledAnswerPage)
        self.notRecalledAnswerPage = QWidget()
        self.notRecalledAnswerPage.setObjectName(u"notRecalledAnswerPage")
        self.verticalLayout_7 = QVBoxLayout(self.notRecalledAnswerPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Q2Button = QPushButton(self.notRecalledAnswerPage)
        self.Q2Button.setObjectName(u"Q2Button")

        self.verticalLayout_7.addWidget(self.Q2Button)

        self.Q1Button = QPushButton(self.notRecalledAnswerPage)
        self.Q1Button.setObjectName(u"Q1Button")

        self.verticalLayout_7.addWidget(self.Q1Button)

        self.Q0Button = QPushButton(self.notRecalledAnswerPage)
        self.Q0Button.setObjectName(u"Q0Button")

        self.verticalLayout_7.addWidget(self.Q0Button)

        self.reviewButtonsStack.addWidget(self.notRecalledAnswerPage)

        self.verticalLayout_3.addWidget(self.reviewButtonsStack)

        self.deckStack.addWidget(self.cardReviewPage)
        self.splitter.addWidget(self.deckStack)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 828, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.toolBar.addAction(self.DeckAdder)
        self.toolBar.addAction(self.FlashcardAdder)
        self.toolBar.addAction(self.StatsViewer)

        self.retranslateUi(MainWindow)

        self.deckStack.setCurrentIndex(0)
        self.reviewButtonsStack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Flashcard App", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import...", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export...", None))
        self.DeckAdder.setText(QCoreApplication.translate("MainWindow", u"Add Deck", None))
        self.FlashcardAdder.setText(QCoreApplication.translate("MainWindow", u"Add Flashcard", None))
        self.StatsViewer.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.firstPageLabel.setText("")
        self.testStartButton.setText(QCoreApplication.translate("MainWindow", u"Take Test", None))
        self.reviewStartButton.setText(QCoreApplication.translate("MainWindow", u"Review Deck", None))
        self.cardDataLabel.setText("")
        self.cardRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove Card", None))
        self.goBackButton.setText(QCoreApplication.translate("MainWindow", u"Go back to the card list", None))
        self.cardFrontLabel.setText("")
        self.cardBackLabel.setText("")
        self.reviewNotifierLabel.setText("")
        self.showAnswerButton.setText(QCoreApplication.translate("MainWindow", u"Show Answer", None))
        self.answerParser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Answer", None))
        self.submitAnswerButton.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.Q5Button.setText(QCoreApplication.translate("MainWindow", u"Perfect Recall", None))
        self.Q4Button.setText(QCoreApplication.translate("MainWindow", u"Some Hesitation", None))
        self.Q3Button.setText(QCoreApplication.translate("MainWindow", u"Significant Effort To Recall", None))
        self.Q2Button.setText(QCoreApplication.translate("MainWindow", u"Seemed Easy To Remember", None))
        self.Q1Button.setText(QCoreApplication.translate("MainWindow", u"Felt Familiar", None))
        self.Q0Button.setText(QCoreApplication.translate("MainWindow", u"Total Blackout", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

