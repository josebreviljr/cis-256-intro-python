"""
    Name: Jose F. Brevil, Jr.
    Student ID: 011064137
    Submission Date: 11.02.25
    Program: Assignment 3
    Sources Consulted: Runestone Academy - How to Think Like a Computer Scientist: Interactive Edition, CIS 256 Slides

    By submitting this work, I attest that it is my original work and that I did not violate
    the University of Mississippi academic policies set forth in the M book or any
    policies of the course.
"""
import os
import datetime as dt
from time import sleep


def main():
    print("\nWelcome to Jose's Library System!")
    sleep(.5)
    print("Loading library...")
    library = load_library()
    sleep(.5)

    while True:
        print("-" * 30)
        print("| JLS: Jose's Library System |")
        print("-" * 30)
        print("| a: View Current Library    |")
        print("| b: Checkout Book           |")
        print("| c: Return Book             |")
        print("| d: View Library Logs       |")
        print("| e: Exit Library            |")
        print("-" * 30)

        user_choice = input("Selection: ").strip()

        if user_choice == "a":
            sleep(1)
            view_library()
        if user_choice == "b":
            checkout_book()
        if user_choice == "c": 
            return_book()
        if user_choice == "d":
            view_logs()
        if user_choice == "e":
            print("\nThank you for using this system.")
            sleep(.5)
            return False
        exit

def load_library():
    try:
        with open("library.txt", "r") as file:
                file.readlines()
                print("Loaded library successfully.")
    except FileNotFoundError:
            print("Library not found––writing default library.")
            with open("library.txt", "w") as file:
                file.write("A Time to Kill::3\n")
                file.write("The Firm::2\n")
                file.write("The Pelican Brief::1\n")
                file.write("The Client::1\n")
                file.write("The Chamber::2\n")
                file.write("The Rainmaker::1\n")
                file.write("The Partner::5\n")
                file.write("The Street Lawyer::3\n")
                file.write("The Testament::1\n")
                sleep(1)
                print("Loaded library successfully.")
            return load_library
            return library
 
def view_library():
    try:
        with open("library.txt", "r") as file:
            print("\nCurrent Library Collection:")
            print("-" * 30)
            for line in file:
                print(line.strip())  # prints each line as-is
            print("-" * 30, "\n")
            sleep(1)
    except FileNotFoundError:
        print("Library file not found.")

def checkout_book():
    book_to_checkout = input("\nEnter the title of the book you want to check out: ").strip()

    try:
        with open("library.txt", "r") as file:
            books = file.readlines()
    except FileNotFoundError:
        print("Library file not found.")
        return

    found = False
    updated_books = []

    for line in books:
        title, copies = line.strip().split("::")
        copies = int(copies)
        if title.lower() == book_to_checkout.lower():
            found = True
            if copies > 0:
                copies -= 1
                print(f"Successfully checked out '{title}'. Enjoy reading!")
                log_action(f"Checked out '{title}'")
            else:
                print(f"Sorry, '{title}' is currently not available.")
        updated_books.append(f"{title}::{copies}\n")

    if not found:
        print(f"Book '{book_to_checkout}' not found in the library.")

    with open("library.txt", "w") as file:
        file.writelines(updated_books)


def log_action(action):
    timestamp = dt.datetime.now().isoformat(sep=" ", timespec="seconds")
    with open("checkout_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {action}\n")


def return_book():
    book_to_return = input("\nEnter the title of the book you want to return: ").strip()

    try:
        with open("library.txt", "r") as file:
            books = file.readlines()
    except FileNotFoundError:
        print("Library file not found.")
        return

    found = False
    updated_books = []

    for line in books:
        title, copies = line.strip().split("::")
        copies = int(copies)
        if title.lower() == book_to_return.lower():
            found = True
            copies += 1
            print(f"Successfully returned '{title}'. Thank you!")
            log_action(f"Returned '{title}'")
        updated_books.append(f"{title}::{copies}\n")

    if not found:
        print(f"Book '{book_to_return}' not found in the library.")

    with open("library.txt", "w") as file:
        file.writelines(updated_books)


def view_logs():
    sleep(.5)
    try:
        with open("checkout_log.txt", "r") as log_file:
            logs = log_file.readlines()
            if not logs:
                print("\nNo checkout or return logs available yet.\n")
                return
            print("\nLibrary Checkout/Return Logs:")
            print("-" * 50)
            for line in logs:
                print(line.strip())
            print("-" * 50, "\n")
    except FileNotFoundError:
        print("\nNo checkout logs found. No books have been checked out or returned yet.\n")

        







if __name__ == "__main__":
        main()
    
