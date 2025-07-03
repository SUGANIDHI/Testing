### 📄 `README.md`

```markdown
# 🧪 Selenium Automated Login & Purchase Testing

This project automates login and purchase flow on [SauceDemo](https://www.saucedemo.com/) using Python, Selenium, and pytest. It reads user credentials from Excel files and generates detailed logs, screenshots, and an HTML report.

---

## 📂 Project Structure

```

project/
├── main.py                # Test script
├── credentials.xlsx       # Excel file with username/password
├── buyers.xlsx            # Excel file with buyers' usernames
├── logs/
│   └── test\_log.txt       # Execution logs
├── screenshots/
│   └── \*.png              # Screenshots on failure/success
└── reports/
└── report.html        # HTML test report


## 📦 Requirements

Install dependencies using pip:

```bash
pip install selenium pandas openpyxl pytest pytest-html
````

---

## 📊 Excel Format

### credentials.xlsx

| username          | password      |
| ----------------- | ------------- |
| standard\_user    | secret\_sauce |
| locked\_out\_user | secret\_sauce |

### buyers.xlsx

| username                  |
| ------------------------- |
| standard\_user            |
| performance\_glitch\_user |

---

## 🚀 How to Run

Run the test and generate an HTML report:

```bash
pytest main.py --html=reports/report.html --self-contained-html
```

---

## ✅ Features

* 🔐 Automated login testing
* 🛒 Purchase flow testing for specific users
* 📸 Screenshots on success/failure
* 🪵 Logging of each test step
* 📊 HTML test report with assertions

---

## 🧪 Test Flow

1. Launch Chrome browser using Selenium.
2. Read user credentials from `credentials.xlsx`.
3. Attempt login for each user.
4. If the user is listed in `buyers.xlsx`, perform a purchase.
5. Logout and capture results.
6. Save logs, screenshots, and test status.
7. Generate an interactive HTML report.

---

## 📸 Sample Report

Open `reports/report.html` after execution to view pass/fail results with logs.

---

## 📌 Notes

* Ensure `chromedriver` is installed and accessible via PATH.
* You can modify `main.py` to test other workflows.
* Designed for demonstration and testing education purposes.

---

## 👨‍💻 Author

**Suganidhi Baskar**
*Automation Test Developer | Python | Selenium | Pytest*


