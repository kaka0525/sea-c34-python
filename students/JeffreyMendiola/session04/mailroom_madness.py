"""
===============================================================================
file: mailroom_madness.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/01/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #11 Mailroom Madness
Description:
     This program allows the user to "SEND A THANK YOU" or "CREATE A REPORT".
     The program will keep looping until asked to stop.

     If the user wishes to "SEND A THANK YOU", the program will prompt for a
     full name and donation amount. Afterwards, it will add the donation to
     the user's donation history and display the thank you e-mail to be sent
     to the donor. If the user would like a list of all the donors, the user
     may enter "List" in response to the "Enter Full Name" prompt.

     If the user wishes to "CREATE A REPORT", the program will display a table
     of the donors sorted by total historical donation amount.
     The table will include:
        - Donor name
        - Total amount donated
        - Number of donations
        - Average donation.
===============================================================================
"""
import sys

# default list of donors
# "donor name": [donation]

donors = {
    "Kobe Bryant": [24000],
    "Manny Pacquiao": [17000],
    "Mike Trout": [100000],
    "Russell Wilson": [1000, 1000, 1000]
}

# task 10: exception feature


def safe_input(user_prompt):
    """
    This wrapper function takes in a string that is to be prompted
    to the user. If an EOFError or KeyboardInterrupt error is raised,
    the function returns None.
    Args:
        user_prompt: This is the question to be prompted to the user.
    Result:
        return string (user's input) or None

    """
    try:
        user_input = raw_input(user_prompt)
        return user_input
    except (EOFError, KeyboardInterrupt):
        return None


def thank_you():
    """
    The function prompts for a full name, donation amount, and displays the
    "Thank-you" e-mail to be sent to the donor.

    If the user enters "List", the function displays a list of all the donors.

    Args:
        None

    Return:
        None
    """
    while True:
        # name_input = raw_input("\nEnter Full Name: ")
        name_input = safe_input("\nEnter Full Name: ")
        if name_input is None:
            raise sys.exit("\n\n(program has ended)\n\n")
        else:
            name_input = name_input.title()

        if name_input.isalpha() is False:
            if len(name_input) <= 2:
                print "\nOops! Please enter 2+ characters."
            else:
                print "\nOops! Please only use letters."
        elif name_input == "List":
            print "List of Donors:"
            counter = 0
            for person in donors:
                counter += 1
                print str(counter) + ". " + str(person)
        elif name_input == "Q":
            break
        else:
            new_member = False

            if name_input not in donors:
                new_member = True
                donors[str(name_input)] = [0]

            while True:
                # donation = raw_input("\nEnter Donation Amount: $ ")
                donation = safe_input("\nEnter Donation Amount: $ ")
                if donation is None:
                    raise sys.exit("\n\n(program has ended)\n\n")
                if donation.upper() == "Q":
                    break
                elif donation.isdigit() is True:
                    donation = int(donation)
                    break
                else:
                    # donation = raw_input("\nOops! Please only use numbers: ")
                    donation = safe_input("\nOops! Please only use numbers.")

            if type(donation) is int:
                pass
            else:
                break
            if new_member is True:
                donors[str(name_input)] = [donation]
            else:
                if donors[str(name_input)] == [0]:
                    donors[str(name_input)] = [donation]
                else:
                    donors[str(name_input)].extend([donation])

            n = str(name_input)
            d = str(donation)

            print "\n\n"
            print "(email to be sent)\n"
            print "Dear {name},\n\n" \
                  " Thank you for your donation of ${amount}.\n\n" \
                  " We appreciate your generosity.\n\n" \
                  "Sincerely,\n\n" \
                  "Taco Corp.\n\n".format(name=n, amount=d)
            break


def new_report():
    """
    The function displays a report of the donors sorted by total historical
    donation amount.

    Args:
        None

    Return:
        None
    """
    donors_sort = []

    for name in donors:
        total_donated = sum(donors[name])
        num_donations = len(donors[name])
        if total_donated == 0:
            avg_donation = 0
            num_donations = 0
        else:
            avg_donation = total_donated / num_donations
        donors_sort.append([name, total_donated, num_donations, avg_donation])

    donors_sort = sorted(donors_sort, reverse=True, key=lambda donor: donor[1])
    print "\n"
    print "{:<20}   {:<10} {:<5}   {:<10}".format('Name', 'Total', '#', 'Avg.')
    for x in donors_sort:
        print "{:<20} $ {:<10} {:<5} $ {:<10}".format(x[0], x[1], x[2], x[3])


# Main Menu Prompt
while True:
    print "\n"
    print "=== MAIN MENU ============================================="
    print "\nA) Send a Thank You\n"
    print "B) Create a Report\n"
    print "Q) Quit\n"
    print "==========================================================="
    print "\n"
    # user_action = raw_input("What would you like to do? : ")
    user_action = safe_input("What would you like to do? : ")
    if user_action is None:
        raise sys.exit("\n\n(program has ended)\n\n")
    else:
        user_action = user_action.upper()

    if user_action == "A":
        thank_you()
    elif user_action == "B":
        new_report()
    elif user_action == "Q":
        print "\nBye!\n"
        raise sys.exit("\n\n(program has ended)\n\n")
    else:
        print "\nEntry Error! You must enter A, B, or Q.\n"
