# Overview

FlashcardApp is an interactive flashcard study application designed to help users enhance their learning experience. The application allows users to create decks of flashcards, review them, and test their knowledge. The key features of the application are:

- **Deck Management**: Users can create decks of flashcards, with each deck having a specific topic or category. Users can import/export decks to/from JSON file format. Users can add flashcards to or remove them from these decks. 

- **Flashcards**: Each flashcard has a front side, which usually contains a question or a prompt, and a back side, which contains the answer or explanation. Additionally, each flashcard has a review date that the application uses to schedule review sessions.

- **Review Mode**: The “Start Review” button initiates a review session for flashcards whose review date has passed. In this mode, flashcards are presented to users one at a time. Users have the option to either type what they think is on the back of the card or click on “Show Answer” to see the back of the card. Regardless of the choice, users are prompted to self-assess their familiarity with the flashcard. This assessment is taken into account by an algorithm that calculates the next review date for that flashcard. The specifics of the algorithm are explained later in the readme. 

- **Testing Mode**: By clicking the “Start Test” button, users can start a test session where they will be shown the front of each flashcard in the deck in sequence. Users have to type what they think is on the back of the card. After the user submits their answer by clicking “Submit Answer,” the next flashcard is presented. At the end of the test session, the application displays the test results, including a list of flashcards the user answered correctly and another list of those answered incorrectly.

- **Statistics**: Users can track their learning progress and application usage through statistical data. This includes the total minutes spent using the app, total test sessions count, total review sessions count, and total card reviews count. The application also provides visualizations of daily statistics for the current month.

This application aims to offer a personalized and effective way for users to study various subjects through spaced repetition and self-assessment.

## Tech Stack

| Category           | Technologies               |
| ------------------ | -------------------------- |
| Front-end Framework | PySide2                   |
| Data Visualization  | Matplotlib                |
| Data Format         | JSON                      |
| Testing Framework   | Pytest                    |

### Front-end Framework
- **PySide2**: PySide2 is used for creating the graphical user interface (GUI) of FlashcardApp. It is the official Python module from the Qt for Python project, which provides Python bindings for the Qt application framework. PySide2 allows for the development of highly functional and visually appealing GUIs.

### Data Visualization
- **Matplotlib**: Matplotlib is used for plotting charts and visualizations. It is a popular Python plotting library that provides object-oriented APIs for embedding plots into applications.

### Data Format
- **JSON**: JSON (JavaScript Object Notation) is used for data interchange

### Testing Framework
- **Pytest**: Pytest is employed for testing the application. It’s a mature full-featured Python testing tool that helps in writing better programs.
