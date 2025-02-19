
# QA Challenge 🔍

## Introduction

This repository showcases a framework for web automation utilizing **Playwright** and **Cucumber**. It features integrated loggers and reports to enhance test visibility and management. Explore the project to understand how automated tests are structured and executed effectively.

## Prerequisites

Before you begin, ensure you have **Python** and **pip** installed on your system. You can verify your installations by running the following commands in your terminal:

```bash
python --version
```
```bash
pip --version
```

If Python is not installed, you can download it from [python.org](https://www.python.org/downloads/). Pip is generally installed automatically with Python.

## Setting Up the Virtual Environment 🛠️

1. **Clone the repository:**

   ```bash
   git clone git@github.com:ensolvers-github-challenges/Sivila-376a18.git
   ```
   ```bash
   cd Sivila-376a18
   ```

2. **Create a virtual environment:**

   In your terminal, navigate to the project directory and run:

   ```bash
   python -m venv env
   ```

   This command creates a new virtual environment named `env` in your current directory.

3. **Activate the virtual environment:**

   - On **Windows**:

     ```bash
     env\Scripts\activate
     ```

   - On **macOS** and **Linux**:

     ```bash
     source env/bin/activate
     ```

   Activating the virtual environment ensures that the installed libraries and Python commands run within this isolated environment.

## Installing Dependencies 📦

1. **Install project dependencies:**

   Once the virtual environment is activated, install the required libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   playwright install
   ```

## Running the Project 🚀

To run the project follow these steps:

## Configuring Execution:

To configure the execution, create a `.env` file in the root project with the following parameters, for example:

```env
BASE_URL=https://qa-challenge.ensolvers.com
USER=username
PASSWORD=password
```

You can also add additional tests in the `/features/scenarios` directory to extend the test suite.
1. **Run the main script:**

   ```bash
   pytest
   ```

   This command will start the execution of all test in **headed mode**. 

2. **Running Tests by Marker:**

   You can also execute tests based on specific markers. Here are some examples:

   - **Account Information tests**  
     ```bash
     pytest -m change_account_information
     ```

   - **Folder section tests**  
     ```bash
     pytest -m manage_folders
     ```

   - **Login Tests:**  
     ```bash
     pytest -m login
     ```

   - **To Do items section Tests:**  
     ```bash
     pytest -m manage_to_do_items
     ```


# Test Suite for Ensolvers QA Challenge

## Test Case Specific Markers:

### Test Cases by Use Case:

- **UC-001: Successful Login with valid credentials**  
  This test case ensures that the user can successfully log in with valid credentials and is redirected to the homepage with a confirmation message.  
    ```bash
    pytest -m uc_001
    ```

- **UC-002: Failed Login with invalid credentials**  
  This test case verifies that the system handles invalid login attempts appropriately, showing an error message and preventing access to the homepage.  
    ```bash
    pytest -m uc_002
    ```

- **UC-003: Successful Logout**  
  This test case checks that the user can successfully log out, and the system confirms the logout action, ensuring that the session is terminated.  
    ```bash
    pytest -m uc_003
    ```

- **UC-004: Access "Manage To-Do Items" Section**  
  This test case ensures that the user can navigate to the "Manage To-Do Items" section successfully, and that the option to create a new To-Do item is visible.  
    ```bash
    pytest -m uc_004
    ```

- **UC-005: Access "Manage Folders" Section**  
  This test case checks if the user can navigate to the "Manage Folders" section, where they can create and manage folders.  
    ```bash
    pytest -m uc_005
    ```

- **UC-006: Create a Folder**  
  This test case validates the process of creating a new folder. The system should allow the user to provide a folder name and save it to the folder list.  
    ```bash
    pytest -m uc_006
    ```

- **UC-007: Rename a Folder**  
  This test case checks that the user can rename an existing folder, ensuring the new name is saved and displayed correctly.  
    ```bash
    pytest -m uc_007
    ```

- **UC-008: Delete a Folder**  
  This test case ensures that a folder can be successfully deleted. It verifies that the system displays a confirmation prompt and removes the folder from the list after deletion.  
    ```bash
    pytest -m uc_008
    ```

- **UC-009: Create a To-Do Item**  
  This test case ensures that the user can successfully create a new To-Do item, including providing a title, description, and folder selection. The new task should appear in the list of To-Do items.  
    ```bash
    pytest -m uc_009
    ```

- **UC-010: Delete a To-Do Item**  
  This test case verifies that a To-Do item can be deleted successfully. The system should prompt the user for confirmation and remove the item from the list.  
    ```bash
    pytest -m uc_010
    ```

- **UC-011: Edit a To-Do Item**  
  This test case ensures that an existing To-Do item can be edited, with the system confirming the update and displaying the changes in the To-Do list.  
    ```bash
    pytest -m uc_011
    ```

- **UC-012: Change Account Information**  
  This test case validates that the user can update their account information, including their first name, last name, and email, in the account settings.  
    ```bash
    pytest -m uc_012
    ```

### How to Run Specific Tests:
To run a specific test case or group of tests, use the `-m` option followed by the desired marker. For example, to test folder management:

```bash
pytest -m uc_004
```

## Running Tests with Different Browsers:

To run tests with different browsers, use the `--browser` parameter in the CLI:

```bash
pytest --browser webkit
```

```bash
pytest --browser firefox
```

```bash
pytest --browser chromium
```

To run in **headed** mode (with a graphical interface), use the `--headed` option:

```bash
pytest --headed
```

The program executes in **headed mode** by default (without a graphical interface) unless you specify otherwise.

You can also combine as for example:
```bash
pytest --headed --browser webkit
```
## Viewing Test Results

After running your tests, the results will be automatically generated and stored in the `/reports` folder. To view the test outcomes in detail, simply open the `report.html` file in your browser. 

If any issues occur during the tests or if you need more detailed troubleshooting information, check the logs located in the `/log` directory. These logs provide detailed insights into the test execution, helping to identify any failures or errors.

---

## Task Overview

### Task 1: [Build a Use Case list]  
To view the details of Task 1, click on the link below:  
[Use Cases.pdf](https://drive.google.com/file/d/1AfivkAYerTisCwRm8OEP6cVvgWIbzCii/view?usp=sharing)

### Task 2: [Test the app end-to-end and report any bug or UX issue]  
To view the details of Task 2, click on the link below: 16 Bugs found. 
[BugReports.pdf](https://drive.google.com/file/d/1HaH0ILqDlqLwKrWKA6oYcrv0ffR4884t/view?usp=sharing)



## About the Author 👨‍💻

This project was created by **Alvaro Sivila**, a dedicated QA Automation Engineer with expertise in various automation tools and frameworks. If you're interested in my work, feel free to check out my portfolio or connect with me on LinkedIn:

- **Portfolio:** [Portfolio](https://junior0123.github.io/QAPortfolio/)
- **LinkedIn:** [Alvaro Sivila](https://www.linkedin.com/in/alvaro-sivila-ram%C3%ADrez-0a8537113/)


