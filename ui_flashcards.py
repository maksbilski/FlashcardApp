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
        MainWindow.resize(828, 714)
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
        self.DeckList = QListWidget(self.splitter)
        self.DeckList.setObjectName(u"DeckList")
        self.splitter.addWidget(self.DeckList)
        self.DeckStack = QStackedWidget(self.splitter)
        self.DeckStack.setObjectName(u"DeckStack")
        self.FirstPage = QWidget()
        self.FirstPage.setObjectName(u"FirstPage")
        self.verticalLayout = QVBoxLayout(self.FirstPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ChooseDeckLabel = QLabel(self.FirstPage)
        self.ChooseDeckLabel.setObjectName(u"ChooseDeckLabel")
        self.ChooseDeckLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ChooseDeckLabel)

        self.DeckStack.addWidget(self.FirstPage)
        self.DeckFlashcardListPage = QWidget()
        self.DeckFlashcardListPage.setObjectName(u"DeckFlashcardListPage")
        self.verticalLayout_2 = QVBoxLayout(self.DeckFlashcardListPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.DeckCardList = QListWidget(self.DeckFlashcardListPage)
        self.DeckCardList.setObjectName(u"DeckCardList")

        self.verticalLayout_2.addWidget(self.DeckCardList)

        self.TestStartButton = QPushButton(self.DeckFlashcardListPage)
        self.TestStartButton.setObjectName(u"TestStartButton")

        self.verticalLayout_2.addWidget(self.TestStartButton)

        self.ReviewStartButton = QPushButton(self.DeckFlashcardListPage)
        self.ReviewStartButton.setObjectName(u"ReviewStartButton")

        self.verticalLayout_2.addWidget(self.ReviewStartButton)

        self.DeckStack.addWidget(self.DeckFlashcardListPage)
        self.CardDataPage = QWidget()
        self.CardDataPage.setObjectName(u"CardDataPage")
        self.verticalLayout_4 = QVBoxLayout(self.CardDataPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.CardDataLabel = QLabel(self.CardDataPage)
        self.CardDataLabel.setObjectName(u"CardDataLabel")
        self.CardDataLabel.setLayoutDirection(Qt.LeftToRight)
        self.CardDataLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.CardDataLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.CardRemoveButton = QPushButton(self.CardDataPage)
        self.CardRemoveButton.setObjectName(u"CardRemoveButton")

        self.verticalLayout_4.addWidget(self.CardRemoveButton)

        self.GoBackButton = QPushButton(self.CardDataPage)
        self.GoBackButton.setObjectName(u"GoBackButton")

        self.verticalLayout_4.addWidget(self.GoBackButton)

        self.DeckStack.addWidget(self.CardDataPage)
        self.CardReviewPage = QWidget()
        self.CardReviewPage.setObjectName(u"CardReviewPage")
        self.verticalLayout_3 = QVBoxLayout(self.CardReviewPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CardFrontLabel = QLabel(self.CardReviewPage)
        self.CardFrontLabel.setObjectName(u"CardFrontLabel")
        self.CardFrontLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.CardFrontLabel)

        self.verticalSpacer = QSpacerItem(138, 488, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.ReviewButtonsStack = QStackedWidget(self.CardReviewPage)
        self.ReviewButtonsStack.setObjectName(u"ReviewButtonsStack")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ShowAnswerButton = QPushButton(self.page)
        self.ShowAnswerButton.setObjectName(u"ShowAnswerButton")

        self.verticalLayout_5.addWidget(self.ShowAnswerButton)

        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.ReviewButtonsStack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.ReviewButtonsStack.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.ReviewButtonsStack)

        self.DeckStack.addWidget(self.CardReviewPage)
        self.splitter.addWidget(self.DeckStack)

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

        self.DeckStack.setCurrentIndex(2)
        self.ReviewButtonsStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Flashcard App", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import...", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export...", None))
        self.DeckAdder.setText(QCoreApplication.translate("MainWindow", u"Add Deck", None))
        self.FlashcardAdder.setText(QCoreApplication.translate("MainWindow", u"Add Flashcard", None))
        self.StatsViewer.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.ChooseDeckLabel.setText(QCoreApplication.translate("MainWindow", u"Choose Deck", None))
        self.TestStartButton.setText(QCoreApplication.translate("MainWindow", u"Take Test", None))
        self.ReviewStartButton.setText(QCoreApplication.translate("MainWindow", u"Review Deck", None))
        self.CardDataLabel.setText("")
        self.CardRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove Card", None))
        self.GoBackButton.setText(QCoreApplication.translate("MainWindow", u"Go back to the card list", None))
        self.CardFrontLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ShowAnswerButton.setText(QCoreApplication.translate("MainWindow", u"Show Answer", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Answer", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

