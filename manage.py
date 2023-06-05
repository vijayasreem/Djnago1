#!/usr/bin/env python

import sys

from sacralai.configure import JiraSoftware

def main():
    if len(sys.argv) < 2:
        print("Please provide the necessary credentials to login to Sacral.ai website")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    jira = JiraSoftware(username, password)

    # Login to Sacral.ai website
    jira.login()

    # Access “Expert Services to change Business” page
    jira.access_expert_services_page()

    # Click on Configure
    jira.configure()

    # Click on Jira Software
    jira.click_jira_software()

    # Enter Jira Software credentials
    jira.enter_jira_credentials()

    # Click on reset button to enter the details again
    jira.reset_jira_credentials()

    # Click on save button to configure
    jira.save_jira_credentials()

    # Validate the Jira Software credentials and return a response
    response = jira.validate_jira_credentials()
    if response.status_code == 200:
        print("Jira Software credentials are valid")
    else:
        print("Jira Software credentials are invalid")
        sys.exit(1)

    # Display the list with Title, User Name, URL, Action
    jira.display_list()

    # Display edit button and delete button to make any changes to the displayed list Title, User Name and URL
    jira.edit_list()
    jira.delete_list()

    # Change the No of entries to display in the list, while clicking on dropdown button in “Show entries”
    jira.change_entry_count()

    # Display pagination under the list
    jira.show_pagination()

    # Click on pagination to change the page numbers
    jira.change_page_numbers()

    # Display Add more button above the list to configure other Jira Software
    jira.add_more_jira_software()

    # Display Pop Up form
    jira.show_popup_form()

    # Enter the required details
    jira.enter_required_details()

    # Click on reset button to enter the details again
    jira.reset_details()

    # Click on save button to configure
    jira.save_details()


if __name__ == "__main__":
    main()