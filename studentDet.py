import tkinter as tk
import csv
# Import DictWriter class from CSV module
from csv import DictWriter
import pandas as pd
import os

root = tk.Tk()
root.title("Student Details")
root.geometry("800x800")
root.configure(bg="black")
# root.resizable(False, False)
formDetails = {}

# global variables

# meanValue = "0"
# maxScoreValue = "0"
# minScoreValue = "0"

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
        if os.stat('student.csv').st_size == 0:
            writer.writeheader()
        # Add the data to the CSV file
        writer.writerow(obj)


def getAllDataInCSVFile():
    with open('student.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def getAllDataInCSVWithPandas():
    df = pd.read_csv('student.csv')
    allScores = df['Score'].tolist()
    global meanValue
    global maxScoreValue
    global minScoreValue
    meanValue = df['Score'].mean()
    maxScoreValue = df['Score'].max()
    minScoreValue = df['Score'].min()
    print(allScores, "mean", meanValue, "max",
          maxScoreValue, "min", minScoreValue)
    dataFrame = pd.DataFrame(df)
    dataFrame = dataFrame.sort_values(by=['Score'], ascending=False)
    global topStudentresultDataFrame
    topStudentresultDataFrame = dataFrame[dataFrame['Score'] >= 70]
    print(dataFrame, topStudentresultDataFrame)

    global lowestStudentresultDataFrame
    lowestStudentresultDataFrame = dataFrame[dataFrame['Score'] < 70]


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
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=15, command=enterDetails)
submitButton.grid(row=6, column=0, columnspan=1, padx=10, pady=10)

# create another button to get data analysis


# create pack to display anlysis
def displayAnalysis():
    getAllDataInCSVWithPandas()

    # create a new window
    analysisWindow = tk.Toplevel(root)
    analysisWindow.title("Data Analysis")
    analysisWindow.geometry("500x500")
    analysisWindow.config(bg="black")
    # create a frame
    analysisFrame = tk.Frame(analysisWindow, bg="black")
    analysisFrame.pack()
    # create a label
    analysisLabel = tk.Label(analysisFrame, text="Exploratory Data Analysis", font=(
        "Times New Roman", 20, "bold"), bg="black", fg="white")
    analysisLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # create mean label
    meanLabel = tk.Label(analysisFrame, text="Mean:", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    meanLabel.grid(row=1, column=0, padx=10, pady=10)

    # create mean Value label
    meanValueLabel = tk.Label(analysisFrame, text=str(meanValue), font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    meanValueLabel.grid(row=1, column=1, padx=10, pady=10)

    # create max label
    maxLabel = tk.Label(analysisFrame, text="Max:", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    maxLabel.grid(row=2, column=0, padx=10, pady=10)

    # create max Value label
    maxValueLabel = tk.Label(analysisFrame, text=str(maxScoreValue), font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    maxValueLabel.grid(row=2, column=1, padx=10, pady=10)

    # create min label
    minLabel = tk.Label(analysisFrame, text="Min:", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    minLabel.grid(row=3, column=0, padx=10, pady=10)

    # create min Value label
    minValueLabel = tk.Label(analysisFrame, text=str(minScoreValue), font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    minValueLabel.grid(row=3, column=1, padx=10, pady=10)

    tablerow = 6
    # create Top Students table label
    topStudents = tk.Label(analysisFrame, text="Top Students", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    topStudents.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # create a table to display top students
    nameRow = tk.Label(analysisFrame, text="Name", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    nameRow.grid(row=5, column=0, padx=10, pady=10)

    for i in range(len(topStudentresultDataFrame)):
        tk.Label(analysisFrame, text=topStudentresultDataFrame.iloc[i, 0] + " " + topStudentresultDataFrame.iloc[i, 1], font=(
            "Times New Roman", 15, "bold"), bg="black", fg="white").grid(row=tablerow, column=0, padx=10, pady=10)
        tablerow += 1

    matricNoRow = tk.Label(analysisFrame, text="Matric No", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    matricNoRow.grid(row=5, column=1, padx=10, pady=10)

    tablerow = 6
    for i in range(len(topStudentresultDataFrame)):
        tk.Label(analysisFrame, text=topStudentresultDataFrame.iloc[i, 2], font=(
            "Times New Roman", 15, "bold"), bg="black", fg="white").grid(row=tablerow, column=1, padx=10, pady=10)
        tablerow += 1

    scoreRowLabel = tk.Label(analysisFrame, text="Score", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    scoreRowLabel.grid(row=5, column=2, padx=10, pady=10)

    tablerow = 6
    for i in range(len(topStudentresultDataFrame)):
        tk.Label(analysisFrame, text=topStudentresultDataFrame.iloc[i, 4], font=(
            "Times New Roman", 15, "bold"), bg="black", fg="white").grid(row=tablerow, column=2, padx=10, pady=10)
        tablerow += 1

    # create Lowest Students table label
    lowestStudentsLabel = tk.Label(analysisFrame, text="Lowest Students", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    lowestStudentsLabel.grid(row=tablerow+1, column=0,
                             columnspan=2, padx=10, pady=10)

    # create a table to display top students
    nameRowLowest = tk.Label(analysisFrame, text="Name", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    nameRowLowest.grid(row=tablerow+2, column=0, padx=10, pady=10)

    tablerowReset = tablerow
    print("table row reset", tablerowReset)
    tablerow += 3
    for i in range(len(lowestStudentresultDataFrame)):
        tk.Label(analysisFrame, text=lowestStudentresultDataFrame.iloc[i, 0] + " " + lowestStudentresultDataFrame.iloc[i, 1], font=(
            "Times New Roman", 15, "bold"), bg="black", fg="white").grid(row=tablerow, column=0, padx=10, pady=10)
        tablerow += 1

    matricNoRowLowest = tk.Label(analysisFrame, text="Matric No", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    matricNoRowLowest.grid(row=tablerowReset + 2, column=1, padx=10, pady=10)

    tablerow = tablerowReset + 3
    for i in range(len(lowestStudentresultDataFrame)):
        tk.Label(analysisFrame, text=lowestStudentresultDataFrame.iloc[i, 2], font=(
            "Times New Roman", 15, "bold"), bg="black", fg="white").grid(row=tablerow, column=1, padx=10, pady=10)
        tablerow += 1
    
    scoreRowLabelLowest = tk.Label(analysisFrame, text="Score", font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    scoreRowLabelLowest.grid(row=tablerowReset + 2, column=2, padx=10, pady=10)

    tablerow = tablerowReset + 3
    for i in range(len(lowestStudentresultDataFrame)):
        tk.Label(analysisFrame, text=lowestStudentresultDataFrame.iloc[i, 4], font=(
            "Times New Roman", 15, "bold"), bg="black", fg="white").grid(row=tablerow, column=2, padx=10, pady=10)
        tablerow += 1

    # create a button to close the window
    closeButton = tk.Button(analysisWindow, text="Close", font=(
        "Times New Roman", 15, "bold"), bg="white", fg="black", width=15, command=analysisWindow.destroy)
    closeButton.pack()


dataAnalysisButton = tk.Button(frame, text="Data Exploration", font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=15, command=displayAnalysis)
dataAnalysisButton.grid(row=6, column=1, columnspan=1, padx=10, pady=20)


root.mainloop()
