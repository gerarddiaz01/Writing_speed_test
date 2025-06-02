# Typing Speed Test ⌨️

A simple but effective Typing Speed Test app built with Python and tkinter. It measures how fast a user types a given sentence, calculating words per minute (WPM), accuracy, and time spent.

As a student, this was my first experience creating a GUI from scratch — it helped me shift from print-based logic to event-driven programming and get comfortable with user input handling, widget interaction, and timed updates. That's why I wanted to include this project as part of my portfolio to showcase my learning journey.

---

## Learning Context 📚

This project was created in April 2025, during my 3rd month learning Python. It represents a milestone in shifting from scripting to building interactive user interfaces. It also marks my first attempt at real-time UI updates and dynamic state control.

---

## How to Run the Application 🛠️

1. **Clone the repository from Github**:
   - Also ensure you have Python 3.x installed on your system.

2. **Run the Script**:
   - Execute the script by running the following command in your terminal:
     ```
     python main.py
     ```

3. **Follow the GUI**:
   - Select a difficulty level and follow the instructions in the GUI to start the test.

---

## Technologies Used 🧰

- Python 3
- tkinter for GUI
- random module to select sentences
- Basic string manipulation and math functions

---

## How It Works 🚀

1. User selects a difficulty level (which sets sentence complexity).
2. A random sentence is shown in the GUI.
3. Once the user starts typing, a timer begins.
4. When the user presses Enter, the timer stops.
5. The program calculates and displays:
   - Time taken (seconds)
   - Words per minute (WPM)
   - Accuracy (% based on correct characters)
   - Total characters typed

---

## Features ✨

- Generates a random sentence from a predefined list.
- Tracks time taken, WPM, accuracy, and characters typed.
- Dynamic timer with real-time GUI update.
- Three difficulty levels: Easy, Medium, Hard.
- Visual feedback and results display after each test.

---

## Results 🧠
The application displays:
- Time taken to type the sentence.
- Accuracy percentage.
- Number of errors.

---

## Challenges Encountered and Solutions 🧩

### Challenge 1: Real-time Timer Without Freezing
I initially tried to use time.sleep() to manage timing — this froze the GUI. I faced the challenge of keeping the UI responsive without threading. I solved this by scheduling non-blocking updates using after().

### Challenge 2: Triggering the Timer Intelligently
I wanted the timer to begin as soon as the user starts typing. I solved this by binding a function to the <Key> event of the typing field, so the timer only activates on first key press.

### Challenge 4: Avoiding Clutter in Code
I experimented with function-driven modularity to reduce duplication and isolate responsibilities (e.g., separating result calculation from GUI state management).

### Challenge 4: Resetting the App Cleanly
I ensured all state (text, timer, results) is cleared when starting a new test. This required managing internal flags and GUI resets carefully.

---

## What I Learned 👨‍🎓

- I built comfort using tkinter widgets (Label, Entry, Button, Text, Frame).
- I learned how to schedule GUI updates without freezing using after().
- I practiced handling user events and building reactive interfaces.
- Instead of Googling every error, I leaned into AI-assisted exploration, testing answers quickly and understanding the why behind them.
- I refined my understanding of StringVar, widget state, and dynamic UI control.

---

## Possible Improvements 🛠️

- Add leaderboard with name input + top scores (WPM)
- Highlight typing errors live with color feedback
- Save session results to a CSV file
- Add sound effects or visual progress bar

---

## Conclusion 📝

This was a fantastic opportunity to explore GUI programming with `tkinter` and apply fundamental programming concepts like event handling, dynamic updates, and user interaction. By building a typing speed test application, I gained hands-on experience in creating an intuitive and interactive interface while solving real-world challenges such as error handling, timer updates, and dynamic sentence selection.

This project not only showcases my technical skills but also highlights my ability to learn new tools, debug effectively, and design user-friendly applications. It reflects my growth as a programmer and my commitment to continuous learning. Feel free to explore, use, and contribute to this project!
