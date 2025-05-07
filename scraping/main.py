from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

# Set up Selenium WebDriver with ChromeDriver (Ensure ChromeDriver is installed and in your PATH)
chrome_driver_path = '/opt/homebrew/bin/chromedriver'  # Update the path to your ChromeDriver

# Use Service class to set the ChromeDriver path
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the URL
url = 'https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham/'
driver.get(url)

# Wait for the table to load (explicit wait for the table element to be visible)
try:
    # Wait until the table is loaded (using a more generic selector for the table)
    table = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'table')))
    
    # Extract headers (column names) from the table
    headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, 'th')]

    # Extract rows of the table
    rows = []
    for tr in table.find_elements(By.TAG_NAME, 'tr')[1:]:  # Skip the header row
        cols = tr.find_elements(By.TAG_NAME, 'td')
        row = [col.text.strip() for col in cols]
        rows.append(row)

    # Check the number of columns in the rows
    for idx, row in enumerate(rows[:5]):  # Print first 5 rows for debugging
        print(f"Row {idx + 1} has {len(row)} columns: {row}")
    
    # Ensure the number of columns in rows matches the headers
    if len(headers) == len(rows[0]):
        # Create DataFrame from the rows and headers
        df = pd.DataFrame(rows, columns=headers)

        # Add the "Kode Saham" column with your NPM value
        df['NPM'] = '065123007'

        # Save the DataFrame to a CSV file
        file_path = os.path.join(os.path.dirname(__file__), 'assets', 'output_data.csv')
        df.to_csv(file_path, index=False)

        # Display the first few rows of the DataFrame
        print(df.head())
    else:
        print(f"Number of columns in headers and rows do not match. Headers: {len(headers)}, Rows: {len(rows[0])}")
    
except Exception as e:
    print("An error occurred while scraping the table:", e)

finally:
    # Close the browser
    driver.quit()
