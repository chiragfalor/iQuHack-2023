from tkinter import *
from PIL import ImageTk, Image
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
        file = open(f"database/{name_info}.txt", "w")
        for answer in self.personality_answers:
            file.write(answer.get() + "\n")
        file.close()
    
        Label(self.input_screen, text="Answers recorded", fg="green", font=("calibri", 11)).pack()
        self.input_screen.destroy()

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
    def input_account_screen(self):
        self.input_screen = Tk()
        self.input_screen.geometry("300x250")
        self.input_screen.title("QuBook")
        Label(text="Welcome to QuBook!", bg="#AAC79D", width="300", height="2", font=("Calibri", 20)).pack()
        Label(text="").pack()
        Label(text="Please answer these personality questions to quantum-ly generate your profile photo!", bg="#AAC79D", width="300", height="2", font=("Calibri", 13)).pack()


        self.name_q = StringVar()
        self.personality_answers = []
        for question in self.QUESTION_LIST:
            self.personality_answers.append(StringVar())

        Label(text="Please enter 1 for yes, 0 for no", bg="#AAC79D", width="300", height="2", font=("Calibri", 13)).pack()
    
        Label(self.input_screen, text="").pack()
        name_label = Label(self.input_screen, text="Enter your name: ")
        name_label.pack()
        Entry(self.input_screen, textvariable=self.name_q).pack()
        Label(self.input_screen, text="").pack()
        for i in range(len(self.QUESTION_LIST)):
            question, q_var = self.QUESTION_LIST[i], self.personality_answers[i]
            Label(self.input_screen, text=f"Q{i}: {question}").pack()
            Entry(self.input_screen, textvariable=q_var).pack()
        
        Label(self.input_screen, text="").pack()

        Button(self.input_screen, text="Done!", width=10, height=1, bg="#AAC79D", command = self.record_answers).pack()

        self.input_screen.mainloop()

    def display_profile_screen(self):
        self.dp_screen = Tk()
        self.dp_screen.geometry("512x1024")
        self.dp_screen.title("QuBook")
        Label(text="Welcome to QuBook!", bg="#AAC79D", width="300", height="2", font=("Calibri", 20)).pack()
        Label(text="").pack()
        Label(text="Here are your friends' profile photos!", bg="#AAC79D", width="300", height="2", font=("Calibri", 13)).pack()
        images = os.listdir("pfps")
        print(images)
        names = ['Chirag', 'Berkin', 'Yiming', 'Tung']
        Label(text="    ", width="300", height="1", font=("Calibri", 10)).pack()
        for i, image in enumerate(images):
            img = Image.open(f"pfps/{image}")
            img = img.resize((120, 120), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img, master=self.dp_screen, width=64, height=64)
            label1 = Label(image=img, anchor=CENTER)
            label1.image = img
            label1.pack()
            Label(text=names[i], width="300", height="2", font=("Calibri", 12)).pack()
            
        self.dp_screen.mainloop()
        

        
if __name__ == "__main__":
    Interface = QuBookInterface()
    Interface.display_profile_screen()