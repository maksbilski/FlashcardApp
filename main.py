from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from gui import Ui_MainWindow
from collection import Collection
import sys


class FlashcardsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.collection = Collection()
        #when the project will be done _setup_decks_list should be added to Ui_MainWindow class
        self.setup_decks_list()

    def setup_decks_list(self):
        '''
        This method sets up the deck list widget after
        the FlashcardWindow is initialized.
        '''
        self.gui.DeckStack.setCurrentIndex(0)
        for deck in self.collection.decklist:
            deck_list_item = QListWidgetItem(deck.name)
            deck_list_item.setData(1, deck)
            self.gui.DeckList.addItem(deck_list_item)
        self.gui.DeckList.itemClicked.connect(self.select_deck)

    def select_deck(self, deck_list_item: QListWidgetItem) -> None:
        '''
        This method changes the stacked widget page to the one that displays
        selected deck card list.
        '''
        self.gui.DeckCardList.clear()
        self.gui.DeckStack.setCurrentIndex(1)
        deck = deck_list_item.data(1)
        for card in deck.flashcards:
            card_list_item = QListWidgetItem(card.front)
            card_list_item.setData(1, card)
            card_list_item.setData(3, deck)
            self.gui.DeckCardList.addItem(card_list_item)
        self.gui.DeckCardList.itemDoubleClicked.connect(self.select_card)

    def select_card(self, card_list_item):
        '''
        This method changes the stacked widget page to the one that displays
        doubleclicked card information.
        '''
        card = card_list_item.data(1)
        deck = card_list_item.data(3)
        self.gui.DeckStack.setCurrentIndex(2)
        self.gui.CardDataLabel.setText(str(card))
        self.gui.CardRemoveButton.clicked.connect(self.remove_card(deck, card))
        self.gui.GoBackButton.clicked.connect(self.gui.DeckStack.setCurrentIndex)

    def remove_card(self, deck, card):
        deck.remove_card(card)
        self.collection.update_serialized_data()
        self.collection.update_source_file()
        self.gui.DeckStack.setCurrentIndex(1)

    def _start_review(self, listed_deck):
        pass

    def _start_test(self, listed_deck):
        pass


def guiMain(args):
    app = QApplication(args)
    window = FlashcardsWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
