# --- Importing relevant files ---
from film_connect import *
from read_films import read_films
from time import sleep

# A subroutine that will insert new records in the filmflix table and
# print the table of records including the new film added.


def insert_films():
    films = []

    print("******************* \n INSERT MOVIES \n*******************")

    # Creating variables to be added to the table from User Input:
    # filmID was not created as set to autoincrement
    title = input("Enter the movie title: ").title()
    year_released = input(f"Enter the year '{title}' was released: ")
    rating = input(f"Enter '{title}' rating: ").upper()
    duration = input(f"Enter '{title}' duration in minutes: ")
    genre = input(f"Enter '{title}' genre: ").title()

    # Appending to the list
    films.append(title)
    films.append(year_released)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    # Prints the content added by the user as a List
    print(films)

    # Adding input to table
    cursor.execute("INSERT INTO tblFilms VALUES (NULL, ?, ?, ?, ?, ?)", films)
    conn.commit()

    # Printing user's action and reads the content of the table on the Terminal
    print(
        f"*******************\nMOVIE TITLE: '{title}' was added to Filmflix\n*******************")
    sleep(4)

    read_films()


if __name__ == "__main__":
    insert_films()
