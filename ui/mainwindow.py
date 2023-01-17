# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flashcards_new.ui'
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
        MainWindow.resize(828, 780)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.deckCreateAction = QAction(MainWindow)
        self.deckCreateAction.setObjectName(u"deckCreateAction")
        self.statsViewer = QAction(MainWindow)
        self.statsViewer.setObjectName(u"statsViewer")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.deckList = QListWidget(self.layoutWidget)
        self.deckList.setObjectName(u"deckList")

        self.verticalLayout_9.addWidget(self.deckList)

        self.deckDeleteButtonStack = QStackedWidget(self.layoutWidget)
        self.deckDeleteButtonStack.setObjectName(u"deckDeleteButtonStack")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.deckDeleteButtonStack.sizePolicy().hasHeightForWidth())
        self.deckDeleteButtonStack.setSizePolicy(sizePolicy1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.deckDeleteButtonStack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_11 = QVBoxLayout(self.page_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.deckDeleteButton = QPushButton(self.page_2)
        self.deckDeleteButton.setObjectName(u"deckDeleteButton")
        self.deckDeleteButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.deckDeleteButton.sizePolicy().hasHeightForWidth())
        self.deckDeleteButton.setSizePolicy(sizePolicy2)
        self.deckDeleteButton.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_11.addWidget(self.deckDeleteButton, 0, Qt.AlignHCenter)

        self.deckExportButton = QPushButton(self.page_2)
        self.deckExportButton.setObjectName(u"deckExportButton")
        sizePolicy2.setHeightForWidth(self.deckExportButton.sizePolicy().hasHeightForWidth())
        self.deckExportButton.setSizePolicy(sizePolicy2)

        self.verticalLayout_11.addWidget(self.deckExportButton, 0, Qt.AlignHCenter)

        self.deckDeleteButtonStack.addWidget(self.page_2)

        self.verticalLayout_9.addWidget(self.deckDeleteButtonStack)

        self.splitter.addWidget(self.layoutWidget)
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
        self.dueCardCountLabel = QLabel(self.cardListPage)
        self.dueCardCountLabel.setObjectName(u"dueCardCountLabel")
        self.dueCardCountLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.dueCardCountLabel)

        self.showAddCardWindowButton = QPushButton(self.cardListPage)
        self.showAddCardWindowButton.setObjectName(u"showAddCardWindowButton")

        self.verticalLayout_2.addWidget(self.showAddCardWindowButton)

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

        self.reviewNotifierLabel = QLabel(self.cardReviewPage)
        self.reviewNotifierLabel.setObjectName(u"reviewNotifierLabel")
        self.reviewNotifierLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.reviewNotifierLabel)

        self.reviewButtonsStack = QStackedWidget(self.cardReviewPage)
        self.reviewButtonsStack.setObjectName(u"reviewButtonsStack")
        self.cardReviewingPage = QWidget()
        self.cardReviewingPage.setObjectName(u"cardReviewingPage")
        self.verticalLayout_8 = QVBoxLayout(self.cardReviewingPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
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
        self.cardTestingPage = QWidget()
        self.cardTestingPage.setObjectName(u"cardTestingPage")
        self.verticalLayout_12 = QVBoxLayout(self.cardTestingPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.submitTestAnswerButton = QPushButton(self.cardTestingPage)
        self.submitTestAnswerButton.setObjectName(u"submitTestAnswerButton")

        self.verticalLayout_12.addWidget(self.submitTestAnswerButton)

        self.testAnswerParser = QLineEdit(self.cardTestingPage)
        self.testAnswerParser.setObjectName(u"testAnswerParser")

        self.verticalLayout_12.addWidget(self.testAnswerParser)

        self.reviewButtonsStack.addWidget(self.cardTestingPage)

        self.verticalLayout_3.addWidget(self.reviewButtonsStack)

        self.deckStack.addWidget(self.cardReviewPage)
        self.testResultPage = QWidget()
        self.testResultPage.setObjectName(u"testResultPage")
        self.verticalLayout_15 = QVBoxLayout(self.testResultPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.testResultLabel = QLabel(self.testResultPage)
        self.testResultLabel.setObjectName(u"testResultLabel")

        self.verticalLayout_15.addWidget(self.testResultLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.correctlyAnsweredCardsListLabel = QLabel(self.testResultPage)
        self.correctlyAnsweredCardsListLabel.setObjectName(u"correctlyAnsweredCardsListLabel")

        self.verticalLayout_13.addWidget(self.correctlyAnsweredCardsListLabel)

        self.correctlyAnsweredCardsList = QListWidget(self.testResultPage)
        self.correctlyAnsweredCardsList.setObjectName(u"correctlyAnsweredCardsList")

        self.verticalLayout_13.addWidget(self.correctlyAnsweredCardsList)


        self.horizontalLayout.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.notCorrectlyAnsweredCardsListLabel = QLabel(self.testResultPage)
        self.notCorrectlyAnsweredCardsListLabel.setObjectName(u"notCorrectlyAnsweredCardsListLabel")

        self.verticalLayout_14.addWidget(self.notCorrectlyAnsweredCardsListLabel)

        self.notCorrectlyAnsweredCardsList = QListWidget(self.testResultPage)
        self.notCorrectlyAnsweredCardsList.setObjectName(u"notCorrectlyAnsweredCardsList")

        self.verticalLayout_14.addWidget(self.notCorrectlyAnsweredCardsList)


        self.horizontalLayout.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout)

        self.testFinishedNotifyLabel = QLabel(self.testResultPage)
        self.testFinishedNotifyLabel.setObjectName(u"testFinishedNotifyLabel")

        self.verticalLayout_15.addWidget(self.testFinishedNotifyLabel)

        self.deckStack.addWidget(self.testResultPage)
        self.splitter.addWidget(self.deckStack)

        self.horizontalLayout_3.addWidget(self.splitter)

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
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addSeparator()
        self.toolBar.addAction(self.deckCreateAction)
        self.toolBar.addAction(self.statsViewer)

        self.retranslateUi(MainWindow)

        self.deckDeleteButtonStack.setCurrentIndex(0)
        self.deckStack.setCurrentIndex(0)
        self.reviewButtonsStack.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Flashcard App", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import Deck...", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export...", None))
        self.deckCreateAction.setText(QCoreApplication.translate("MainWindow", u"Create Deck", None))
#if QT_CONFIG(tooltip)
        self.deckCreateAction.setToolTip(QCoreApplication.translate("MainWindow", u"Create Deck", None))
#endif // QT_CONFIG(tooltip)
        self.statsViewer.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.deckDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete Highlighted Deck", None))
        self.deckExportButton.setText(QCoreApplication.translate("MainWindow", u"Export Highlighted Deck", None))
        self.firstPageLabel.setText("")
        self.dueCardCountLabel.setText("")
        self.showAddCardWindowButton.setText(QCoreApplication.translate("MainWindow", u"Add Flashcard", None))
        self.testStartButton.setText(QCoreApplication.translate("MainWindow", u"Take Test", None))
        self.reviewStartButton.setText(QCoreApplication.translate("MainWindow", u"Review Deck", None))
        self.cardDataLabel.setText("")
        self.cardRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove Card", None))
        self.goBackButton.setText(QCoreApplication.translate("MainWindow", u"Go back to the card list", None))
        self.cardFrontLabel.setText("")
        self.cardBackLabel.setText("")
        self.reviewNotifierLabel.setText("")
        self.showAnswerButton.setText(QCoreApplication.translate("MainWindow", u"Show Answer", None))
        self.answerParser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the back of the card here", None))
        self.submitAnswerButton.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.Q5Button.setText(QCoreApplication.translate("MainWindow", u"Perfect Recall", None))
        self.Q4Button.setText(QCoreApplication.translate("MainWindow", u"Some Hesitation", None))
        self.Q3Button.setText(QCoreApplication.translate("MainWindow", u"Significant Effort To Recall", None))
        self.Q2Button.setText(QCoreApplication.translate("MainWindow", u"Seemed Easy To Remember", None))
        self.Q1Button.setText(QCoreApplication.translate("MainWindow", u"Felt Familiar", None))
        self.Q0Button.setText(QCoreApplication.translate("MainWindow", u"Total Blackout", None))
        self.submitTestAnswerButton.setText(QCoreApplication.translate("MainWindow", u"Submit Answer", None))
        self.testResultLabel.setText("")
        self.correctlyAnsweredCardsListLabel.setText(QCoreApplication.translate("MainWindow", u"Correctly answered cards:", None))
        self.notCorrectlyAnsweredCardsListLabel.setText(QCoreApplication.translate("MainWindow", u"Not correctly answered cards:", None))
        self.testFinishedNotifyLabel.setText(QCoreApplication.translate("MainWindow", u"You finished the test! Your stats have been updated based on the result. ", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

