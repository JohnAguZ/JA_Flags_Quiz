from tkinter import *
from functools import partial
import random

import csv

all_flags = open("flag_codes.csv")
csv_all_flags = csv.reader(all_flags)

all_flags = {}

for row in csv_all_flags:
    all_flags[row[1]] = row[0]

flag_list = list(all_flags.items())     #
secret_flag = random.choice(flag_list)  #
flag_pic = (secret_flag[0])             # This code is what generates a random flag that is in the directory.
var_filename = (flag_pic+"-flag.gif")   #
print(secret_flag[0], secret_flag[1])   #
question = secret_flag[1]               # This saves the name of the country that is associated with the shown flag


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10, bg="#E6E6E6")
        self.start_frame.grid()

        # Set number of correct answers to 0...
        self.num_correct = IntVar()
        self.num_correct.set(0)

        # Setup answer to a string...
        self.Q_and_A = StringVar()
        self.Q_and_A.set(secret_flag[1])

        # Number of questions asked..
        self.questions_asked = IntVar()
        self.questions_asked.set(0)

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

        # Green Play Button
        self.play_button = Button(self.quiz_frame, text="Play",
                                  font=button_font, bg="#00994D", fg="white", width=10,
                                  command=self.to_quiz)
        self.play_button.grid(row=0, column=1, padx=10, pady=10)

        # Help Button
        self.how_to_play_button = Button(self.quiz_frame, text="How To Play",
                                         bg="#808080", fg="white", font=button_font,
                                         command=self.to_help1)
        self.how_to_play_button.grid(row=0, column=2, padx=10, pady=10)

    def to_quiz(self):
        answer = self.Q_and_A.get()
        correct = self.num_correct.get()
        q_asked = self.questions_asked.get()
        Quiz(self, answer, correct, q_asked)

    def to_help1(self):
        help_text1 = "Welcome to the International Flags Quiz. \n" \
                     "This quiz is aimed at testing your knowledge of different countries and their flags.\n \n" \
                     "When you click the 'Play' button, you wil " \
                     "\n " \
                     "\n \n " \

        Help1(self, help_text1)


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
    def __init__(self, partner, answer, correct, q_asked):

        background_color = "#00bbd4"
        photo = PhotoImage(file=var_filename)
        print("quiz photos", photo)

        var_new_photo = StringVar()
        var_new_photo.set("")

        

        # String Variable to hold correct answer
        self.valid_response = StringVar()
        self.valid_response.set(answer)
        # Variable to hold # of questions asked
        self.asked_questions = IntVar()
        self.asked_questions.set(q_asked)
        # Variable to hold # correct
        self.Q_correct = IntVar()
        self.Q_correct.set(correct)
        # List for holding statistics

        # GUI Setup
        self.quiz_box = Toplevel()
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)
        self.quiz_frame = Frame(self.quiz_box, bg=background_color)
        self.quiz_frame.grid()

        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Flags Quiz",
                                   font="Arial 24 bold", padx=10,
                                   pady=10, bg=background_color)
        self.heading_label.grid(row=0)

        # Flag Row
        self.flag_box = Frame(self.quiz_frame, bg=background_color)
        self.flag_box.grid(row=1, pady=10)

        # Flags
        self.flags_label = Label(self.flag_box, bg=background_color, image=photo, padx=10, pady=10)
        self.flags_label.photo = photo
        self.flags_label.grid(row=0)

        # Questionnaire
        self.Q_and_A = Label(self.quiz_frame, bg=background_color)
        self.Q_and_A.grid(row=2, pady=10)

        # Entry Box, Button and Error Label (Row 2)
        self.entry_error_frame = Frame(self.quiz_frame, width=200, bg=background_color)
        self.entry_error_frame.grid(row=3)

        self.response_entry = Entry(self.entry_error_frame,
                                    font="Arial 16 bold", width=20)
        self.response_entry.grid(row=0, column=1, padx=5)

        '''self.totals_label = Label(self.entry_error_frame,
                                  font="Arial 10 bold", wrap=175,
                                  justify=CENTER)
        self.totals_label.grid(row=1, columnspan=5, pady=5)'''

        self.question = Label(self.entry_error_frame,
                              bg=background_color, fg="maroon", text="What country has this flag?",
                              font="Arial 10 bold", wrap=175)
        self.question.grid(row=2, columnspan=5, pady=5)

        self.error_label = Label(self.entry_error_frame,
                                 bg=background_color, fg="maroon", text="",
                                 font="Arial 10 bold", wrap=175)
        self.error_label.grid(row=3, columnspan=5, pady=5)

        # Buttons go here...
        self.button_frame = Frame(self.quiz_frame, bg=background_color)
        self.button_frame.grid(row=4, pady=10)
        # Help Button
        self.help_button = Button(self.button_frame, text="Help",
                                  bg="#808080", fg="white", font="Arial 14 bold",
                                  command=self.to_quiz_help2)
        self.help_button.grid(row=0, column=1, padx=5, pady=5)

        self.submit_button = Button(self.button_frame, text="Submit",
                                    bg="#009900", fg="white", font="Arial 14 bold",
                                    command=self.check_response)
        self.submit_button.grid(row=0, column=2, padx=5, pady=5)

        self.next_button = Button(self.button_frame, text="Next",
                                  bg="#00AAFF", fg="white", font="Arial 14 bold",
                                  command=self.next_question)
        self.next_button.grid(row=0, column=3, padx=5, pady=5)

        self.next_button.config(state=DISABLED)



    def check_response(self):
        compare1 = self.valid_response.get()
        compare2 = self.response_entry.get()
        correct_num = self.Q_correct.get()
        q_asked = self.asked_questions.get()

        compare1 = compare1.lower()
        compare2 = compare2.lower()

        print("compare 1", compare1)
        print("compare 2", compare2)

        # Set error background colours (and assume that there are no errors at the start...)
        error_back = "#ffafaf"
        is_wrong = "no"

        # Change background colours to white (For testing purposes)...
        self.response_entry.config(bg="white")
        self.error_label.config(text="")

        running_total = q_asked
        total_correct = correct_num

        try:
            if compare1 != compare2:
                is_wrong = "yes"
                error_feedback = "This is wrong," \
                                 "try again!"
                running_total += 1
                total_correct += 0
            elif compare1 == compare2:
                is_wrong = "no"
                error_feedback1 = "Correct!"
                running_total += 1
                total_correct += 1
                self.submit_button.config(state=DISABLED)
                self.next_button.config(state=NORMAL)

        except SyntaxError:
            is_wrong = "yes"
            error_feedback = "Please enter a country name (No Numbers or Decimals)"

        if is_wrong == "yes":
            self.response_entry.config(bg=error_back)
            self.error_label.config(text=error_feedback, fg="#ff1100")

        elif is_wrong == "no":
            self.response_entry.config(bg="#42f572")
            self.error_label.config(text=error_feedback1, fg="#00a113")
            return

        # Add 1 to both the number of questions asked and if the user's first input was correct,
        # add one to the num correct.
        self.asked_questions.set(running_total)
        self.Q_correct.set(correct_num)

        if running_total == 10:
            root.destroy()
        else:
            self.next_question()

    def next_question(self):
        all_flags = open("flag_codes.csv")
        csv_all_flags = csv.reader(all_flags)

        all_flags = {}

        for row in csv_all_flags:
            all_flags[row[1]] = row[0]

        flag_list = list(all_flags.items())  #
        secret_flag = random.choice(flag_list)  #
        flag_pic = (secret_flag[0])  # This code is what generates a random flag that is in the directory.
        var_filename = (flag_pic + "-flag.gif")  #
        print("file name", var_filename)
        print(secret_flag[0], secret_flag[1])  #
        # question = secret_flag[1]

        photo = PhotoImage(file=var_filename)
        print(photo)
        self.flags_label.config(image=photo)


    def to_quit(self):
        root.destroy()

    def to_quiz_help2(self):
        help_text2 = "Welcome to the International Flags Quiz. \n" \
                     "This quiz is aimed at testing your knowledge of different countries and their flags.\n \n" \
                     "When you click the 'Play' button, you will be sent to a minor page showing you the layout " \
                     "of the quiz prior to you doing the quiz\n " \

        Help2(self, help_text2)


class Help2:
    def __init__(self, partner, help_text):
        background = "#a9ef99"

        # Disable help button
        partner.help_button.config(state=DISABLED)

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
