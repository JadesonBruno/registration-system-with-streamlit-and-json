# Registration System with Streamlit and JSON

[![License](https://img.shields.io/npm/l/react)](https://github.com/JadesonBruno/registration-system-with-streamlit-and-json/blob/main/LICENSE)

## About the Project

This project implements a simple registration system using Streamlit, a Python library for creating web applications, and JSON, another Python library that allows you to interact with files in the file.json format. The system allows users to perform various operations such as inserting new users, deleting users, updating user information, and accessing information about individual users or all users.

This project was a prerequisite for approval in the “Programming Logic II” module of the “Vem Ser Tech Course - Data powered by [Ifood](https://www.ifood.com.br/) | Data Analystic” from the educational institution [Ada Tech](https://ada.tech/).

## Code Overview

### File Structure

- `registration_system_with_streamlit.py`: Python script containing the Streamlit application.
- `users.json`: json format file used to read and persist user information.

### Libraries Used

- **Streamlit**: Used for creating the web application.
- **JSON**: Used for reading and writing data to the JSON file.

### Functions

1. `read_file(file_name='users.json')` function:

- Reads data from the JSON file and returns it.

2. `save_users(file_name='users.json')` function:
   
- Saves user data to the JSON file.

3. `insert_users(users) function`:

- Inserts new users into the system.
- Handles duplicate entries and reactivation of previously deleted users.

4. `delete_users(users)` function:

- Deletes users based on their ID.
- Sets the user's status to inactive.
  
5. `edit_users(users)` function:

- Allows users to update their information.
- Provides an interactive interface to select the information to update.

6. `display_user(users)` function:

- Displays information about a specific user based on their ID.

7. `display_all_users(users)`:

- Displays information about all active users.

8. `main()` function:

- Controls the flow of the application.
- Uses Streamlit to create a sidebar with different options.

9. `option1() to option6()`:

- Functions handling specific options chosen by the user.
- Display appropriate messages and call corresponding functions.

## Technologies Used

- Python 3.10.9
- JSON library
- Streamlit library

## How to execute the project

To run the Python program, you need to have Python installed on your system and the Streamlit library. After installing the Python Environment and the Streamlit library, follow the steps below:

1. Clone the Repository:
   
- Clone the repository containing the **registration_system_with_streamlit.py** script and **users.json** file.

2. Keep in the same Directory:

- Keep the **registration_system_with_streamlit.py** script and **users.json** file in the same directory.

3. Run the Application:

Run the command below in the terminal::

```bash
streamlit run registration_system_with_streamlit.py
```

4. Interact with the System:

- The browser will open and you will be able to choose the sidebar options and interact with the system.

## Contributions

Feel free to contribute to the project by suggesting improvements, reporting issues, or enhancing features. Create issues or pull requests on the GitHub repository to collaborate.

## Author

Jadeson Bruno Albuquerque da Silva

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jadeson-bruno-228450101/)

