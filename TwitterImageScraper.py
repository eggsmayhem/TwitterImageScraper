from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver 
import re
import urllib.request

#test comment 

def get_tweet_data(card):
    """extract data from tweet"""  
    url = card.find_element_by_xpath('.//img[@alt="Image"]').get_attribute('src')
    l_url = re.sub("small", "large", url)
    tweet = (l_url)
    return tweet 

#create instance of web driver

driver = webdriver.Firefox()

driver.get('https://www.twitter.com/login')
driver.maximize_window()

username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username.send_keys('flipmybit@protonmail.com')
my_password = 'Your_password_here'

password = driver.find_element_by_xpath('//input[@name="session[password]"]')
password.send_keys(my_password)
password.send_keys(Keys.RETURN)
sleep(1)

driver.get('https://www.twitter.com/PROFILETOSCRAPE')
sleep(2)
driver.find_element_by_link_text('Media').click()

data = []
tweet_ids = set()
last_position = driver.execute_script("return window.pageYOffset;")
scrolling = True

while scrolling:
    page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweetPhoto"]')
    for card in page_cards:
        tweet = get_tweet_data(card)
        if tweet:
            tweet_id = ''.join(tweet)
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)
                data.append(tweet)
    
    scroll_attempt = 0
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)
        curr_position = driver.execute_script("return window.pageYOffset;")
        if last_position == curr_position:
            scroll_attempt += 1
            
            if scroll_attempt >= 3:
                scrolling = False
                break
            else:
                sleep(2)
        else:
            last_position = curr_position
            break

name = 0
for url in data:
    r = urllib.request.urlopen(url)
    global name
    with open(f'{name}.jpg', "wb") as f:
        f.write(r.read())
        name += 1
len(data)