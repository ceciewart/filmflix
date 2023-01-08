# --- Importing relevant files ---
from film_connect import *
from time import sleep
from read_films import read_films

# A subroutine that will delete a single record
# By identifying it using the filmID


def delete_film():

    read_films()
    print(
        """\n********************************************
        \nCHOOSE RECORD TO DELETE FROM THE LIST ABOVE\n
        """)

    id_field = input("Enter the filmID of the record to be deleted: ")
    cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {id_field}")
    conn.commit()

    print(f"Record {id_field} deleted from Filmflix.")
    sleep(3)

    read_films()


if __name__ == "__main__":
    delete_film()
