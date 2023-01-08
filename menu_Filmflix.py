# --- Importing relevant files ---
from read_films import read_films
from add_films import insert_films
from update_films import update_films
from delete_films import delete_film
from report_films import create_report

# --- Integration file ---

# A function that asks the user to what they want to do with Filmflix
# It keeps running until main_program becomes False.


def menu_options():
    options = 0
    while options not in ["1", "2", "3", "4", "5"]:
        print("""********************************************\nWELCOME TO FILMFLIX\n********************************************
        """)
        print("--MENU--\n1. Add a record.\n2. Delete a record.\n3. Amend a record.\n4. Print all records.\n5. Create Report\n6. Exit")
        # re-assign the value for the options variable
        options = input("\nEnter any of the options above: ")
        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not a valid choice")

    return options


menu_options()

main_program = True

while main_program:
    main_menu = menu_options()

    if main_menu == "1":
        insert_films()
    elif main_menu == "2":
        delete_film()
    elif main_menu == "3":
        update_films()
    elif main_menu == "4":
        read_films()
    elif main_menu == "5":
        create_report()
    else:
        main_program = False

    exit = input("Press Enter to 'q' (Quit) to exit the application ").lower()
    if exit == "q":
        break
