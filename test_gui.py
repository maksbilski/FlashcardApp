from pytestqt import qtbot

def test_add_new_card(qtbot):
    # Create the main window and the add card dialog
    main_window = MainWindow()
    add_card_dialog = AddCardDialog(main_window)
    qtbot.addWidget(main_window)
    qtbot.addWidget(add_card_dialog)

    # Select a deck in the main window
    main_window.selectDeck(main_window.deck_list[0])

    # Open the add card dialog
    qtbot.mouseClick(main_window.addCardButton, QtCore.Qt.LeftButton)

    # Fill in the card front and back
    qtbot.keyClicks(add_card_dialog.card_front_edit, "Card front")
    qtbot.keyClicks(add_card_dialog.card_back_edit, "Card back")

    # Click the add card button
    qtbot.mouseClick(add_card_dialog.add_button, QtCore.Qt.LeftButton)

    # Check that the card was added to the current deck
    assert main_window.currentDeck.num_cards() == 1
    assert main_window.currentDeck.flashcards[0].front == "Card front"
    assert main_window.currentDeck.flashcards[0].back == "Card back"