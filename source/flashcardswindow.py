from PySide2.QtWidgets import (
    QMainWindow,
    QListWidgetItem,
    QMessageBox
)
from PySide2.QtCore import QElapsedTimer
from ui.iowindow import Ui_deckIOWindow
from ui.createdeckwindow import Ui_DeckCreationWindow
from ui.addcardwindow import Ui_AddCardWindow
from ui.mainwindow import Ui_MainWindow
from ui.statswindow import Ui_StatsWindow
from source.collection import Collection
from source.statisticshandler import StatisticsHandler
from source.cards import Card
from source.decks import Deck
from source.errors import EmptyUserInputError, MalformedDeckDataError
from queue import Queue

class FlashcardsWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        """
        Main window initialization method. Here the deck list widget is set up,
        which is something like a homepage and
        all buttons and action connection methods are called.
        """
        super().__init__(parent)
        self.elapsed_timer = QElapsedTimer()
        self.elapsed_timer.start()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.collection = Collection()
        self.statisticsHandler = StatisticsHandler()

        self.setupDeckList()
        self.setupActions()

        self.setupDeckListRelatedButtons()
        self.setupCardReviewQualityButtons()
        self.setupCardListRelatedPageButtons()
        self.setupCardDataPageButtons()
        self.setupCardTestingAndReviewPageButtons()

    def setupActions(self) -> None:
        """
        Connects actions to their designated methods.
        """
        self.gui.deckCreateAction.triggered.connect(self.showDeckCreatorWindow)
        self.gui.importDeckAction.triggered.connect(self.showDeckImportWindow)
        self.gui.showStatsAction.triggered.connect(self.showStatsWindow)

    def setupCardReviewQualityButtons(self) -> None:
        """
        Sets up all card familiarity buttons' connections,
        so when user clicks on a button, which he thinks represents
        his familiarity of the card stored in self.currentReviewedCard attribute, # NOQA
        self.calculatReviewDateCallNextCard(quality) will be called
        and quality argument will be an integer that is an integer
        representation of his familiarity of the card
        """
        self.gui.Q0Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(0)) # NOQA
        self.gui.Q1Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(1)) # NOQA
        self.gui.Q2Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(2)) # NOQA
        self.gui.Q3Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(3)) # NOQA
        self.gui.Q4Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(4)) # NOQA
        self.gui.Q5Button.clicked.connect(lambda: self.calculateReviewDateCallNextCard(5)) # NOQA

    def setupDeckListRelatedButtons(self) -> None:
        """
        Sets up all deck list related buttons.
        """
        self.gui.deckList.itemClicked.connect(self.selectDeck)
        self.gui.deckDeleteButton.clicked.connect(
            lambda: self.removeDeckAndSwitchPage())
        self.gui.deckExportButton.clicked.connect(self.showDeckExportWindow)
        self.gui.showAddCardWindowButton.clicked.connect(
            lambda: self.showAddCardWindow())

    def setupCardListRelatedPageButtons(self) -> None:
        """
        Sets up button connections, for buttons that are
        on the card list page.
        """
        self.gui.cardList.itemDoubleClicked.connect(self.selectCard)
        self.gui.testStartButton.clicked.connect(self.startTest)
        self.gui.reviewStartButton.clicked.connect(self.startReview)

    def setupCardDataPageButtons(self) -> None:
        """
        Sets up button connections, for buttons that
        are on cardData page
        """
        self.gui.cardRemoveButton.clicked.connect(self.removeCardAndSwitchPage)
        self.gui.goBackButton.clicked.connect(
            lambda: self.selectDeck(self.currentDeckListItem))

    def setupCardTestingAndReviewPageButtons(self) -> None:
        """
        Sets up button connections, for buttons that are displayed,
        when user is asked to enter the back of the card.
        """
        self.gui.showAnswerButton.clicked.connect(
            lambda: self.validateAnswer("not answered"))
        self.gui.submitAnswerButton.clicked.connect(
            lambda: self.validateAnswer(self.gui.answerParser.text()))
        self.gui.submitTestAnswerButton.clicked.connect(
            lambda: self.validateTestAnswer(self.gui.testAnswerParser.text())
        )

    def setupStatsWindowButtons(self):
        """
        Connect the buttons in the statistics window to the appropriate
        methods in the statisticsHandler for plotting daily statistics.
        """
        self.statsWindowUi.plotCardsReviewedButton.clicked.connect(
            lambda: self.statisticsHandler.plot_daily_stats('cards_reviewed'))
        self.statsWindowUi.plotTestSessionsButton.clicked.connect(
            lambda: self.statisticsHandler.plot_daily_stats('test_sessions'))
        self.statsWindowUi.plotMinutesButton.clicked.connect(
            lambda: self.statisticsHandler.plot_daily_stats('minutes'))
        self.statsWindowUi.plotReviewSessionsButton.clicked.connect(
            lambda: self.statisticsHandler.plot_daily_stats('review_sessions'))

    def showStatsWindow(self) -> None:
        """
        Show the statistics window with the current month's
        and total statistics displayed. Also, connects the buttons in the
        window to the appropriate methods in the statisticsHandler.
        """
        self.statsWindow = QMainWindow(self)
        self.statsWindowUi = Ui_StatsWindow()
        self.statsWindowUi.setupUi(self.statsWindow)
        self.setupStatsWindowButtons()

        current_month_stats = self.statisticsHandler.get_monthly_total()
        total_stats_stats = self.statisticsHandler.get_total_stats()
        self.statsWindowUi.statsDataLabel.setText(total_stats_stats)
        self.statsWindowUi.currentMonthsDataLabel.setText(current_month_stats)

        self.statsWindow.show()

    def showDeckImportWindow(self) -> None:
        """
        Shows the deck import window and sets up the UI.
        It also connects the import button to the importDeck method.
        """
        self.deckImportWindow = QMainWindow(self)
        self.deckImportUi = Ui_deckIOWindow()
        self.deckImportUi.setupUi(self.deckImportWindow)
        self.deckImportUi.ioLabel.setText("Enter path of imported deck:")
        self.deckImportWindow.show()
        self.deckImportUi.deckIOButton.setText("Import Deck")
        self.deckImportUi.deckIOButton.clicked.connect(
            lambda: self.importDeck(self.deckImportUi.pathParser.text()))

    def importDeck(self, filepath: str) -> None:
        """
        Imports the deck from the specified filepath,
        updates the source file and updates the deck list.

        :param filepath: str, path of the file that user wants to import

        :raises FileNotFoundError: if parsed pathfile doesn't exist
        :raises MalformedDeckDataError: if file at the filepath argument
            doesn't exist.
        """
        try:
            self.collection.import_deck_from_json(filepath)
            self.collection.update_source_file()
            self.setupDeckList()
            self.deckImportWindow.close()
        except FileNotFoundError as e:
            self.showError(e)
        except MalformedDeckDataError as e:
            self.showError(e)

    def showDeckExportWindow(self) -> None:
        """
        Shows the deck export window and sets up the UI.
        It also connects the export button to the importDeck method.
        Similar to how showDeckImportMethod works
        """
        self.deckExportWindow = QMainWindow(self)
        self.deckExportUi = Ui_deckIOWindow()
        self.deckExportUi.setupUi(self.deckExportWindow)
        self.deckExportUi.ioLabel.setText("Enter path of Exported deck:")
        self.deckExportWindow.show()
        self.deckExportUi.deckIOButton.setText("Exported Deck")
        self.deckExportUi.deckIOButton.clicked.connect(
            lambda: self.exportDeck(self.deckExportUi.pathParser.text()))

    def exportDeck(self, filepath: str) -> None:
        """
        Exports the deck the specified filepath.

        :param filepath: str, path at which de deck will be exported
        """
        try:
            self.collection.export_deck_to_json(self.currentDeck, filepath)
            self.deckExportWindow.close()
        except Exception as e:
            self.showError(e)

    def showAddCardWindow(self) -> None:
        """
        Opens a window for creating a new card,
        connects self.AddNewCard method to addCardButton,
        and parses texts entered by user to it.
        """
        self.addCardWindow = QMainWindow(self)
        self.addCardUi = Ui_AddCardWindow()
        self.addCardUi.setupUi(self.addCardWindow)
        self.addCardUi.addCardButton.clicked.connect(
            lambda: self.addNewCard(
                self.addCardUi.cardFrontEdit.text(),
                self.addCardUi.cardBackEdit.text()
                )
            )
        self.addCardWindow.show()

    def addNewCard(self, card_front: str, card_back: str) -> None:
        """
        Adds a new card to the current selected deck.

        :param card_front: str, Text that will be on the front of the card
        :param card_back: str, Text that will be on the back of the card

        :raises EmptyUserInpurtError: When card_front or card_back is empty.
        """
        try:
            if not card_front or not card_back:
                raise EmptyUserInputError(
                        "You can't create a card with an empty side")
            self.currentDeck.add_card(Card(card_front, card_back))
            self.collection.update_source_file()
            self.selectDeck(self.currentDeckListItem)
            self.addCardUi.cardFrontEdit.clear()
            self.addCardUi.cardBackEdit.clear()
        except EmptyUserInputError as e:
            self.showError(e)

    def showDeckCreatorWindow(self) -> None:
        """
        Opens a window for adding a new deck.
        Works similar to showAddCardWindow method.
        """
        self.createDeckWindow = QMainWindow(self)
        self.createDeckUi = Ui_DeckCreationWindow()
        self.createDeckUi.setupUi(self.createDeckWindow)
        self.createDeckUi.createDeckButton.clicked.connect(
            lambda: self.createNewDeck(
                self.createDeckUi.deckNameEdit.text()
            )
        )
        self.createDeckWindow.show()

    def createNewDeck(self, new_deck_name: str) -> None:
        """
        Creates a new deck with the given name
        and adds it to the collection of flashcards.

        :param new_deck_name: str, The name of the new deck

        :raises EmptyUserInputError: If new_deck_name is empty or None
        """
        try:
            if not new_deck_name:
                raise EmptyUserInputError(
                        "You can't create a deck without a name")
            self.collection.add_deck(Deck(new_deck_name))
            self.collection.update_source_file()
            self.setupDeckList()
            self.createDeckWindow.close()
        except EmptyUserInputError as e:
            self.showError(e)

    def showError(self, e: Exception) -> None:
        """
        Displays an error message in a QMessageBox.

        :param e: Exception, exception object that contains an error message.
        """
        error_message = QMessageBox()
        error_message.setIcon(QMessageBox.Warning)
        error_message.setText(str(e))
        error_message.setWindowTitle("Error")
        error_message.exec()

    def setupDeckList(self) -> None:
        """
        Populate the deck list widget with the decks from the collection.
        """
        self.gui.deckList.clear()
        self.gui.firstPageLabel.setText("Choose deck")
        for deck in self.collection.decklist:
            deck_list_item = QListWidgetItem(deck.name)
            deck_list_item.deck = deck
            self.gui.deckList.addItem(deck_list_item)

    def removeDeckAndSwitchPage(self) -> None:
        """
        Removes the currently selected deck from the collection
        and updates the deck list on the GUI.
        Also updates the serialized data and source file for the collection.
        """
        self.collection.decklist.remove(self.currentDeck)
        self.setupDeckList()
        self.collection.update_source_file()
        self.gui.deckStack.setCurrentIndex(0)
        self.gui.deckDeleteButtonStack.setCurrentIndex(0)

    def selectDeck(self, deck_list_item: QListWidgetItem) -> None:
        """
        This method changes the stacked widget page to the one that displays
        selected deck card list.
        """
        self.currentDeck, self.currentDeckListItem = deck_list_item.deck, deck_list_item # NOQA
        self.gui.cardList.clear()
        due_cards_count = len(self.currentDeck.get_due_cards())
        self.gui.dueCardCountLabel.setText(f"Due card's count: {due_cards_count}") # NOQA
        self.gui.deckStack.setCurrentIndex(1)
        self.gui.deckDeleteButtonStack.setCurrentIndex(1)
        self.setupCardList()

    def setupCardList(self) -> None:
        """
        Populates the card list widget with cards from the selected deck.
        """
        for card in self.currentDeck.flashcards:
            card_list_item = QListWidgetItem(card.front)
            card_list_item.card = card
            self.gui.cardList.addItem(card_list_item)

    def selectCard(self, card_list_item: QListWidgetItem) -> None:
        """
        Selects and displays the data of the selected card from the card list.

        :param card_list_item: The selected card's QListWidgetItem
        """
        self.currentCard = card_list_item.card
        self.gui.deckStack.setCurrentIndex(2)
        self.gui.cardDataLabel.setText(str(self.currentCard))

    def removeCardAndSwitchPage(self):
        """
        Removes the currently selected card from the current deck
        and updates the card list page.

        This method first removes the card by calling the remove_card() method
        on the current deck with the current card as an argument.
        Then it calls selectDeck() method with the current deck list item
        to update the card list page.
        It also updates the serialized data and source file.
        """
        self.currentDeck.remove_card(self.currentCard)
        self.selectDeck(self.currentDeckListItem)
        self.collection.update_source_file()

    def startTest(self) -> None:
        """
        This method starts a test session for the current selected deck.
        It changes the current page of stacked widget to test page,
        and initializes the testQueue with the flashcards of the current deck.
        It also calls the testNextCardFromTheQueue method
        to start displaying the first card in the test queue.
        """
        self.gui.reviewButtonsStack.setCurrentIndex(3)
        self.gui.deckStack.setCurrentIndex(4)
        self.gui.deckStack.setCurrentIndex(3)
        self.testQueue = Queue()
        for card in self.currentDeck.flashcards:
            self.testQueue.put(card)
        self.testNextCardFromTheQueue()

    def testNextCardFromTheQueue(self):
        """
        Retrieves the next card from the testQueue
        and calls the testCard method on it.
        If the testQueue is empty, the testDone method is called.
        """
        if self.testQueue.empty():
            self.testDone()
            return
        self.testCard(self.testQueue.get())

    def testCard(self, card: Card) -> None:
        """
        Displays the front side of the card and prepares
        the user input field for answering.
        Also, it sets the current tested card attribute to the provided card.
        It also prepares the UI for test by clearing the answer field
        and hiding the backside of the card.

        :param card: Card, The card object to be tested
        """
        self.gui.testAnswerParser.clear()
        self.currentTestedCard = card
        self.gui.cardFrontLabel.setText(self.currentTestedCard.front)
        self.gui.cardBackLabel.setText("")
        self.gui.reviewNotifierLabel.setText("")
        self.gui.reviewButtonsStack.setCurrentIndex(4)

    def validateTestAnswer(self, users_answer: str) -> None:
        """
        Validates the answer given by the user during a test and
        updates the list of correctly and incorrectly answered cards.
        Proceeds to the next card in the test queue.
        I convert both users_answer and self.currentTestedCard.back
        to lowercase so the answer validations isn't case-sensitive.

        :param users_answer: str, The answer given by the user
        """
        if users_answer.strip().lower() == self.currentTestedCard.back.lower():
            self.gui.correctlyAnsweredCardsList.addItem(
                QListWidgetItem(self.currentTestedCard.front)
            )
        else:
            self.gui.notCorrectlyAnsweredCardsList.addItem(
                QListWidgetItem(self.currentTestedCard.front)
            )
        self.testNextCardFromTheQueue()

    def testDone(self) -> None:
        """
        Sets up test result page and populates it with data about
        users tests results, including the number of correctly answered cards,
        the total number of cards, and the percentage of correct answers.

        It also updates the statistics data in self.statisticsHandler
        attribute and saves these changes to the source file.
        """
        self.gui.deckStack.setCurrentIndex(4)
        correct_answers_count = self.gui.correctlyAnsweredCardsList.count()
        total_cards_count = len(self.currentDeck.flashcards)
        test_result_percentage = (
            round((correct_answers_count / total_cards_count) * 100, 2)
        )
        self.gui.testResultLabel.setText(
            f"Result: {correct_answers_count}/{total_cards_count}({test_result_percentage}%)" # NOQA
        )
        self.statisticsHandler.update_data(test_sessions=1)
        self.statisticsHandler.update_source_file()

    def startReview(self) -> None:
        """
        The function startReview() starts a review session
        for the current selected deck. It changes the current page
        of stacked widget to the review page and initializes the reviewQueue
        with the flashcards of the current deck that are due for review.
        It also calls the reviewNextCardFromTheQueue() method
        to start displaying the first card in the review queue.
        """
        due_cards = self.currentDeck.get_due_cards()
        self.gui.deckStack.setCurrentIndex(3)
        self.reviewQueue = Queue()
        for card in due_cards:
            self.reviewQueue.put(card)
        self.reviewNextCardFromTheQueue()

    def reviewNextCardFromTheQueue(self) -> None:
        """
        Retrieves the next card from the reviewQueue
        and calls the testCard method on it.
        If the testQueue is empty, the testDone method is called.
        """
        if self.reviewQueue.empty():
            self.reviewDone()
            return
        self.reviewCard(self.reviewQueue.get())

    def reviewCard(self, card: Card) -> None:
        """
        This function assigns the passed in card to the
        scurrent reviewed card attribute.
        Also, it sets the current reviewd card attribute to the provided card.
        It also prepares the UI for review by clearing the answer field
        and hiding the backside of the card.

        :param card: Card, the Card object to be reviewed
        """
        self.gui.answerParser.clear()
        self.currentReviewedCard = card
        self.gui.cardFrontLabel.setText(self.currentReviewedCard.front)
        self.gui.cardBackLabel.setText("")
        self.gui.reviewNotifierLabel.setText("")
        self.gui.reviewButtonsStack.setCurrentIndex(0)

    def validateAnswer(self, users_answer: str) -> None:
        """
        Validates the answer passed by the user and returns
        a string that indicates if the answer was correct or not.
        It also updates the statistics, by incrementing the
        cards_reviewed key value by one.

        :param users_answer: bool, True if users answer was correct
                        False if it wasn't

        """
        if users_answer.strip().lower() == self.currentReviewedCard.back.lower(): # NOQA
            self.setupCardAnsweredPage(True)
        else:
            self.setupCardAnsweredPage(False)
        self.statisticsHandler.update_data(cards_reviewed=1)

    def setupCardAnsweredPage(self, answer_validation_result: bool) -> None:
        """
        This method sets up the user interface for the page
        that appears after the user has answered a flashcard.
        It displays the back of the card, and sets up the buttons
        for rating familiarity of the information on the card.
        :param answer_validation_result: represents whether the user's answer
            was correct or not. It's either True or False.
        :type answer_validation_result: str
        """
        notify_texts = {
            True: (
                "Correct answer!.\n"
                "How easy was the information for you to recall?"
                ),
            False: (
                "You didn't know the Answer.\n"
                "Upon seeing the back of the card\n"
                "how familiar the information seems to you?"
                )
            }
        stack_indexes = {
            True: 1,
            False: 2
            }
        self.gui.reviewNotifierLabel.setText(notify_texts[answer_validation_result]) # NOQA
        self.gui.cardBackLabel.setText(self.currentReviewedCard.back)
        self.gui.reviewButtonsStack.setCurrentIndex(stack_indexes[answer_validation_result]) # NOQA

    def calculateReviewDateCallNextCard(self, quality) -> None:
        """
        Calculates the next review date for the current card
        based on the given quality and reviews the next card from the queue
        Purpose of this method is to connect these two functions
        calls to one button click.
        :param quality: int, represents the quality of user's familiarity
            currently reviewed card.
        """
        self.currentReviewedCard.calculate_review_date(quality)
        self.reviewNextCardFromTheQueue()

    def reviewDone(self) -> None:
        """
        Sets up the user interface for the page that appears
        after the user has finished reviewing all the cards
        in the current deck.

        It also updates the serialized data and the source file
        with the current state of the self.collection attribute
        so all of the cards' updated review dates are saved

        It also updates the statistics data in self.statisticsHandler
        attribute and saves these changes to the source file
        """
        self.gui.deckStack.setCurrentIndex(0)
        self.gui.firstPageLabel.setText(
            "Congratulations!\n You have finished this deck for now.\n"
            "If you wish to study outside the planned schedule\n"
            "you can take a test from the card list page."
            )
        self.statisticsHandler.update_data(review_sessions=1)
        self.statisticsHandler.update_source_file()
        self.collection.update_source_file()

    def closeEvent(self, event) -> None:
        """
        Reimplemented method that is called when the window is closed.
        It calculates the elapsed time in seconds since the window was opened,
        updates the statistics and saves it to file.

        :param event: QCloseEvent, Event object containing information
            about the close event
        """
        # get elapsed time and convert it to seconds
        elapsed_time_in_seconds = round(self.elapsed_timer.elapsed() / 1000)
        self.statisticsHandler.update_data(seconds=elapsed_time_in_seconds)
        self.statisticsHandler.update_source_file()
        super().closeEvent(event)