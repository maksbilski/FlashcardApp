from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from gui import Ui_MainWindow
from collection import Collection
from cards import Card
from queue import Queue
import sys


class FlashcardsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.setupDeckList()
        self.setupStateManagementAttributes()
        self.setupButtons()
        self.collection = Collection()

    def setupStateManagementAttributes(self):
        self.currentDeckListItem = None
        self.currentCard = None
        self.currentDeck = None

    def setupButtons(self):
        self.gui.cardList.itemDoubleClicked.connect(self.selectCard)
        # cardList buttons
        self.gui.cardRemoveButton.clicked.connect(self.removeCardAndSwitchPage) # NOQA
        self.gui.goBackButton.clicked.connect(lambda: self.selectDeck(self.currentDeckListItem)) # NOQA
        self.gui.reviewStartButton.clicked.connect(self.startReview)# NOQA
        # Card review buttons
        self.gui.showAnswerButton.clicked.connect(lambda: self.setupAnswerNotRecalledPage(self.currentReviewedCard)) # NOQA
        self.gui.submitAnswerButton.clicked.connect(lambda: self.validateAnswer(self.currentReviewedCard, self.gui.AnswerParser.text())) # NOQA

    def setupDeckList(self):
        '''
        This method sets up the deck list widget after
        the FlashcardWindow is initialized.
        '''
        self.gui.firstPageLabel.setText("Choose deck")
        for deck in self.collection.decklist:
            deck_list_item = QListWidgetItem(deck.name)
            deck_list_item.deck = deck
            self.gui.deckList.addItem(deck_list_item)
        self.gui.deckList.itemClicked.connect(self.selectDeck)

    def selectDeck(self, deck_list_item: QListWidgetItem) -> None:
        '''
        This method changes the stacked widget page to the one that displays
        selected deck card list.
        '''
        self.currentDeck, self.currentDeckListItem = deck_list_item.deck, deck_list_item # NOQA
        self.gui.cardList.clear()
        self.gui.deckStack.setCurrentIndex(1)
        for card in self.currentDeck.flashcards:
            card_list_item = QListWidgetItem(card.front)
            card_list_item.card = card
            self.gui.cardList.addItem(card_list_item)


    def selectCard(self, card_list_item: QListWidgetItem) -> None:
        self.currentCard = card_list_item.card
        self.gui.deckStack.setCurrentIndex(2)
        self.gui.cardDataLabel.setText(str(self.currentCard))

    def removeCardAndSwitchPage(self):
        self.currentDeck.remove_card(self.currentCard)
        self.selectDeck(self.currentDeckListItem)b

    def startReview(self):
        due_cards = self.currentDeck.get_due_cards()
        self.gui.deckStack.setCurrentIndex(3)
        self.reviewQueue = Queue()
        for card in due_cards:
            self.reviewQueue.put(card)
        self.reviewNextCard()

    def reviewNextCard(self):
        if self.reviewQueue.empty():
            self.reviewDone()
            return
        self.reviewCard(self.reviewQueue.get())

    def reviewCard(self, card):
        # Next line sets up the self.currentReviewedCard attribute value
        # to the card that was next in the self.reviewQueue, so that
        # the functions that are connected to showAnswerButton
        # and submitAnsweredButton get the current reviewed card.
        self.currentReviewedCard = card
        self.gui.cardFrontLabel.setText(card.front)
        self.gui.cardBackLabel.setText("")
        self.gui.reviewNotifierLabel.setText("")
        self.gui.reviewButtonsStack.setCurrentIndex(0)
        # Button connections are setup in FlashcardWindow.setupButtons method.

    def validateAnswer(self, card: Card, users_answer: str):
        if users_answer == card.back:
            self.setupAnswerRecalledPage(card)
        else:
            self.setupAnswerNotRecalledPage(card)

    # def setupAnswerRecalledPage(self, card, due_cards):
    #     text = "Correct answer!.\nHow easy was the information for you to recall?" # NOQA
    #     self.gui.ReviewNotifierLabel.setText(text)
    #     self.gui.CardBackLabel.setText(card.back)
    #     self.gui.ReviewButtonsStack.setCurrentIndex(1)
    #     self.gui.Q3Button.clicked.connect(lambda: self.reviewCardAndReviewNextCard(card, due_cards, 3)) # NOQA
    #     self.gui.Q4Button.clicked.connect(lambda: self.reviewCardAndReviewNextCard(card, due_cards, 3)) # NOQA
    #     self.gui.Q5Button.clicked.connect(lambda: self.reviewCardAndReviewNextCard(card, due_cards, 3)) # NOQA

    # def setupAnswerNotRecalledPage(self, card, due_cards):
    #     text = "Upon seeing the back of the card.\nHow familiar the information seems to you?" # NOQA
    #     self.gui.ReviewNotifierLabel.setText(text)
    #     self.gui.CardBackLabel.setText(card.back)
    #     self.gui.ReviewButtonsStack.setCurrentIndex(2)
    #     self.gui.Q0Button.clicked.connect(lambda: self.reviewCardAndReviewNextCard(card, due_cards, 0)) # NOQA
    #     self.gui.Q1Button.clicked.connect(lambda: self.reviewCardAndReviewNextCard(card, due_cards, 1)) # NOQA
    #     self.gui.Q2Button.clicked.connect(lambda: self.reviewCardAndReviewNextCard(card, due_cards, 2)) # NOQA

    # def reviewDone(self):
    #     self.gui.DeckStack.setCurrentIndex(0)
    #     self.gui.FirstPageLabel.setText("Congratulations!\n You have finished this deck for now.") # NOQA
    #     self.collection.update_serialized_data()
    #     self.collection.update_source_file()


def guiMain(args):
    app = QApplication(args)
    window = FlashcardsWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
