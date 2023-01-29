from tkinter import *
import os
 
def record_answers():
 
    q1_info = q1.get()
    q2_info = q2.get()
    q3_info = q3.get()
    q4_info = q4.get()
    q5_info = q5.get()
    q6_info = q6.get()
    q7_info = q7.get()
 
    file = open(q1_info, "w")
    #file.write(q1_info + "\n")
    file.write(q2_info + "\n")
    file.write(q3_info + "\n")
    file.write(q4_info + "\n")
    file.write(q5_info + "\n")
    file.write(q6_info + "\n")
    file.write(q7_info)
    file.close()
 
    q1_entry.delete(0, END)
    q2_entry.delete(0, END)
    q3_entry.delete(0, END)
    q4_entry.delete(0, END)
    q5_entry.delete(0, END)
    q6_entry.delete(0, END)
    q7_entry.delete(0, END)
 
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
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("QuBook")
    Label(text="Welcome to QuBook!", bg="#AAC79D", width="300", height="2", font=("Calibri", 20)).pack()
    Label(text="").pack()
    Label(text="Please answer these personality questions to quantum-ly generate your profile photo!", bg="#AAC79D", width="300", height="2", font=("Calibri", 13)).pack()
 
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q1_entry
    global q2_entry
    global q3_entry
    global q4_entry
    global q5_entry
    global q6_entry
    global q7_entry
    q1 = StringVar()
    q2 = StringVar()
    q3 = StringVar()
    q4 = StringVar()
    q5 = StringVar()
    q6 = StringVar()
    q7 = StringVar()

    Label(text="Please enter 1 for yes, 0 for no", bg="#AAC79D", width="300", height="2", font=("Calibri", 13)).pack()
 
    Label(main_screen, text="").pack()
    q1_lable = Label(main_screen, text="Q1: Enter your name: ")
    q1_lable.pack()
    q1_entry = Entry(main_screen, textvariable=q1)
    q1_entry.pack()
    q2_lable = Label(main_screen, text="Q2: Do you think Schrodinger's cat is alive or dead?")
    q2_lable.pack()
    q2_entry = Entry(main_screen, textvariable=q2)
    q2_entry.pack()
    q3_lable = Label(main_screen, text="Q3: Do you think Schrodinger should have a cat?")
    q3_lable.pack()
    q3_entry = Entry(main_screen, textvariable=q3)
    q3_entry.pack()
    q4_lable = Label(main_screen, text="Q4: Do you think Schrodinger should have opened the box?")
    q4_lable.pack()
    q4_entry = Entry(main_screen, textvariable=q4)
    q4_entry.pack()
    q5_lable = Label(main_screen, text="Q5: What is the likelihood that universe is deterministic?")
    q5_lable.pack()
    q5_entry = Entry(main_screen, textvariable=q5)
    q5_entry.pack()
    q6_lable = Label(main_screen, text="Q6: How much do you like cats?")
    q6_lable.pack()
    q6_entry = Entry(main_screen, textvariable=q6)
    q6_entry.pack()
    q7_lable = Label(main_screen, text="Q7: Do you like quantum mechanics?")
    q7_lable.pack()
    q7_entry = Entry(main_screen, textvariable=q7)
    q7_entry.pack()

    
    Label(main_screen, text="").pack()

    Button(main_screen, text="Done!", width=10, height=1, bg="#AAC79D", command = record_answers).pack()
    main_screen.mainloop()
 
main_account_screen()