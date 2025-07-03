import os
import time
import pandas as pd
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Create output folders
os.makedirs("screenshots", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Logging setup
logging.basicConfig(
    filename="logs/test_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Read users from Excel
df = pd.read_excel("users.xlsx")
results = []

# Setup Chrome
driver = webdriver.Chrome()
driver.maximize_window()

for index, row in df.iterrows():
    username = row["Username"]
    password = row["Password"]
    result = {"Username": username, "Password": password}

    try:
        # Open site
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)

        # Enter credentials
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Validate login
        if "inventory" in driver.current_url:
            result["Status"] = "Pass"
            result["Error"] = ""
            screenshot_path = f"screenshots/{username}_success.png"
            logging.info(f"Login successful for: {username}")

            # Screenshot and logout
            driver.save_screenshot(screenshot_path)
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(1)
            driver.find_element(By.ID, "logout_sidebar_link").click()
            time.sleep(1)
        else:
            raise AssertionError("Login failed (locked out or invalid user)")

    except Exception as e:
        result["Status"] = "Fail"
        result["Error"] = str(e)
        screenshot_path = f"screenshots/{username}_fail.png"
        driver.save_screenshot(screenshot_path)
        logging.error(f"Login failed for: {username} - Reason: {e}")

    result["Screenshot"] = screenshot_path
    results.append(result)

driver.quit()

# Report DataFrame
report_df = pd.DataFrame(results)

# Save Excel Report
report_df.to_excel("test_result.xlsx", index=False)

# Generate HTML Report
html_content = """
<html>
<head>
    <meta charset="UTF-8">
    <title>Login Test Report</title>
    <style>
        body { font-family: Arial; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
        th { background-color: #f2f2f2; }
        .pass { color: green; }
        .fail { color: red; }
    </style>
</head>
<body>
    <h2>Login Test Report</h2>
    <table>
        <tr><th>Username</th><th>Status</th><th>Error</th><th>Screenshot</th></tr>
"""

for _, row in report_df.iterrows():
    status_class = "pass" if "Pass" in row["Status"] else "fail"
    html_content += f"<tr>"
    html_content += f"<td>{row['Username']}</td>"
    html_content += f"<td class='{status_class}'>{row['Status']}</td>"
    html_content += f"<td>{row['Error']}</td>"
    html_content += f"<td><a href='{row['Screenshot']}' target='_blank'>View</a></td>"
    html_content += f"</tr>"

html_content += """
    </table>
</body>
</html>
"""

# Write HTML report
with open("test_report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Reports generated: test_result.xlsx and test_report.html")


