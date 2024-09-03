from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
service = Service('/Users/jordantorres/Desktop/chromedriver')  # Update the path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the fantasy football stats page
url = 'https://www.espn.com/nfl/stats'

# Open the URL
driver.get(url)

# Find the table containing the stats
table = driver.find_element(By.CSS_SELECTOR, 'table.Table--align-right.Table--fixed.Table--fixed-left')

# Extract the headers
headers = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]

# Extract the data rows
rows = []
for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:
    cells = row.find_elements(By.TAG_NAME, 'td')
    row_data = [cell.text.strip() for cell in cells]
    rows.append(row_data)

# Print the stats
print(headers)
for row in rows:
    print(row)

# Close the WebDriver
driver.quit()
