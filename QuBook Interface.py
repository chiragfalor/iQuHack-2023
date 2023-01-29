from tkinter import *
import os
 
class QuBookInterface:

    QUESTION_LIST = [
        "How alive is Schrodinger's cat?",
        "Do you think Schrodinger should have a cat?",
        "Do you think Schrodinger should have opened the box?",
        "What is the likelihood that universe is deterministic?",
        "How much do you like cats?",
        "How much do you like quantum mechanics?",
    ]

    def __init__(self):
        pass

    def record_answers(self):
        name_info = self.name_q.get()
        file = open(name_info+".txt", "w")
        for answer in self.personality_answers:
            file.write(answer.get() + "\n")
        file.close()
    
        Label(main_screen, text="Answers recorded", fg="green", font=("calibri", 11)).pack()

    # for finding friends to entangle with
    '''
    def find_friend():
        friend = friend_verify.get()
        find_friend_entry.delete(0, END) #represents textbox to search for friend
    
        list_of_users = os.listdir()
        if friend in list_of_users:
            file1 = open(friend, "r")
            traits = file1.read().splitlines() #obtains all the traits
        else:
            user_not_found()

    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Uh-Oh")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found :(").pack()
        Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
    '''
    def main_account_screen(self):
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("QuBook")
        Label(text="Welcome to QuBook!", bg="#AAC79D", width="300", height="2", font=("Calibri", 20)).pack()
        Label(text="").pack()
        Label(text="Please answer these personality questions to quantum-ly generate your profile photo!", bg="#AAC79D", width="300", height="2", font=("Calibri", 13)).pack()


        self.name_q = StringVar()
        self.personality_answers = []
        for question in self.QUESTION_LIST:
            self.personality_answers.append(StringVar())

        Label(text="Please enter 1 for yes, 0 for no", bg="#AAC79D", width="300", height="2", font=("Calibri", 13)).pack()
    
        Label(main_screen, text="").pack()
        name_label = Label(main_screen, text="Enter your name: ")
        name_label.pack()
        Entry(main_screen, textvariable=self.name_q).pack()
        Label(main_screen, text="").pack()
        for i in range(len(self.QUESTION_LIST)):
            question, q_var = self.QUESTION_LIST[i], self.personality_answers[i]
            Label(main_screen, text=f"Q{i}: {question}").pack()
            Entry(main_screen, textvariable=q_var).pack()
        
        Label(main_screen, text="").pack()

        Button(main_screen, text="Done!", width=10, height=1, bg="#AAC79D", command = self.record_answers).pack()
        main_screen.mainloop()
 
Interface = QuBookInterface()
Interface.main_account_screen()