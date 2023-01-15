from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from ui.addcardwindow import Ui_AddCardWindow
from ui.mainwindow import Ui_MainWindow
from collection import Collection
from cards import Card
from queue import Queue
import sys


class FlashcardsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.collection = Collection()
        self.setupDeckList()
        self.setupButtons()
        self.setupCardReviewQualityButtons()

    def setupButtons(self):
        # cardListPageButtons
        self.gui.goBackButton.clicked.connect(lambda: self.selectDeck(self.currentDeckListItem)) # NOQA
        self.gui.reviewStartButton.clicked.connect(self.startReview)# NOQA
        self.gui.cardList.itemDoubleClicked.connect(self.selectCard)
        # cardDataPage buttons
        self.gui.cardRemoveButton.clicked.connect(self.removeCardAndSwitchPage) # NOQA
        # Card review buttons
        self.gui.showAnswerButton.clicked.connect(lambda: self.setupCardAnsweredPage('not answered')) # NOQA
        self.gui.submitAnswerButton.clicked.connect(lambda: self.validateAnswer(self.gui.answerParser.text())) # NOQA
        # AddCardWindow show button
        self.gui.showAddCardWindowButton.clicked.connect(lambda: self.showAddCardWindow()) # NOQA

    def showAddCardWindow(self):
        self.addCardWindow = QMainWindow(self)
        self.addCardUi = Ui_AddCardWindow()
        self.addCardUi.setupUi(self.addCardWindow)
        self.addCardUi.addCardButton.clicked.connect(
            lambda: self.addNewCard(Card(
                self.addCardUi.cardFrontEdit.text(),
                self.addCardUi.cardBackEdit.text()
                ))
            )
        self.addCardWindow.show()

    def addNewCard(self, new_card: Card):
        self.currentDeck.add_card(new_card)
        self.collection.update_serialized_data()
        self.collection.update_source_file()
        self.selectDeck(self.currentDeckListItem)

    def setupCardReviewQualityButtons(self):
        self.gui.Q0Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(0)) # NOQA
        self.gui.Q1Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(1)) # NOQA
        self.gui.Q2Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(2)) # NOQA
        self.gui.Q3Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(3)) # NOQA
        self.gui.Q4Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(4)) # NOQA
        self.gui.Q5Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(5)) # NOQA

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
        due_cards_count = len(self.currentDeck.get_due_cards())
        self.gui.dueCardCountLabel.setText(f"Due card's count: {due_cards_count}") # NOQA
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
        self.selectDeck(self.currentDeckListItem)
        self.collection.update_serialized_data()
        self.collection.update_source_file()

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
        # Next line assigns the self.currentReviewedCard attribute value
        # to the card that was pased on from the queue so that this data
        # can be easily accessed from parts of GUI.
        self.gui.answerParser.clear()
        self.currentReviewedCard = card
        self.gui.cardFrontLabel.setText(card.front)
        self.gui.cardBackLabel.setText("")
        self.gui.reviewNotifierLabel.setText("")
        self.gui.reviewButtonsStack.setCurrentIndex(0)
        # Button connections are setup in FlashcardWindow.setupButtons method.

    def validateAnswer(self, users_answer: str):
        if users_answer == self.currentReviewedCard.back:
            self.setupCardAnsweredPage('answered')
        else:
            self.setupCardAnsweredPage('not answered')

    def setupCardAnsweredPage(self, answer_validation_result: str):
        notify_texts = {
            "answered": "correct answer!.\nHow easy was the information for you to recall?", # NOQA
            "not answered": "Upon seeing the back of the card\nhow familiar the information seems to you?" # NOQA
            }
        stack_indexes = {
            "answered": 1,
            "not answered": 2
            } # NOQA
        self.gui.reviewNotifierLabel.setText(notify_texts[answer_validation_result]) # NOQA
        self.gui.cardBackLabel.setText(self.currentReviewedCard.back)
        self.gui.reviewButtonsStack.setCurrentIndex(stack_indexes[answer_validation_result]) # NOQA
        # Button coinnections are setup in FlashcardWindow.setupCardReviewQualityButtons method # NOQA

    def calculateReviewDateCallNextCard(self, quality):
        '''
        Whole purpose of this method is to assign Card.review method call
        and FlashcardWindow.reviewNextCard to one pushButton.clicked signal.
        '''
        self.currentReviewedCard.calculate_review_date(quality)
        self.reviewNextCard()

    def reviewDone(self):
        self.gui.deckStack.setCurrentIndex(0)
        self.gui.firstPageLabel.setText("Congratulations!\n You have finished this deck for now.") # NOQA
        self.collection.update_serialized_data()
        self.collection.update_source_file()


def guiMain(args):
    app = QApplication(args)
    window = FlashcardsWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
