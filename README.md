## Overview

FlashcardApp is an interactive flashcard study application designed to help users enhance their learning experience. The application allows users to create decks of flashcards, review them, and test their knowledge. The key features of the application are:

- **Deck Management**: Users can create decks of flashcards, with each deck having a specific topic or category. Users can import/export decks to/from JSON file format. Users can add flashcards to or remove them from these decks. 

- **Flashcards**: Each flashcard has a front side, which usually contains a question or a prompt, and a back side, which contains the answer or explanation. Additionally, each flashcard has a review date that the application uses to schedule review sessions.

- **Review Mode**: The “Start Review” button initiates a review session for flashcards whose review date has passed. In this mode, flashcards are presented to users one at a time. Users have the option to either type what they think is on the back of the card or click on “Show Answer” to see the back of the card. Regardless of the choice, users are prompted to self-assess their familiarity with the flashcard. This assessment is taken into account by an algorithm that calculates the next review date for that flashcard. The specifics of the algorithm are explained later in the readme. 

- **Testing Mode**: By clicking the “Start Test” button, users can start a test session where they will be shown the front of each flashcard in the deck in sequence. Users have to type what they think is on the back of the card. After the user submits their answer by clicking “Submit Answer,” the next flashcard is presented. At the end of the test session, the application displays the test results, including a list of flashcards the user answered correctly and another list of those answered incorrectly.

- **Statistics**: Users can track their learning progress and application usage through statistical data. This includes the total minutes spent using the app, total test sessions count, total review sessions count, and total card reviews count. The application also provides visualizations of daily statistics for the current month.


## Tech Stack

| Category           | Technologies               |
| ------------------ | -------------------------- |
| Front-end Framework | PySide2                   |
| Data Visualization  | Matplotlib                |
| Data Format         | JSON                      |
| Testing Framework   | Pytest                    |

### Front-end Framework
- **PySide2**: PySide2 is used for creating the graphical user interface (GUI) of FlashcardApp. It is the official Python module from the Qt for Python project, which provides Python bindings for the Qt application framework. PySide2 allows for the development of highly functional and visually appealing GUIs.


## Installation steps

1. **Clone the Repository**: First, clone the FlashcardApp repository to your local machine. You can do this using Git via the command line:

    ```sh
    git clone https://github.com/YOUR_GITHUB_USERNAME/FlashcardApp.git
    ```

    Alternatively, you can download the ZIP archive of the repository from GitHub and extract it.

2. **Navigate to the Repository Directory**: Use the command line to navigate into the directory where the repository has been cloned or extracted.

    ```sh
    cd FlashcardApp
    ```

3. **Install Dependencies**: FlashcardApp requires some additional Python libraries. Install these by executing the following command:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Application**: Once the dependencies are installed, you can run FlashcardApp by executing:

    ```sh
    python main.py
    ```


## Review Mode and the SM-2 Algorithm

The SM-2 algorithm is used in Review Mode to calculate the optimal intervals between reviews, enhancing memory retention. Here’s how it's integrated:

The user’s personal rating of their knowledge of the flashcard plays a crucial role. The user rates their recall on a scale (e.g., from 0 to 5), with higher values indicating easier recall.

Based on this rating, the SM-2 algorithm adjusts the Easiness Factor (EF) and calculates the next review date. The algorithm takes into account the number of times the card has been reviewed (n) and uses the rating to update the EF.

The interval (I) before the card should be reviewed again is calculated. If the rating is above a certain threshold, the interval increases, meaning the card will be scheduled for review later. If the rating is below this threshold, the interval is shorter.

The flashcard is then scheduled for review based on the calculated interval.

This integration of the SM-2 algorithm in Review Mode ensures that the review sessions are personalized. Flashcards that are harder for the user are reviewed more frequently, while easier cards are gradually spaced out. This optimizes the learning process by focusing on material that the user finds challenging, and not overburdening them with content they already know well.

Remember that Review Mode can only be conducted on flashcards that have a due review date. This ensures that the user is reviewing content at the optimal times based on their previous performance and the SM-2 algorithm.


## Unit testing

FlashcardApp includes a suite of unit tests to ensure the integrity and reliability of the codebase. These tests focus on the core functionality, including the manipulation and management of cards, decks, and collections, as well as the integration with JSON files for data persistence.

## App Presentation
![Windows Image](./presentation/windows.png)
![App1 GIF](./presentation/presentation.gif)
![App2 GIF](./presentation/presentation2.gif)
