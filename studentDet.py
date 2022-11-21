import tkinter as tk
import csv
# Import DictWriter class from CSV module
from csv import DictWriter
import os

root = tk.Tk()
root.title("Student Details")
root.geometry("500x500")
root.configure(bg="black")
# root.resizable(False, False)
formDetails = {}

# Create a frame to hold the widgets
frame = tk.Frame(root, bg="black")
frame.pack()

# Create a label for the title
title = tk.Label(frame, text="Student Details", font=(
    "Times New Roman", 20, "bold"), bg="black", fg="white")
title.grid(row=0, column=0, columnspan=2, pady=10)

# Create a label for the first name
studentFirstName = tk.Label(frame, text="First Name:", font=(
    "Times New Roman", 15, "bold"), bg="black", fg="white")
studentFirstName.grid(row=1, column=0, padx=10, pady=10)

# Create an entry box for the first name
studentFirstNameEntry = tk.Entry(frame, font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=30)
studentFirstNameEntry.grid(row=1, column=1, padx=10, pady=10)

# Create a label for the last name
studentLastName = tk.Label(frame, text="Last Name:", font=(
    "Times New Roman", 15, "bold"), bg="black", fg="white")
studentLastName.grid(row=2, column=0, padx=10, pady=10)

# Create an entry box for the last name
studentLastNameEntry = tk.Entry(frame, font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=30)
studentLastNameEntry.grid(row=2, column=1, padx=10, pady=10)

# Create a label for the Matric Number
studentMatricNo = tk.Label(frame, text="Matric No:", font=(
    "Times New Roman", 15, "bold"), bg="black", fg="white")
studentMatricNo.grid(row=3, column=0, padx=10, pady=10)

# Create an entry box for the Matric Number
studentMatricNoEntry = tk.Entry(frame, font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=30)
studentMatricNoEntry.grid(row=3, column=1, padx=10, pady=10)

# Create a label for the Subject
studentSubject = tk.Label(frame, text="Subject:", font=(
    "Times New Roman", 15, "bold"), bg="black", fg="white")
studentSubject.grid(row=4, column=0, padx=10, pady=10)

# Create an entry box for the Subject
studentSubjectEntry = tk.Entry(frame, font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=30)
studentSubjectEntry.grid(row=4, column=1, padx=10, pady=10)

# Create a label for the Score
studentSubjectScore = tk.Label(frame, text="Subject Score:", font=(
    "Times New Roman", 15, "bold"), bg="black", fg="white")
studentSubjectScore.grid(row=5, column=0, padx=10, pady=10)

# Create an entry box for the Score
studentSubjectScoreEntry = tk.Entry(frame, font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=30)
studentSubjectScoreEntry.grid(row=5, column=1, padx=10, pady=10)


def showError(shouldShow, message):
    showErrorLabel = tk.Label(frame, text="", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="red")
    showErrorLabel.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    if shouldShow:
        showErrorLabel.config(text=message)
        showErrorLabel.after(3000, lambda: showErrorLabel.destroy())
    else:
        showErrorLabel.destroy()


def writeObjToCSVFile(obj):
    with open('student.csv', 'a', newline='') as file:
        # Create a DictWriter object
        writer = DictWriter(file, fieldnames=obj.keys())
        # Add the data to the CSV file
        writer.writerow(obj)

def getAllDataInCSVFile():
    with open('student.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
def getAllDataInCSVWithPandas():
    df = pd.read_csv('student.csv')
    print(df)
# def saveDetailsToExcel(obj): 
#     filepath = "studentsData.xlsx"
#     # Check if the file exists
#     if os.path.isfile(filepath):
#         # Open the file in append mode
#         wb = openpyxl.load_workbook(filepath)
#         # Get the active sheet
#         sheet = wb.active
#         # Append the data to the sheet
#         sheet.append(obj)
#         # Save the file
#         wb.save(filepath)


def enterDetails():
    formDictionary = {
        "firstname": studentFirstNameEntry.get(),
        "lastname": studentLastNameEntry.get(),
        "matric-no": studentMatricNoEntry.get(),
        "Subject": studentSubjectEntry.get(),
        "Score": studentSubjectScoreEntry.get()
    }
    # Form Validating
    if formDictionary["firstname"] == "":
        print("First Name is required")
        showError(True, "First Name is required")
    elif formDictionary["lastname"] == "":
        print("Last Name is required")
        showError(True, "Last Name is required")
    elif formDictionary["matric-no"] == "":
        print("Matric Number is required")
        showError(True, "Matric Number is required")
    elif formDictionary["Subject"] == "":
        print("Subject is required")
        showError(True, "Subject is required")
    elif formDictionary["Score"] == "":
        print("Subject Score is required")
        showError(True, "Subject Score is required")
    else:
        showError(False, "")
        print(formDictionary)
        # saveDetailsToExcel(formDictionary)
        writeObjToCSVFile(formDictionary)
        getAllDataInCSVFile()
        # clear form inputs
        studentFirstNameEntry.delete(0, tk.END)
        studentLastNameEntry.delete(0, tk.END)
        studentMatricNoEntry.delete(0, tk.END)
        studentSubjectEntry.delete(0, tk.END)
        studentSubjectEntry.delete(0, tk.END)
        studentSubjectScoreEntry.delete(0, tk.END)


# Create a button to submit the form
submitButton = tk.Button(frame, text="Submit", font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=30, command=enterDetails)
submitButton.grid(row=6, column=0, columnspan=2, padx=10, pady=20)


root.mainloop()
