#!/usr/bin/env python
donation_list = {"Peter": [300, 200], "Paul": [200, 35], "Mary": [100],
                 "Joe": [99.02], "Karen": [200]}


def main_program():
    while True:
        user_input = raw_input(u"Send a thank you, enter 1  or Create a "
                               "report, enter 2, quit, enter 3"
                               " to quit anytime ")
        if (user_input == "1"):
            send_thank_you()
        elif (user_input == "2"):
            create_a_report()
        elif (user_input == "3"):
            break
        else:
            print ("sorry i don't recognize your command")


def get_donation_amount():
    while True:
        amount = raw_input(u"How much do you want to donate? ")
        try:
            return float(amount)
        except:
            print ("Please enter a number")


def send_thank_you():
    prompt_name = None
    while True:
        prompt_name = raw_input(u" Enter the full name of the recipient."
                                " Type list to see a list of donor names ")
        if prompt_name == "list" or prompt_name == "List":
            print (donation_list)
            continue
        if prompt_name.isalpha():
            if prompt_name not in donation_list:
                donation_list[prompt_name] = []
            donation_list[prompt_name].append(get_donation_amount())
            thankyou_letter(prompt_name)
            break


def thankyou_letter(prompt_name):
    print ("Dear {name}, Thank you for your generous "
           "donation.".format(name=prompt_name))


def create_a_report():
    donor_info = []
    for (name, donation) in donation_list.items():
        total_donated = float(sum(donation))
        num_donation = len(donation)
        donor_info.append({
            "name": name,
            "total_donated": total_donated,
            "num_donation": num_donation,
            "average_donation": total_donated / num_donation})
    donor_info.sort(key=lambda donor: donor["total_donated"])
    for donor in donor_info:
        print ("{name} has donated {num_donation} times with a total donation"
               " of {total} dollars; an average of {average_donation} per"
               " donation".format(name=donor["name"],
                                  num_donation=donor["num_donation"],
                                  total=donor["total_donated"],
                                  average_donation=donor["average_donation"]))


if __name__ == "__main__":
    main_program()
