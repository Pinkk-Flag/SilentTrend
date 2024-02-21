'''
This file is used in order to scrape the data from indsider week data and then creates a CSV.
'''

from bs4 import BeautifulSoup
import requests
import csv

url = "https://insider-week.com/en/cot/"

# Fetch the HTML content using requests
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, "html.parser")  # Now 'soup' is defined

# Now you can use soup to find table rows
table_data = soup.find_all("td")[:1100]

filtered_td = soup.find_all("td", class_= ["widthCol1", "redColor widthCol1"])

# Find all <a> tags
numbers = [tag.get_text(strip=True) for tag in soup.find_all('a')]

numeric_values = []
for number in numbers:
    number = number.replace(' ', '')  # Remove whitespaces
    if number.replace('-', '').isdigit():  # Check if the remaining string is a digit
        numeric_values.append(number)  # Append number
    elif number.startswith('-') and number[1:].isdigit():  # Check for negative numbers
        numeric_values.append(number)  # Append number

# Specify the relative file path
file_path = 'Weekly Data CSV/Data.csv'
'''
Write the data into a CSV file

It ensures that the data given is only the first 8 then skips the next 9.
This ensures that we only get the data from COMMERCIAL and LARGE SPECULATORS

In that 8, it then only gets the first 1st, 3rd, 5th and 7th point.
'''
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    for i in range(0, len(numeric_values), 17):  # Loop through the list with a step of 17
        for j in range(0, 8, 2):  # Loop through the indices of the desired points
            writer.writerow([numeric_values[i+j]])  # Write the desired point on a new line
