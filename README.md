
# Selenium End-to-End Automation Test

Welcome! This project uses Selenium with Python to automate end-to-end tests for the login functionality on [Practice Test Automation](https://practicetestautomation.com/practice-test-login/). The tests follow the **Page Object Model (POM)** design pattern to keep the code clean and easy to maintain.

---

## What This Project Does

The test suite covers these scenarios:

1. Logging in with **valid** username and password (using centralized test data)  
2. Trying to log in with **invalid** credentials and capturing the error message  
3. Checking if the **logout button** or success message appears after logging in  
4. Trying to access a **protected page** without logging in  
5. Logging out and verifying that the session ends properly and the protected page is no longer accessible  

---

## Technologies Used

- **Python 3.x**  Python 3.12.6
- **Selenium WebDriver** for browser automation  
- **Pytest** as the testing framework  
- **webdriver-manager** for managing browser drivers automatically  
- **python-dotenv** to handle environment variables (like URLs)  
- Following the **Page Object Model (POM)** to organize the code  
- **Centralized test data** management in `test_data.py` for easy maintenance  

---

## Project Layout

```
selenium_automation_project/
├── pages/
│   ├── base_page.py         # Common page methods used by other pages
│   ├── login_page.py        # Actions and locators related to the login page
│   └── success_page.py      # Actions and locators for the success page after login
├── tests/
│   └── test_login.py        # The test cases themselves
├── conftest.py              # Setup code like WebDriver initialization
├── test_data.py             # Centralized test data (usernames, passwords, error messages)
├── .env                     # Environment variables (URLs)
├── requirements.txt         # Required Python packages
└── README.md                # This file
```

---

## Setting Up Environment Variables

Create a `.env` file at the project root with this content:

```env
BASE_URL=https://practicetestautomation.com
```

---

## How to Get Started

1. Clone this repo to your machine:

```bash
git clone https://github.com/YasarEid/login-test.git
cd login-test
```

2. Install the needed Python packages:

```bash
pip install -r requirements.txt
```

3. Create your `.env` file as explained above.

---

## Running the Tests

Simply run:

```bash
python -m pytest tests/test_login.py
```

Pytest will pick up and run all the test cases in the `tests/` folder.

---

## Tests Included

| Test Case                           | What it does                                     |
|-------------------------------------|-------------------------------------------------|
| Valid Login                         | Logs in successfully with correct credentials    |
| Invalid Username                    | Tries to log in with wrong username               |
| Invalid Password                    | Tries to log in with wrong password               |
| Access Protected Page Without Login | Tries to open success page without logging in   |
| Logout                              | Logs out and verifies session is closed          |

---

## Why This Approach?

- Using **Page Object Model (POM)** makes tests easier to read and maintain  
- Explicit waits ensure tests wait for page elements to load properly  
- Using environment variables keeps config clean and flexible  
- Centralized test data management simplifies maintenance and avoids duplication
- Writing tests with **pytest** allows for modular, readable test code  

---

## About Me

Hi, I'm Yasar Naser, a QA Engineer passionate about test automation and writing clear, maintainable code.  
If you have any questions or want to connect, feel free to reach me at:  
**Email:** yasar.e.naser@gmail.com

---
