# --- Importing relevant files ---

from film_connect import *
from time import sleep
from read_films import read_films

# A subroutine that creates a report


def create_report():

    while True:
        try:
            user_options = ["1", "2", "3", "4"]
            print("******************* \n CREATING REPORT MODE \n*******************")
            user_choice = input(
                "1 - Year Released |2 -  Rating |3 - Duration |4 - Genre |5 - Exit \nEnter Option: ")
            if user_choice == "1":
                choose_year = int(
                    input("What year would you like to search? "))
                query = "SELECT * FROM tblFilms WHERE yearReleased=?"
                cursor.execute(query, (choose_year,))
                print(
                    f"******************* \n FILMFLIX REPORT - Films from {choose_year}  \n*******************")

            elif user_choice == "2":
                choose_rating = input(
                    "PG | PG-13 | G | R |\nPlease inform rating to search: ").upper()
                query = "SELECT * FROM tblFilms WHERE rating=?"
                cursor.execute(query, (choose_rating,))

                print(
                    f"******************* \n FILMFLIX REPORT - Film RATING: {choose_rating}  \n*******************")

            elif user_choice == "3":
                choose_duration = int(input("How many minutes? "))
                query = "SELECT * FROM tblFilms WHERE duration=?"
                cursor.execute(query, (choose_duration,))

                print(
                    f"******************* \n FILMFLIX REPORT - Film Duration: {choose_duration} Minutes  \n*******************")

            elif user_choice == "4":
                choose_genre = input(
                    '''Action| Animation | Comedy | Crime | Fantasy |\nMovie Genre to search:''').title()
                query = "SELECT * FROM tblFilms WHERE genre=?"
                cursor.execute(query, (choose_genre,))
                print(
                    f"******************* \n FILMFLIX REPORT - Film By Genre: {choose_genre} \n*******************")
            elif user_choice == "5":
                print("Closed Reports")
                break   
            elif user_choice not in user_options:
                print(
                    f"User choice: {user_choice} | Invalid option, try again ")
        except (ValueError, TypeError) as err:
            print("Invalid input information try again")
            print(err)

        row = cursor.fetchall()
        conn.commit()
        for film_record in row:
            print(
                f'''Film ID: {film_record[0]} | Title: {film_record[1]} | Year: {film_record[2]}
            \nRating: {film_record[3]} | Duration: {film_record[3]} |Genre: {film_record[4]}
            \n ------ ''')

        break


if __name__ == "__main__":
    create_report()
