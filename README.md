# TwitterImageScraper
Opens the media tab on a twitter profile and scrapes images that profile has tweeted

(This code is a modification of israel-dryers twitter scraper, which scrapes certain text info and replies from tweets: https://github.com/israel-dryer/Twitter-Scraper)


This code will select a twitter profile, go to that profile's Media tab, and scrape images that have been tweeted from that profile.

This code currently only scrapes from about half of a user's tweets...it skips 11 every 9 tweets. If you have any thoughts on how to fix this, I am all ears, otherwise I will get to that fix when I have a bit.

This code scrapes using the Firefox browser, which you will need to have installed. 

For this code to work, you need to download the latest geckodriver webdriver, and put the exe file in your System PATH environment variable. 

you will also need to pip install selenium (make sure it is installed within whichever virtual environment you might be using) 


Lines you will have to change:

line 24 my_password = 'Your_password_here'
line 31 driver.get('https://www.twitter.com/NAMEOFPROFILETOSCRAPE')


You will know you are done when len(data) at the bottom tells you how many images were scraped 

    © 2021 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Docs

    Contact GitHub
    Pricing
    API
    Training
