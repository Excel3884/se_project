from fileinput import filename
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from mysql.connector import Error
import  dbConnection

#set up filePath for using it later
global filePath
filePath = str(filename)

def helpWindow():
    # dhmiourgia parathyrou help
    help_window = Toplevel()
    help_window.title("Help")
    help_window.iconbitmap("Images/budget_icon.ico")
    help_window.configure(background="#4a47a3")

    #dropdown menu options
    options =[
        "Γενικές ερωτήσεις",
        "Τεχνικό πρόβλημα"
    ]
    
    clicked = StringVar()
    clicked.set( options[0] )
    
    #function to open the select a file dialog
    def selectFile():
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        global filename
        filename = filedialog.askopenfilename(
            title="Επισυνάψτε ένα αρχείο καταγραφής του προβλήματος", 
            initialdir='/', 
            filetypes=filetypes)
        if filename == "":
            openFileBtn.config(text="Επισυνάψτε ένα αρχείο καταγραφής του προβλήματος")
        else:
            openFileBtn.config(text=filename)

    #function for the move on button
    def openForm(event):
        if clicked.get() == options[0]:
            #put everything on grid
            firstNameLabel.grid(row=1, column=1, sticky="e")
            firstNameText.grid(row=1, column=2, sticky="w")
            lastNameLabel.grid(row=2, column=1,sticky="e")
            lastNameText.grid(row=2, column=2,sticky="w")
            usernameLabel.grid(row=3, column=1, sticky="e")
            usernameText.grid(row=3, column=2, sticky="w")
            inputLabel.grid(row=4, column=1, columnspan=2, padx=10, pady=(10, 0))
            inputText.grid(row=5, column=1, columnspan=2, padx=10, pady=(0 ,10))
            openFileBtn.grid_forget()
            
            #change the inputLabel text
            inputLabel.config(text="Γράψτε μία ερώτηση για το κόστος λογισμικού")
        else:
            #put everything on grid
            firstNameLabel.grid(row=1, column=1, sticky="e")
            firstNameText.grid(row=1, column=2, sticky="w")
            lastNameLabel.grid(row=2, column=1,sticky="e")
            lastNameText.grid(row=2, column=2,sticky="w")
            usernameLabel.grid(row=3, column=1, sticky="e")
            usernameText.grid(row=3, column=2, sticky="w")
            inputLabel.grid(row=4, column=1, columnspan=2, padx=10, pady=(10, 0))
            inputText.grid(row=5, column=1, columnspan=2, padx=10, pady=(0 ,10))
            openFileBtn.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

            #change the inputLabel text
            inputLabel.config(text="Περιγράψτε το Τεχνικό Πρόβλημα")

    #make label and text input for firstname, lastname and username
    global firstNameLabel
    firstNameLabel = Label(help_window, text="First Name", background="#4a47a3", font=("Calibri bold", 9))
    global firstNameText 
    firstNameText = Entry(help_window)
    global lastNameLabel
    lastNameLabel = Label(help_window, text="Last Name", background="#4a47a3", font=("Calibri bold", 9))
    global lastNameText
    lastNameText = Entry(help_window)

    #make label and text input for username
    global usernameLabel 
    usernameLabel = Label(help_window, text="Username", background="#4a47a3", font=("Calibri bold", 9))
    global usernameText
    usernameText = Entry(help_window)

    #make label and text input for the question
    global inputLabel 
    inputLabel = Label(help_window, text="Γράψτε όποια ερώτηση μπορεί να έχετε", background="#4a47a3", font=("Calibri bold", 9))
    global inputText
    inputText = Text(help_window, width=50, height=10)

    #make the open file button
    global openFileBtn
    openFileBtn = Button(help_window, text="Επισυνάψτε ένα αρχείο καταγραφής του προβλήματος", command=selectFile)

    #make the dropdown menu
    dropdown = OptionMenu( help_window, clicked, *options, command=openForm )
    dropdown.config( font =("Calibri bold", 16), background="#4a47a3", activebackground="#6664ef", highlightthickness=0)
    dropdown.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    #function 
    def submission():
        #put all data in a dictionary
        if clicked.get() == options[0]:
            info = {
                'firstName' : firstNameText.get(),
                'lastName' : lastNameText.get(),
                'username' : usernameText.get(),
                'textInput' : inputText.get("1.0", END)
            }
            #check for user mistakes
            if info["firstName"] == "" or info["lastName"] == "" or info["username"] == "" or info["textInput"] == "":
                errorLabel.grid(row=8, column=1, columnspan=2, padx=10, pady=(0, 10))
            else:
                #put data in db
                try:
                    conn = dbConnection.conn
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO `help` (`firstname`, `lastname`, `username`, `text`, `type`) VALUES (%s, %s, %s, %s, %s)", 
                        (info["firstName"], info["lastName"], info["username"], info["textInput"], "question"))
                    conn.commit()
                    showinfo(title= "Επιτυχής Καταχώρηση Αιτήματος", 
                        message= "Το αίτημά σας έχει καταχωρηθεί στο σύστημα, στοιχεία αιτήματος:" + "\n" 
                            + "First Name: " + info["firstName"] + "\n" 
                            + "Last Name: " + info["lastName"] + "\n" 
                            + "Username: " + info["username"] + "\n" 
                            + "Question: " + info["textInput"])
                except Error as e:
                    showinfo(title="Πρόβλημα Καταχώρηση Αιτήματος", 
                        message="Το αίτημά σας δεν μπόρεσε να καταχωρηθεί στο σύστημα, παρακαλώ προσπαθήστε αργότερα!" + 
                            "Κωδικός σφάλματος: " + e)
        else:
            #put all data in a dictionary
            info = {
                "firstName" : firstNameText.get(),
                "lastName" : lastNameText.get(),
                "username" : usernameText.get(),
                "textInput" : inputText.get("1.0",END),
                "file" : filename
            }
            print(info["file"])
            #check for user mistakes
            if info["firstName"] == "" or info["lastName"] == "" or info["username"] == "" or info["textInput"] == "" or info["file"] == "":
                errorLabel.grid(row=8, column=1, columnspan=2, padx=10, pady=(0, 10))
                print(info["firstName"] + info["lastName"] + info["username"] + info["textInput"] + info["file"])
            else:
                #put data in db
                try:
                    conn = dbConnection.conn
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO `help` (`firstname`, `lastname`, `username`, `text`, `filepath`, `type`) VALUES (%s, %s, %s, %s, %s, %s)", 
                        (info["firstName"], info["lastName"], info["username"], info["textInput"], info["file"], "technical"))
                    conn.commit()
                    showinfo(title= "Επιτυχής Καταχώρηση Αιτήματος", 
                        message= "Το αίτημά σας έχει καταχωρηθεί στο σύστημα, στοιχεία αιτήματος:" + "\n" 
                            + "First Name: " + info["firstName"] + "\n" 
                            + "Last Name: " + info["lastName"] + "\n" 
                            + "Username: " + info["username"] + "\n" 
                            + "Technical Problem: " + info["textInput"] + "\n"
                            + "Uploaded File: " + info["file"])
                except Error as e:
                    showinfo(title="Πρόβλημα Καταχώρηση Αιτήματος", 
                        message="Το αίτημά σας δεν μπόρεσε να καταχωρηθεί στο σύστημα, παρακαλώ προσπαθήστε αργότερα!" + 
                            "Κωδικός σφάλματος: " + e)
    # submit button
    submissionbutton = Button(help_window ,text="Υποβολή", padx=10, pady=20,
                            fg="#413c69", activeforeground="#413c69", bg="#e1fa40", activebackground="#e1fa40",
                            command=submission)
    submissionbutton.grid(row=7, column=1, columnspan=2, padx=10, pady=10)
    submissionbutton.config(font=("Calibri bold", 16))

    #error label
    global errorLabel 
    errorLabel = Label(help_window, text="Δεν έχετε γράψει όλα τα στοιχεία που χρειάζονται", 
        background="#4a47a3", 
        font=("Calibri bold", 7),
        foreground="red")
   

