from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")


def play(player_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    name = name_entry.get() or "Player"

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = f"{name} Wins!"
    else:
        result = "Computer Wins!"

    choices_label.config(text=f"{name}: {player_choice} | Computer: {computer_choice}")
    outcome_label.config(text=result)


Label(root, text="Enter your name:", font=("Arial", 10)).pack(pady=5)
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Choose your move:", font=("Arial", 12, "bold")).pack(pady=20)

btn_frame = Frame(root)
btn_frame.pack()

Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

choices_label = Label(root, text="Waiting for your move...", font=("Arial", 10), fg="gray")
choices_label.pack(pady=15)

outcome_label = Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
outcome_label.pack()

root.mainloop()
