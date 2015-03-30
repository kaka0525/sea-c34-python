# Task 11: Mailroom Madness

# list of donors and history of donation amounts

donors = {
    "Russell Wilson": [1000, 1000, 1000],
    "Marshawn Lynch": [10000, 14000],
    "Richard Sherman": [25000]
}

# send a thank you


def thank_you():
    while True:
        name_input = raw_input("Enter Full Name: ")
        name_input = name_input.title()

        if name_input == "List":
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
                donors[str(name_input)] = None

            donation = raw_input("Enter Donation Amount: $")

            while True:
                if donation.upper() == "Q":
                    break
                elif donation.isdigit() is True:
                    donation = int(donation)
                    break
                else:
                    donation = raw_input("Oops! Please only use numbers: ")

            if type(donation) is int:
                pass
            else:
                break
            if new_member is True:
                donors[str(name_input)] = [donation]
            else:
                donors[str(name_input)].extend([donation])

            n = str(name_input)
            d = str(donation)

            print "\n"
            print "Dear {name},\n" \
                  " Thank you for your donation of ${amount}.\n" \
                  " We appreciate your generosity.\n \n" \
                  "Sincerely,\n\n" \
                  "Taco Corp.\n".format(name=n, amount=d)
            break

# main menu prompt


def user_menu():
    """
    Display user main menu with a list of options.
    Keep looping until user enters "Q"
    """
    print "MAIL ROOM MENU:\n"
    print "A) SEND A THANK YOU\n"
    print "B) CREATE A REPORT\n"
    print "Q) QUIT\n"

    while True:
        user_action = raw_input("WHAT WOULD YOU LIKE TO DO?: ")
        user_action = user_action.upper()

        if user_action == "A":
            print "SELECTION: SEND A THANK YOU \n"
            thank_you()
        elif user_action == "B":
            print "SELECTION: CREATE A REPORT \n"
            # new_report()
        elif user_action == "Q":
            print "SELECTION: QUIT"
            print "BYE!"
            # quit()
            break
        else:
            print("SELECTION: %s" % user_action)
            print "Sorry, you must enter A, B, or Q.\n"

user_menu()
