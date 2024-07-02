from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to read URLs from a .txt file
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    # Remove any leading/trailing whitespace characters
    urls = [url.strip() for url in urls]
    return urls

# Function to scrape LeetCode question details
def scrape_leetcode_questions(urls):
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    question_data = []

    for url in urls:
        driver.get(url)
        time.sleep(3)  # Wait for the page to load completely

        # Extract question title
        try:
            title_element = driver.find_element(By.CLASS_NAME, "text-title-large")
            title = title_element.text if title_element else "N/A"
        except Exception as e:
            title = "N/A"

        # Extract difficulty level
        try:
            difficulty = "N/A"
            if driver.find_elements(By.CLASS_NAME, "text-difficulty-hard"):
                difficulty = "Hard"
            elif driver.find_elements(By.CLASS_NAME, "text-difficulty-medium"):
                difficulty = "Medium"
            elif driver.find_elements(By.CLASS_NAME, "text-difficulty-easy"):
                difficulty = "Easy"
        except Exception as e:
            difficulty = "N/A"

        # Extract question content from a div that contains <p> and <ul>
        try:
            content_element = driver.find_element(By.XPATH, '//div[contains(@class, "elfjS")]')
            content = content_element.text if content_element else "N/A"
            # content_div = driver.find_element(By.XPATH, '//div[contains(@class, "elfjS")]')
            # content_elements = content_div.find_elements(By.XPATH, './*')

            # content = ""
            # for element in content_elements:
            #     if element.tag_name == "p":
            #         content += element.text
            #         # Include <code> content within <p>
            #         code_elements = element.find_elements(By.TAG_NAME, "code")
            #         for code_element in code_elements:
            #             content += " " + code_element.text
            #         content += "\n"
            #     elif element.tag_name == "ul":
            #         list_items = element.find_elements(By.TAG_NAME, "li")
            #         for item in list_items:
            #             content += "- " + item.text + "\n"
            #     else:
            #         content += element.text + "\n"

        except Exception as e:
            content = "N/A"

        # Store the extracted data
        question_data.append({
            "url": url,
            "title": title,
            "difficulty": difficulty,
            "content": content
        })

    # Close the WebDriver
    driver.quit()

    return question_data

# Function to write question data to a .txt file
def write_questions_to_file(questions, output_file_path):
    with open(output_file_path, 'w') as file:
        for question in questions:
            file.write(f"URL: {question['url']}\n")
            file.write(f"Title: {question['title']}\n")
            file.write(f"Difficulty: {question['difficulty']}\n")
            file.write(f"Content:\n{question['content']}\n")
            file.write("\n" + "-"*80 + "\n\n")

# Path to the .txt file containing LeetCode question URLs
input_file_path = 'leetcode_urls.txt'
# Path to the output .txt file
output_file_path = 'leetcode_questions_output.txt'

# Read URLs from the file
urls = read_urls_from_file(input_file_path)

# Scrape the questions
questions = scrape_leetcode_questions(urls)

# Write the scraped data to the output file
write_questions_to_file(questions, output_file_path)

print(f"Scraped data has been written to {output_file_path}")
