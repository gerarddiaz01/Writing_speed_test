import tkinter as tk
from tkinter import messagebox
from timeit import default_timer as timer
import random

# Sentence lists for different difficulties
easy_sentences = [
    "The cat sat on the mat.",
    "I love programming.",
    "Python is fun.",
    "Hello world!",
    "Typing is easy.",
    "This is a test.",
    "Keep it simple."
]

medium_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language!",
    "1234567890 is a sequence of numbers.",
    "Typing speed tests are fun and challenging.",
    "Can you type this sentence without any errors?",
    "Practice makes perfect.",
    "Coding is a valuable skill."
]

hard_sentences = [
    "El rápido zorro marrón salta sobre el perro perezoso.",
    "La programmation est une compétence précieuse.",
    "1234567890 est une séquence de chiffres.",
    "Les tests de vitesse de frappe sont amusants et stimulants.",
    "¿Puedes escribir esta oración sin errores?",
    "Typing in multiple languages is challenging.",
    "La práctica hace al maestro."
]

# Global variables
start_time = None
selected_sentence = None
timer_running = False
difficulty_sentences = []

# Function to start the test
def start_test():
    global start_time, selected_sentence, timer_running
    selected_sentence = random.choice(difficulty_sentences)
    sentence_label.config(text=selected_sentence)
    input_field.delete(0, tk.END)
    input_field.config(state='normal')
    input_field.focus_set()
    start_time = timer()
    timer_running = True
    update_timer()
    start_button.config(text="Restart", command=restart_test)

# Function to restart the test
def restart_test():
    start_test()

# Function to end the test
def end_test():
    global timer_running
    timer_running = False
    end_time = timer()
    typed_text = input_field.get()
    input_field.config(state='disabled')

    # Calculate time taken
    time_taken = end_time - start_time

    # Check accuracy
    if typed_text == selected_sentence:
        accuracy = 100
        errors = 0
    else:
        errors = sum(1 for a, b in zip(typed_text, selected_sentence) if a != b) + abs(len(typed_text) - len(selected_sentence))
        accuracy = max(0, 100 - (errors / len(selected_sentence) * 100))

    # Highlight errors
    highlighted_errors = ""
    for a, b in zip(typed_text, selected_sentence):
        if a == b:
            highlighted_errors += a
        else:
            highlighted_errors += f"[{a}]"
    highlighted_errors += typed_text[len(selected_sentence):]  # Add extra characters if typed_text is longer

    # Show results
    messagebox.showinfo(
        "Results",
        f"Time: {time_taken:.2f} seconds\n"
        f"Accuracy: {accuracy:.2f}%\n"
        f"Errors: {errors}\n\n"
        f"Original Sentence:\n{selected_sentence}\n\n"
        f"Your Input:\n{highlighted_errors}"
    )

# Function to update the timer label
def update_timer():
    if timer_running:
        elapsed_time = timer() - start_time
        timer_label.config(text=f"Time: {elapsed_time:.1f} seconds")
        root.after(1000, update_timer)

# Function to set difficulty
def set_difficulty(level):
    global difficulty_sentences
    if level == "easy":
        difficulty_sentences = easy_sentences
    elif level == "medium":
        difficulty_sentences = medium_sentences
    elif level == "hard":
        difficulty_sentences = hard_sentences
        messagebox.showwarning("Hard Difficulty", "Warning: Sentences may include other languages!")
    difficulty_frame.pack_forget()
    main_frame.pack()

# Create the main window
root = tk.Tk()
root.title("Typing Speed Test")

# Difficulty selection frame
difficulty_frame = tk.Frame(root)
tk.Label(difficulty_frame, text="Select Difficulty", font=("Arial", 16)).pack(pady=10)
tk.Button(difficulty_frame, text="Easy", command=lambda: set_difficulty("easy")).pack(pady=5)
tk.Button(difficulty_frame, text="Medium", command=lambda: set_difficulty("medium")).pack(pady=5)
tk.Button(difficulty_frame, text="Hard", command=lambda: set_difficulty("hard")).pack(pady=5)
difficulty_frame.pack()

# Main frame (hidden until difficulty is selected)
main_frame = tk.Frame(root)
sentence_label = tk.Label(main_frame, text="Press Start to begin the test", wraplength=400, font=("Arial", 14))
sentence_label.pack(pady=20)
input_field = tk.Entry(main_frame, font=("Arial", 14), state='disabled', width=50)
input_field.pack(pady=10)
timer_label = tk.Label(main_frame, text="Time: 0.0 seconds", font=("Arial", 12))
timer_label.pack(pady=5)
start_button = tk.Button(main_frame, text="Start", command=start_test)
start_button.pack(pady=5)
end_button = tk.Button(main_frame, text="End", command=end_test)
end_button.pack(pady=5)

# Run the application
root.mainloop()