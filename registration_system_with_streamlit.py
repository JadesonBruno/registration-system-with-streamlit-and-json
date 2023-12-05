# Importing Streamlit and JSON libraries
import streamlit as st
import json

# Function to read data from the JSON file
def read_file(file_name='users.json'):
    try:
        with open(file_name, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save data to the JSON file
def save_users(file_name='users.json'):
    with open(file_name, "w", encoding='utf-8') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

# Function to insert new users
def insert_users(users):
    # Assigns a new ID to the user
    new_id = len(users) + 1

    # Get user information via graphical interface
    name = st.text_input("Enter the user's name:")
    phone = st.text_input("Enter the user's phone number:")
    address = st.text_input("Enter the user's address:")

    # Button to finish and add to the user dictionary
    if st.button("Add user!"):
        # Handling for empty fields
        name = name if name != '' else "Not specified"
        phone = phone if phone != '' else "Not specified"
        address = address if address != '' else "Not specified"

        # Create a new user
        new_user = {
            'Status': True,
            'Name': name,
            'Phone': phone,
            'Address': address
        }

        user_found = False

        for user in users:
            if users[user]['Name'] == name and users[user]['Phone'] == phone and users[user]['Address'] == address:
                # Handling for inactive users
                if users[user]['Status'] == False:
                    users[user]['Status'] = True
                    user_found = True
                    st.success('Existing record, reactivating...')
                    break
                # Handling for users already in the system
                else:
                    user_found = True
                    st.warning('Record already exists in the system!')
                    break

        # Add the new user if it does not exist in the dictionary
        if not user_found:
            users[new_id] = new_user
            st.success('User added successfully!')

    # Save the data after the operation
    save_users()

# Function to delete users
def delete_users(users):
    # Get the user ID to be deleted via graphical interface
    delete_id = st.text_input("Enter an ID:")

    # Button to finish and delete from the user dictionary
    if st.button("Delete user!"):
        user_found = False

        for user in users:
            # Delete user if it exists
            if user == delete_id and users[user]['Status'] == True:
                user_found = True
                users[user]['Status'] = False
                st.success(f'User "{user}" deleted successfully!\n')
                break

        # Handling for non-existent users
        if delete_id not in users and not user_found:
            st.warning(f'User "{delete_id}" not found!\nEnter a valid ID!')
        # Handling for users who have already been deleted
        elif delete_id in users and not user_found:
            user_found = True
            st.warning(f'User "{delete_id}" has already been deleted from the system!')

    # Save the data after the operation
    save_users()

# Function to edit user information
def edit_users(users):
    # Initialize graphical interface state control variables
    if 'button_update_clicked' not in st.session_state:
        st.session_state.button_update_clicked = False

    if 'button_option_clicked' not in st.session_state:
        st.session_state.button_option_clicked = False

    # Get the user ID to be updated via graphical interface
    update_id = st.text_input("Enter an ID to update")  # ID input for update

    # Button to signal the start of the update process
    if st.button("Update user!"):
        st.session_state.button_update_clicked = True

    # Execute the update logic if the button was clicked
    if st.session_state.button_update_clicked:
        user_found = False

        for user in users:
            # Check if the user ID exists and is active
            if user == update_id and users[user]['Status'] == True:
                user_found = True

                # Display options to choose what to update
                st.markdown("<h3 style='color: black;'>Which information would you like to change?</h3>", unsafe_allow_html=True)
                st.markdown("<h5 style='color: black;'>Please choose a numeric option:</h5>", unsafe_allow_html=True)
                st.markdown("<h6 style='color: black;'>1 - Name</h6>", unsafe_allow_html=True)
                st.markdown("<h6 style='color: black;'>2 - Phone</h6>", unsafe_allow_html=True)
                st.markdown("<h6 style='color: black;'>3 - Address</h6>", unsafe_allow_html=True)

                # Get the chosen option via graphical interface
                option = st.text_input("Choose an option")

                # Button to confirm the choice
                if st.button("Choose option!"):
                    st.session_state.button_option_clicked = True

                # Execute the logic of the chosen option
                if st.session_state.button_option_clicked:
                    if option == "1":
                        # Get the new user name via graphical interface
                        new_name = st.text_input("Enter the new user name: ")
                        # Button to confirm the name update
                        if st.button("Register name!"):
                            users[update_id]["Name"] = new_name
                            st.success("User updated successfully!")

                    elif option == "2":
                        # Get the new user phone number via graphical interface
                        new_phone = st.text_input("Enter the new user phone number: ")
                        # Button to confirm the phone number update
                        if st.button("Register phone!"):
                            users[update_id]["Phone"] = new_phone
                            st.success("User updated successfully!")

                    elif option == "3":
                        # Get the new user address via graphical interface
                        new_address = st.text_input("Enter the new user address: ")
                        # Button to confirm the address update
                        if st.button("Register address!"):
                            users[update_id]["Address"] = new_address
                            st.success("User updated successfully!")

                    else:
                        st.warning("Invalid option. Please try again!")

                    break
        # Handling for non-existent users
        if update_id not in users and not user_found:
            st.warning(f'User "{update_id}" not found!\nEnter the user ID:\n')
            st.session_state.button_update_clicked = False

        # Handling for users who have already been deleted
        elif update_id in users and not user_found:
            st.warning(f'User "{update_id}" has already been deleted from the system!\n')

    # Save the data after the operation
    save_users()

# Function to display information about a specific user
def display_user(users):

    # Get the user ID to be viewed via graphical interface
    display_id = st.text_input("Enter the user ID to view their data: ")

    # Button to display user information
    if st.button("Display a user!"):

        user_found = False

        for user in users:
            # Check if the user exists and is active
            if user == display_id and users[user]['Status'] == True:
                user_found = True
                # Display user information
                st.write(f'ID: {user}\n\nName: {users[user]["Name"]}\n\nPhone: {users[user]["Phone"]}\n\nAddress: {users[user]["Address"]}\n')
                break

        # Handling for non-existent users
        if display_id not in users and not user_found:
            st.warning(f'User {display_id} not found!\nEnter the User ID:\n ')
            display_id = input('Enter the User ID: ')

        # Handling for users who have already been deleted
        elif display_id in users and not user_found:
            st.warning(f'User "{display_id}" has already been deleted from the system!\n')

# Function to display information about all active users
def display_all_users(users):

    for user in users:
        # Check if the user is active
        if users[user]['Status']:
            # Display user information
            st.write(f'ID: {user}\n\nName: {users[user]["Name"]}\n\nPhone: {users[user]["Phone"]}\n\nAddress: {users[user]["Address"]}\n\n')

# Main function that controls the flow of the application
def main():

    # Dropdown to select and execute the option via graphical interface
    choice = st.sidebar.selectbox("Choose an option", ["Insert users", "Delete users", "Update user information",
                                                       "Access information about a user", "Access information about all users", "Exit the system"])

    if choice == "Insert users":
        option1()
    elif choice == "Delete users":
        option2()
    elif choice == "Update user information":
        option3()
    elif choice == "Access information about a user":
        option4()
    elif choice == "Access information about all users":
        option5()
    elif choice == "Exit the system":
        option6()

# Function to handle the option: insert users
def option1():
    st.markdown("<h1 text-align: center; style='color: red;'>Welcome to the registration system!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 text-align: center; style='color: red;'>You chose the option: insert a new user.</h2>", unsafe_allow_html=True)

    insert_users(users)

# Function to handle the option: delete users
def option2():
    st.markdown("<h1 text-align: center; style='color: red;'>Welcome to the registration system!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 text-align: center; style='color: red;'>You chose the option: delete a user.</h2>", unsafe_allow_html=True)

    delete_users(users)

# Function to handle the option: update user information
def option3():
    st.markdown("<h1 text-align: center; style='color: red;'>Welcome to the registration system!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 text-align: center; style='color: red;'>You chose the option: update data of a user.</h2>", unsafe_allow_html=True)

    edit_users(users)

# Function to handle the option: access information about a specific user
def option4():
    st.markdown("<h1 text-align: center; style='color: red;'>Welcome to the registration system!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 text-align: center; style='color: red;'>You chose the option: view data of a user.</h2>", unsafe_allow_html=True)

    display_user(users)

# Function to handle the option: access information about all users
def option5():
    st.markdown("<h1 text-align: center; style='color: red;'>Welcome to the registration system!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 text-align: center; style='color: red;'>You chose the option: view data of all users.</h2>", unsafe_allow_html=True)

    display_all_users(users)

# Function to handle the option: exit the system
def option6():
    st.markdown("<h1 text-align: center; style='color: red;'>You chose the option: exit the system. Thank you for visiting! </h1>", unsafe_allow_html=True)

# Read the JSON file
users = read_file()

# Execute the main function
main()
