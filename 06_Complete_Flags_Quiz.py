from tkinter import *
from functools import partial
import random

import csv


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10, bg="#E6E6E6")
        self.start_frame.grid()

        # Set number of correct answers to 0...
        self.num_correct = IntVar()
        self.num_correct.set(0)

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
        correct_num = self.num_correct.get()

        Quiz(self, correct_num)

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
    def __init__(self, partner, correct_ans, ):

        all_flags = open("flag_codes.csv")
        csv_all_flags = csv.reader(all_flags)

        all_flags = {}

        for row in csv_all_flags:
            all_flags[row[1]] = row[0]

        flag_list = list(all_flags.items())

        background_color = "#00bbd4"

        photo = PhotoImage(file="filler.gif")

        # String Variable to hold correct answer
        self.valid_response = StringVar()
        self.valid_response.set(correct_ans)

        # Variable to hold # of questions asked
        self.asked_questions = IntVar()
        self.asked_questions.set(0)
        q_asked = self.asked_questions.get()

        # Variable to hold # correct
        self.q_correct = IntVar()
        self.q_correct.set(0)
        num_correct = self.q_correct.get()

        # List for holding statistics
        self.game_stats_list = [q_asked, num_correct]

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

        # Entry Box, Button and Error Label (Row 2)
        self.entry_error_frame = Frame(self.quiz_frame, width=200, bg=background_color)
        self.entry_error_frame.grid(row=2)

        self.response_entry = Entry(self.entry_error_frame,
                                    font="Arial 16 bold", width=20)
        self.response_entry.grid(row=0, column=1, padx=5)

        self.error_label = Label(self.entry_error_frame,
                                 bg=background_color, fg="maroon", text="What country has this flag?",
                                 font="Arial 10 bold", wrap=175)
        self.error_label.grid(row=3, columnspan=5, pady=5)

        # Stats label
        self.stats_frame = Frame(self.quiz_frame, bg=background_color)
        self.stats_frame.grid(row=4)

        self.stats_label = Label(self.stats_frame, text="Stats...", bg=background_color)
        self.stats_label.grid(row=0)

        # Disable the entry
        self.response_entry.config(state=DISABLED)

        # Buttons go here...
        self.button_frame = Frame(self.quiz_frame, bg=background_color)
        self.button_frame.grid(row=5, pady=10)

        # Help Button
        self.help_button = Button(self.button_frame, text="Help",
                                  bg="#808080", fg="white", font="Arial 14 bold", width=5,
                                  command=self.to_quiz_help2)
        self.help_button.grid(row=0, column=1, padx=5, pady=5)

        self.submit_button = Button(self.button_frame, text="Submit",
                                    bg="#009900", fg="white", font="Arial 14 bold", width=6,
                                    command=self.check_response)
        self.submit_button.focus()
        self.submit_button.bind('<Return>', lambda e: self.check_response())
        self.submit_button.grid(row=0, column=2, padx=5, pady=5)

        self.next_button = Button(self.button_frame, text="Next",
                                  bg="#00AAFF", fg="white", font="Arial 14 bold", width=5,
                                  command=lambda: self.next_question(flag_list, correct_ans, q_asked,
                                                                     num_correct))
        self.next_button.grid(row=0, column=3, padx=5, pady=5)

        self.results_button = Button(self.button_frame, text="To Results",
                                     bg="#003366", fg="white", font="Arial 14 bold",
                                     command=lambda: self.to_game_results(self.game_stats_list))
        self.results_button.grid(row=0, column=4, padx=5, pady=5)
        self.submit_button.config(state=DISABLED)
        self.results_button.config(state=DISABLED)

    def to_game_results(self, game_stats_list):

        Game_Results(self, game_stats_list)

    def check_response(self):
        self.next_button.config(state=DISABLED)
        compare1 = self.valid_response.get()
        compare2 = self.response_entry.get()

        compare1 = compare1.lower()
        compare2 = compare2.lower()

        print("compare 1", compare1)
        print("compare 2", compare2)
        # Set error background colours (and assume that there are no errors at the start...)
        error_back = "#ffafaf"
        is_wrong = "no"

        # Change background colours to white (For testing purposes)...
        self.response_entry.config(bg="white")
        self.error_label.config(text="What country has this flag?")

        # Get the num correct
        num_correct = self.q_correct.get()

        # Get number of questions asked, add one and reset
        q_asked = self.asked_questions.get()

        try:

            if compare1 != compare2:

                is_wrong = "yes"
                error_feedback = "This is wrong," \
                                 "try again!"

                # Adding one to number correct and setting it
                q_asked += 1
                self.asked_questions.set(q_asked)

                self.submit_button.config(state=DISABLED)
                self.next_button.config(state=NORMAL)
            elif compare1 == compare2:

                is_wrong = "no"
                error_feedback1 = "Correct!"

                # Adding one to number correct and setting it
                q_asked += 1
                self.asked_questions.set(q_asked)

                # Adding one to number correct and setting it
                num_correct += 1
                self.q_correct.set(num_correct)

                self.submit_button.config(state=DISABLED)
                self.next_button.config(state=NORMAL)

        except SyntaxError:
            is_wrong = "yes"
            error_feedback = "Please enter a country name (No Numbers or Decimals)"

        if is_wrong == "yes":
            self.response_entry.config(bg=error_back)
            self.error_label.config(text=error_feedback, fg="#ff1100")

        else:
            self.response_entry.config(bg="#42f572")
            self.error_label.config(text=error_feedback1, fg="#00a113")
            # Add 1 to both the number of questions asked and if the user's first input was correct,
            # add one to the num correct.

    def next_question(self, flag_list, correct_ans, q_asked, num_correct):

        num_correct = self.q_correct.get()
        q_asked = self.asked_questions.get()

        stat1 = q_asked
        stat2 = num_correct

        # Stats statement
        stats_statement = "Questions Asked: {} \n" \
                          "Questions Correct: {}".format(q_asked, num_correct)
        # Edit the stats label
        self.stats_label.configure(text=stats_statement)

        # Put data into the list
        self.game_stats_list[0] = stat1
        self.game_stats_list[1] = stat2

        # Enable the response entry
        self.response_entry.config(state=NORMAL)
        # Keep the results button disabled
        self.results_button.config(state=DISABLED)

        # choose random flag
        secret_flag = random.choice(flag_list)

        # Reset the response entry
        self.response_entry.config(bg="white")
        self.response_entry.delete(0, END)

        # Reset question
        self.error_label.config(text="What country has this flag?", fg="maroon")
        # Get filename...
        flag_pic = (secret_flag[0])
        var_filename = "{}-flag.gif".format(flag_pic)

        print("file name", var_filename)
        print(secret_flag[0], secret_flag[1])
        # question = secret_flag[1]

        correct_answer = secret_flag[1]
        self.valid_response.set(correct_answer)

        photo = PhotoImage(file=var_filename)
        print(photo)
        self.flags_label.config(image=photo)

        # Ensures image actually appears!
        self.flags_label.photo = photo

        self.submit_button.config(state=NORMAL)
        self.next_button.config(state=DISABLED)

        # Results page
        num_asked = self.asked_questions.get()

        # Ensures 10 questions have been asked.
        if num_asked == 10:
            self.response_entry.destroy()
            self.flag_box.destroy()
            self.flags_label.destroy()
            self.submit_button.config(state=DISABLED)
            self.next_button.config(state=DISABLED)
            self.stats_label.configure(fg="#00bbd4")
            self.results_button.config(state=NORMAL)

            finish_statement = "Congratulations!! \n" \
                               "You have finished the quiz!\n" \
                               "Click the 'RESULTS' Button to look at your results"

            self.error_label.configure(bg="#00bbd4", font="Arial 15 bold", text=finish_statement, padx=5)

    def to_quit(self):
        root.destroy()

    def to_quiz_help2(self):
        help_text2 = "Welcome to the International Flags Quiz. \n" \
                     "This quiz will ask you 10 questions and 10 flags will appear.\n \n" \
                     "You can check your answer by clicking on the 'Submit' button" \
                     "and when you either get the question right or wrong, the program will tell you.\n " \

        Help_2(self, help_text2)


class Help_2:
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


class Game_Results:
    def __init__(self, partner, game_stats):
        print("game_stats", game_stats)
        # Disable Help Button
        partner.results_button.config(state=DISABLED)

        var_num_asked = game_stats[0]

        num_correct = game_stats[1]

        game_stats = [var_num_asked, num_correct]

        heading = "Arial 12 bold"
        content = "Arial 12"
        background = "#a9ef99"

        # Sets up child window
        self.stats_box = Toplevel()

        # If user press the cross at the top, closes child window and 'releases' help button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box, bg=background, width=300)
        self.stats_frame.grid()

        # Set up Help heading (Row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                         font="arial 19 bold", bg=background)
        self.stats_heading_label.grid(row=0)

        # To export <instructions> (row 1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are your Game Statistics. "
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "round that you played ", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10, pady=10, bg=background)
        self.export_instructions.grid(row=1)

        # Stats Frame (Row 2.0)
        self.details_frame = Frame(self.stats_frame, bg=background)
        self.details_frame.grid(row=2)

        # Calculate percentage
        calc1 = var_num_asked
        calc2 = num_correct

        print("calc1", calc1)
        print("calc2", calc2)

        raw = calc2 / float(10)
        print(raw)
        percent = raw * 100
        print(percent)

        self.correct_num_label = Label(self.details_frame, font=content, bg=background,
                                       text="Total Correct: {}/10".format(calc2))
        self.correct_num_label.grid(row=0, column=0, padx=0)

        "/n " \

        self.total_questions_label = Label(self.details_frame, font=content, bg=background,
                                           text="Asked Questions: {}".format(calc1))
        self.total_questions_label.grid(row=1, column=0, padx=0)

        "/n " \

        self.percentage_label = Label(self.details_frame, font=content, bg=background,
                                      text="You got {}% of the questions correct".format(percent))
        self.percentage_label.grid(row=2, column=0, padx=0)

        # Buttons go here
        self.buttons_frame = Frame(self.stats_frame, bg=background)
        self.buttons_frame.grid(row=3)

        # Help Button
        self.help_button = Button(self.buttons_frame, text="Help",
                                  bg="#808080", fg="white", font="Arial 10 bold", width=10,
                                  command=self.to_quiz_help3)
        self.help_button.grid(row=0, column=0, pady=5, padx=5)

        # Dismiss button (Row 5.0)
        self.dismiss_btn = Button(self.buttons_frame, text="Dismiss",
                                  bg="orange", font="Arial 10 bold", width=10,
                                  command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=0, column=1, pady=5, padx=5)

        # Export Button (Row 5.1)
        self.export_button = Button(self.buttons_frame,
                                    text="Export",
                                    font="Arial 10 bold", bg="light blue", width=10,
                                    command=lambda: self.export(game_stats))
        self.export_button.grid(row=0, column=2, pady=5, padx=5)

    def close_stats(self, partner):
        # Put history button back to normal...
        partner.results_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, game_stats):

        Export(self, game_stats)

    def to_quiz_help3(self):
        help_text3 = "Welcome to the International Flags Quiz Results Page! \n" \
                     "This page tell you your grand stats.\n \n" \
                     "You can export your results in a .txt file via the 'Export' button. " \
                     "To redo the quiz again and try for a higher score, re-run the program\n " \

        Help3(self, help_text3)


class Help3:
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


class Export:
    def __init__(self, partner, game_stats):

        background = "#a9ef99"  # Pale Green

        # Disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (i.e: Export Box)
        self.export_box = Toplevel()

        # If users press the cross at the top, closes export and
        # 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up Export heading(Row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="Arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export Instructions(Row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "and press the Save  "
                                                         "button to save your"
                                                         "results to a text file",
                                 justify=LEFT, width=40,
                                 bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning Text (Row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists,  "
                                                         "its contents will "
                                                         "be replaced with "
                                                         "your current results "
                                                         , wrap=250,
                                 justify=LEFT, width=40, bg=background,
                                 font="arial 10 italic", fg="maroon",
                                 padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (Row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels(Initially blank, Row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame, bg=background)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (Row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", width=5,
                                  command=lambda: self.save_stats(partner, game_stats))
        self.save_button.grid(row=0, column=0, padx=5)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", width=5,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1, padx=5)

    def save_stats(self, partner, game_stats):
        # Regular expression to check filename is valid

        print(game_stats)

        global problem
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == "":
                problem = "(No spaces allowed)"

            else:
                problem = ("(no {}'s allowed".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "Can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close the dialogue
            # add .text suffix
            filename = filename + ".txt"

            # Create file to hold data
            f = open(filename, "w+")

            # Add new line at the end of each item
            for round in game_stats:

                f.write(round + "\n")

            # Heading for rounds
            f.write("\nRound Details\n\n")

            # Close the file
            f.close()

            # Close the dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put history button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Flags Quiz")
    start_program = Start(root)
    root.mainloop()
