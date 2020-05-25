# ------------------------------------------------------------------------#
# !/usr/bin/env python3
# Title: cli_main.py
# Desc: The module cli_main.py would include all of your user interaction functions and main program flow.
# Tian Xie, 2020-05-21, Created File
# ------------------------------------------------------------------------#


from donor_models import Donor as D
from donor_models import DonorCollection as DC

# Initiate Default DonorCollection
donor_collection = DC()

# A dictionary of donor paired with a list of donation amounts

# Main Prompt
main_prompt = "\n".join(("=======  Main Menu ======= \n",
                         "Welcome to the Mailroom. Please select an option:",
                         "1: Send a Thank You to a single donor",
                         "2: Create a Report",
                         "3: Send letters to all donors",
                         "4: Exit",
                         ">>> "))


def menu_selection(prompt, dispatch_dict):
    """Displays a menu of choices to the user
    Args:
        prompt: main menu
        dispatch_dict: choices for user to choose from
    Returns:
        None.
    """
    while True:
        response = input(prompt)  # continuously collect user selection
        try:
            int(response)
            if dispatch_dict[response]() == "Exit Menu":
                break
        except KeyError:
            print('\nError: you entered {}, which is not a number from 1-4. Please select again >'.format(response))
        except ValueError:
            print('\nError: you entered {}, which is not a number from 1-4. Please select again >'.format(response))

def send_thank_you():
    """Sending a thank you email using user input.

    Args:
       None

    Returns:
       None

    """
    # Ask user for a donor's name or to display current list of donors, then ask for donation amount
    print()
    while True:
        donor_name = input('======= The Thank you Menu: =======\n'
                           "Enter 'list' for to see the list of donors\n"
                           "or enter full name of donor. \n"
                           "Enter 'exit' to return to the main menu >").title()
        if donor_name == "Exit": #If the user types exist return to main menu.
            break
        elif donor_name == "List": #If the user types list show them a list of the donor names and re-prompt.
            print('======= The Donor List: =======')
            print(donor_collection.show_donor_list())
        else:
            donation_amount = input('Please enter a donation amount for ' + donor_name + ' >')
            while True:
                try:
                    float(donation_amount)
                    break
                except ValueError:
                    donation_amount = input('Error: Please enter a number for the donation amount>')
            donor_collection.add_new_donation(donor_name, donation_amount)
            print(donor_collection.get_donor(donor_name).create_email())
            break


def send_all():
    """Writing a letter for each donor and save them into a directory with the donor's name.

    Args:
       None

    Returns:
       None.
   """
    for name in donor_collection:
        file_name = f'{name.replace(" ", "_"):}.txt'
        with open(file_name, 'w') as objfile:
            objfile.write(f'Dear {name},\n\nThank you for your generosity, your donation of ${donor_collection[name][-1]:.2f} will be put to very good use.\n\n'
                          f'Your total donation amount is ${sum(donor_collection[name]):.2f}.\n\nWarm regards,\nMailroom Staff')


def display_report(report):
    """Displaying the report.

    Args:
       report generated from create_report_format function

    Returns:
       None

    """
    for item in report:
        print(item)

def create_report():
    """Creating format and then display.

    Args:
       None

    Returns:
       None

    """
    report = donor_collection.create_report_format()
    display_report(report)


def quit():
    print("Exiting the menu now")
    return "Exit Menu"


main_dispatch = {'1': send_thank_you,
                 '2': create_report,
                 '3': send_all,
                 '4': quit,
                 }

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
