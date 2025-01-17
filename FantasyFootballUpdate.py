from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# Configure WebDriver (Update path to your WebDriver)
driver_path = "path/to/chromedriver"  # Replace with the path to your WebDriver
driver = webdriver.Chrome(driver_path)

# Open the fantasy football stats page
url = "https://www.fantasypros.com/nfl/rankings/overall.php"  # Example site (use a real one)
driver.get(url)

# Wait for the page to load
time.sleep(3)

# Scrape data
player_stats = []

try:
    # Locate the table containing player stats
    table = driver.find_element(By.XPATH, '//table[@id="rank-data"]')  # Adjust XPath as needed
    rows = table.find_elements(By.XPATH, './/tr')[1:]  # Skip header row

    for row in rows:
        # Extract individual columns
        cols = row.find_elements(By.XPATH, './/td')
        if len(cols) > 1:  # Ensure it's a valid row
            player_name = cols[1].text  # Name of the player
            position = cols[2].text  # Position (e.g., QB, RB)
            team = cols[3].text  # NFL team
            points = cols[4].text  # Fantasy points

            player_stats.append({
                "Name": player_name,
                "Position": position,
                "Team": team,
                "Points": points
            })

finally:
    # Close the browser
    driver.quit()

# Save stats to a CSV file
output_file = "fantasy_football_stats.csv"
with open(output_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Position", "Team", "Points"])
    writer.writeheader()
    writer.writerows(player_stats)

print(f"Scraped {len(player_stats)} players' stats and saved to {output_file}.")

