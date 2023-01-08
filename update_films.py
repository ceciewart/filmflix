# --- Importing relevant files ---
from film_connect import *
from time import sleep
from read_films import read_films

# A subroutine that will update a single field on the film files
# by identifying the record using the filmID


def update_films():
    while True:
        menu_options = ["1", "2", "3", "4", "5", "6"]
        print("******************* \n UPDATING A RECORD \n*******************")
        read_films()  # so the user can see the IDs
        id_field = input(
            "Enter the Movie ID of the record to be updated or 'q' to exit: ")
        if id_field == "q":
            print("Closed Film Updating")
            break
        field_name = input(
            "Which field would you like to update: \n1 - Title\n2 - Year Released\n3 - Rating \n4 - Duration \n5 - Genre \n6 - Exit \nType here:")
        if field_name == "1":
            field_name = "title"
        elif field_name == "2":
            field_name = "yearReleased"
        elif field_name == "3":
            field_name = "rating"
        elif field_name == "4":
            field_name == "duration"
        elif field_name == "5":
            field_name = "genre"
        elif field_name == "6":
            print("Closed Film Updating")
            break
        elif field_name not in menu_options:
            print(f"Field Input: {field_name} is not a valid option")
            break

        new_field_value = input(f"Enter the new value for {field_name}: ")
        print("******************* \n RECORD UPDATED \n*******************")
        print(
            f"Record {id_field} has been updated | {field_name}: {new_field_value}")
        new_field_value = "'" + new_field_value + "'"

        # update FILMs table
        cursor.execute(
            f"UPDATE tblFilms SET {field_name} = {new_field_value} WHERE filmID = {id_field}")
        conn.commit()

        sleep(3)

        read_films()


if __name__ == "__main__":
    update_films()
