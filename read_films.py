# --- Importing the connection ---
from film_connect import *

# A subroutine that will read the films in the table
# and print each record


def read_films():

    cursor.execute("SELECT * FROM tblFilms")
    row = cursor.fetchall()
    print("******************* \n FILMFLIX RECORDS \n*******************")
    print(f"Total number of records: {len(row)}")
    for film_record in row:
        print(film_record)


if __name__ == "__main__":
    read_films()
