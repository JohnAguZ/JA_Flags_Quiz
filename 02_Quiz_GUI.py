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
                                  font=button_font, bg="#00994D",fg="white", width=10,
                                  command=lambda: self.to_quiz())
        self.play_button.grid(row=0, column=1, padx=10, pady=10)

        # Help Button
        self.how_to_play_button = Button(self.quiz_frame, text="How To Play",
                                         bg="#808080", fg="white", font=button_font,
                                         command=lambda: self.to_help1())
        self.how_to_play_button.grid(row=0, column=2, padx=10, pady=10)

    def to_help1(self):
        help_text1 = "Welcome to the International Flags Quiz. \n" \
                     "This quiz is aimed at testing your knowledge of different countries and their flags.\n \n" \
                     "When you click the 'Play' button, you wil " \
                     "\n " \
                     "\n \n " \
                     "" \
                     "\n" \
                     "" \
                     "\n" \
                     "\n \n" \
                     "\n" \
                     " \n" \
                     " \n \n" \
                     "" \
                     " " \
                     " " \
                     ""

        Help1(self,help_text1)

    def to_quiz(self):
        Quiz()

class Help1:
    def __init__(self, partner, help_text):
        background = "#a9ef99"

        # Disable help button
        partner.how_to_play_button.config(state=DISABLED)

        # Sets up child window (ie: Help Box)
        self.help_box = Toplevel()

        # If users press cross at the top, close help and 'release' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.help_frame, text="The Help Page",
                                 font="Arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help for Start Class (Label,Row 1)
        self.help_text = Label(self.help_frame,
                               text=help_text, wrap=250,
                               font="arial 10 italic",
                               justify=LEFT, width=40, bg=background, fg="maroon",
                               padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (Row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="Arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
            # Put history button back to normal...
            partner.how_to_play_button.config(state=NORMAL)
            self.help_box.destroy()



class Quiz:
    def __init__(self):
        background_color = "#E3E3E3"
        box_back = "#999871"
        box_text = "Arial 10"
        box_width = 20

        # List for holding statistics


        # GUI Setup
        self.quiz_box = Toplevel()
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)
        self.quiz_frame = Frame(self.quiz_box, bg=background_color)
        self.quiz_frame.grid()


        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Heading",
                                   font="Arial 24 bold", padx=10,
                                   pady=10, bg=background_color)
        self.heading_label.grid(row=0)

        # Flag Row
        self.flag_box = Frame(self.quiz_frame, bg=background_color)
        self.flag_box.grid(row=1, pady=10)

        # Flags
        self.flags_label = Label(self.flag_box, text="Flags will show up here", font=box_text,
                                 bg=box_back, width=box_width, padx=10, pady=10)
        self.flags_label.grid(row=0, column=2)


        # Entry Box, Button and Error Label (Row 2)
        self.entry_error_frame = Frame(self.quiz_frame, width=200, bg=background_color)
        self.entry_error_frame.grid(row=3)

        self.response_entry = Entry(self.entry_error_frame,
                                        font="Arial 16 bold", width=20)
        self.response_entry.grid(row=0, column=5, padx=5)

        self.error_label = Label(self.entry_error_frame,
                                        bg=background_color, fg="maroon", text="",
                                        font="Arial 10 bold", wrap=175,
                                        justify=CENTER)
        self.error_label.grid(row=0, columnspan=5, pady=5)

        # Buttons go here...
        self.button_frame = Frame(self.quiz_frame, bg=background_color)
        self.button_frame.grid(row=4, pady=10)
        # Help Button
        self.how_to_play_button = Button(self.button_frame, text="Help",
                                         bg="#808080", fg="white", font="Arial 14 bold",
                                         command=lambda: self.to_quiz_help2)
        self.how_to_play_button.grid(row=0, column=1, padx=5, pady=5)

        self.submit_and_next_button = Button(self.button_frame, text="Submit",
                                         bg="#009900", fg="white", font="Arial 14 bold",
                                         command=lambda: self.check_response(1))
        self.submit_and_next_button.grid(row=0, column=2, padx=5, pady=5)

    def to_quit(self):
        root.destroy()

    def check_response(self, response):
        starting_balance = self.response_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # Check the user's input
        country_list = []


    def to_quiz_help2(self):
        help_text2 = "Welcome to the International Flags Quiz. \n" \
                     "This quiz is aimed at testing your knowledge of different countries and their flags.\n \n" \
                     "When you click the 'Play' button, you will be sent to a minor page showing you the layout " \
                     "of the quiz prior to you doing the quiz\n " \
                     "\n \n " \
                     "" \
                     "\n" \
                     "" \
                     "\n" \
                     "\n \n" \
                     "\n" \
                     " \n" \
                     " \n \n" \
                     "" \
                     " " \
                     " " \
                     ""
        Help2(self,help_text2)


class Help2:
    def __init__(self, partner, help_text):
        background = "#a9ef99"

        # Disable help button
        partner.how_to_play_button.config(state=DISABLED)

        # Sets up child window (ie: Help Box)
        self.help_box = Toplevel()

                # If users press cross at the top, close help and 'release' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

                # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

                # Set up history heading (row 0)
        self.how_heading = Label(self.help_frame, text="The Help Page",
                                         font="Arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

                # Help for Start Class (Label,Row 1)
        self.help_text = Label(self.help_frame,
                                       text=help_text, wrap=250,
                                       font="arial 10 italic",
                                       justify=LEFT, width=40, bg=background, fg="maroon",
                                       padx=10, pady=10)
        self.help_text.grid(row=1)

                # Dismiss button (Row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                          width=10, bg="orange", font="Arial 10 bold",
                                          command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
                # Put history button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()







# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Flags Quiz")
    start_program = Start(root)
    root.mainloop()