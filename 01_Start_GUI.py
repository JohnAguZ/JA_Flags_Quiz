from tkinter import *
from functools import partial
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10, bg="#E6E6E6")
        self.start_frame.grid()

        # Flags Heading (Row 0)
        self.flags_quiz_label = Label(self.start_frame, text="Country Flags Quiz",
                                       font="Arial 19 bold", bg="#E6E6E6")
        self.flags_quiz_label.grid(row=0)

        # Initial Instructions (Row 1)
        self.quiz_instructions = Label(self.start_frame, font="Arial 10 italic",
                                       text="Welcome to the International Flags Quiz \n \n "
                                            "To start the quiz click the 'Play' button below. "
                                            "If you want a more detailed explanation of the quiz, "
                                            "click the 'How To Play' button below. \n \n "
                                            "Have fun and good luck! ",
                                       wrap=275, justify=CENTER, padx=10, pady=10, bg="#E6E6E6")
        self.quiz_instructions.grid(row=1)


        # Play Button Frame (Note: Not Youtube) (Row 2)
        self.quiz_frame = Frame(self.start_frame, bg="#E6E6E6")
        self.quiz_frame.grid(row=2)

        # Buttons go here...
        button_font = "Arial 12 bold"

        # Green High Stakes Button
        self.play_button = Button(self.quiz_frame, text="Play",
                                         font=button_font, bg="#00994D",fg="white", width=10)
        self.play_button.grid(row=0, column=1, padx=10, pady=10)

        # Help Button
        self.how_to_play_button = Button(self.quiz_frame, text="How To Play",
                                  bg="#808080", fg="white", font=button_font)
        self.how_to_play_button.grid(row=0, column=2, padx=10, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Flags Quiz")
    start_program = Start(root)
    root.mainloop()