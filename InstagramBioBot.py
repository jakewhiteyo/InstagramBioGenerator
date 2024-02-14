from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import openai
import sys

GPT_MODEL_NAME = 'gpt-3.5-turbo-instruct'

def generate_caption():
   response = openai.Completion.create(
            model=GPT_MODEL_NAME,
            prompt="Give me a sentence of the structure - {adjective} doing it. Where {adjective} is a complicated one-word exaggeration (example: unequivocally). Make the adjective pretty complex and require a high reading level. You can replace {doing} with words like [handling, running, doing, making]. Only respond with these 3 words in this format.",
            max_tokens=50, 
            n=1,
            stop=None, 
            temperature=1 
        )
   return response.choices[0].text.strip()

def drive_to_instagram(username, password, bio):
  options = Options()
  options.add_argument("--headless")
  driver = webdriver.Firefox(options=options)
  driver.implicitly_wait(10)
  driver.get("https://www.instagram.com/accounts/edit/")
  driver.find_element(By.NAME, "username").send_keys(username)
  driver.find_element(By.NAME, "password").send_keys(password)
  driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div").click()
  time.sleep(5)
  driver.get("https://www.instagram.com/accounts/edit/")
  driver.find_element(By.ID, "pepBio").clear()
  driver.find_element(By.ID, "pepBio").send_keys(bio)
  driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/div/div/form/div[4]/div").click()
  time.sleep(5)
  driver.quit();

def main():
  username = sys.argv[1]
  password = sys.argv[2]
  key = sys.argv[3]
  openai.api_key = key

  bio = generate_caption()
  drive_to_instagram(username, password, bio);

if __name__ == '__main__':
    main()