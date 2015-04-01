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

            donation = raw_input("Enter Donation Amount: $ ")

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
            print "Dear {name},\n\n" \
                  " Thank you for your donation of ${amount}.\n\n" \
                  " We appreciate your generosity.\n\n" \
                  "Sincerely,\n\n" \
                  "Taco Corp.\n\n".format(name=n, amount=d)
            break

# new report


def new_report():

    donors_sort = []

    for name in donors:
        total_donated = sum(donors[name])
        num_donations = len(donors[name])
        avg_donation = total_donated / num_donations
        donors_sort.append([name, total_donated, num_donations, avg_donation])

    donors_sort = sorted(donors_sort, reverse=True, key=lambda donor: donor[1])

    print "{:<20} {:<10} {:<5} {:<10}".format('Name', 'Total', '#', 'Avg.')
    for x in donors_sort:
        print "{:<20} {:<10} {:<5} {:<10}".format(x[0], x[1], x[2], x[3])


# main menu prompt

"""
========== MAIN ===============================================================
- Display user main menu with a list of options.
- Keep looping until user enters "Q"
===============================================================================
"""
while True:
    print "\n\nMAIL ROOM MENU:\n"
    print "A) SEND A THANK YOU\n"
    print "B) CREATE A REPORT\n"
    print "Q) QUIT\n"
    user_action = raw_input("WHAT WOULD YOU LIKE TO DO?: ")
    user_action = user_action.upper()

    if user_action == "A":
        print "SELECTION: SEND A THANK YOU\n"
        thank_you()
    elif user_action == "B":
        print "SELECTION: CREATE A REPORT\n"
        new_report()
    elif user_action == "Q":
        print "\nBYE!\n"
        break
    else:
        print("SELECTION: %s" % user_action)
        print "Sorry, you must enter A, B, or Q.\n"
