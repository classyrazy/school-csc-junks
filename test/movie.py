# create the form to search movie
from imdb import Cinemagoer
from matplotlib import pyplot as plt
import PyMovieDb
from PyMovieDb import IMDB
import tkinter as tk
import json
import numpy as np
import io
import csv
# Import DictWriter class from CSV module
from csv import DictWriter
import pandas as pd
import os
# ia = Cinemagoer()
ia = IMDB()
root = tk.Tk()
root.title("Movie Scraper")
root.geometry("800x800")
root.configure(bg="black")

# create a frame to hold the widgets
frame = tk.Frame(root, bg="black")
frame.pack()

title = tk.Label(frame, text="Movie Scrapper", font=(
    "Times New Roman", 20, "bold"), bg="black", fg="white")
title.grid(row=0, column=0, columnspan=2, pady=10)

# Create a label for the first name
searchMovies = tk.Label(frame, text="Name Of Movie:", font=(
    "Times New Roman", 15, "bold"), bg="black", fg="white")
searchMovies.grid(row=1, column=0, padx=10, pady=10)

# Create an entry box for the first name
searchMoviesEntry = tk.Entry(frame, font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=30)
searchMoviesEntry.grid(row=1, column=1, padx=10, pady=10)
# label.pack()
# Searching movies that have rock in their name


def search():
    print("Searching...")
    userSearchValue = searchMoviesEntry.get()
    # movies = ia.search_movie("rock")
    print(userSearchValue)
    # movies = ia.search_movie(userSearchValue)

    movies = ia.get_by_name(userSearchValue)

    # print(movies[0])
    result = json.loads(movies)

    movieName = result["name"]
    movieNameLabel = tk.Label(frame, text=movieName, font=(
        "Times New Roman", 15, "bold"), bg="black", fg="white")
    movieNameLabel.grid(row=2, column=0, padx=10, pady=10)
    # loop through and display genres
    genres = result["genre"]
    tableRow = 2
    for genre in genres:
        tk.Label(frame, text=genre, font=("Times New Roman", 15, "bold"),
                 bg="black", fg="white").grid(row=tableRow, column=1, padx=10, pady=10)
        tableRow += 1

    searchMoviesEntry.delete(0, tk.END)
    print(result)
    addMovieToCSV(genres)

    # print(movies[0].keys())


def addMovieToCSV(genreArr):
    print("Adding movie to CSV file")
    genresAvail = getAllDataInCSVFileAndTurnIntoArray()

    print(genresAvail)
    if len(genresAvail) > 0:
        for genre in genreArr:
            if genre in genresAvail:
                print("Genre already in CSV file")
                # read the csv file
                df = pd.read_csv('movies.csv')
                # get the row that contains the genre
                row = df.loc[df['genre'] == genre]
                # get the count of the genre
                count = row['count'].values[0]
                # increment the count
                count += 1
                # update the count
                df.loc[df['genre'] == genre, 'count'] = count
                # write the changes to the csv file
                df.to_csv('movies.csv', index=False)
            else:
                obj = {
                    "genre": genre,
                    "count": 1
                }
                with open('movies.csv', 'a', newline='') as file:
                    # Create a DictWriter object
                    writer = DictWriter(file, fieldnames=obj.keys())
                    if os.stat('movies.csv').st_size == 0:
                        writer.writeheader()
                    # Add the data to the CSV file
                    writer.writerow(obj)

    else:
        for gen in genreArr:
            obj = {
                "genre": gen,
                "count": 1
            }
            with open('movies.csv', 'a', newline='') as file:
                # Create a DictWriter object
                writer = DictWriter(file, fieldnames=obj.keys())
                if os.stat('movies.csv').st_size == 0:
                    writer.writeheader()
                # Add the data to the CSV file
                writer.writerow(obj)


def viewAnalysis():
    df = pd.read_csv('movies.csv')
    allGenres = df["genre"].tolist()
    allCounts = df["count"].tolist()
    genratePieChart(allGenres, allCounts )
    # for genre in arrayOfGenres:
    #     obj = {
    #         "genre": genre
    #     }

    # with open('movies.csv', 'a', newline='') as file:
    #     # Create a DictWriter object
    #     writer = DictWriter(file, fieldnames=obj.keys())
    #     if os.stat('movies.csv').st_size == 0:
    #         writer.writeheader()
    #     # Add the data to the CSV file
    #     writer.writerow(obj)
    # getAllDataInCSVFileAndExplore(obj)


def genratePieChart(labelArray, dataArray):

    # Creating plot
    fig = plt.figure(figsize=(10, 7))
    plt.pie(dataArray, labels=labelArray)

    # show plot
    plt.show()


def getAllDataInCSVFileAndTurnIntoArray():
    if os.stat('movies.csv').st_size != 0:
        df = pd.read_csv('movies.csv')
        allGenres = df['genre']
        allGenres = np.array(allGenres)

        # unstringify element of the allGenres array
        # allGenres = [eval(x) for x in allGenres]
        # flat_list = list(np.concatenate(allGenres).flat)
        # # turn insto a set to remove duplicates
        # flat_list = set(flat_list)
        return allGenres
    else:
        return []


searchButton = tk.Button(frame, text="Search", font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=15, command=search)
searchButton.grid(row=6, column=1, columnspan=1, padx=10, pady=20)

dataExplore = tk.Button(frame, text="View Analysis", font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=15, command=viewAnalysis)
dataExplore.grid(row=6, column=0, columnspan=1, padx=10, pady=20)


root.mainloop()
