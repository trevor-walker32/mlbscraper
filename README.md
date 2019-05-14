# MLBscraper

This repository uses the beautiful soup library to scrape the mlb website every weekday at 10:30pm for the latest statistics. 

# Getting Started

Make sure you have a up to date Framework of Python (Python3.6 <)

https://www.python.org/downloads/

Clone a copy of MLBscraper onto your machine and
cd into that directory.

First you need to run:  
pip3 install beautifulsoup4  
pip3 install requests

in that project directory.

Next, run python3 mlbscraper.py and enjoy your
structured data :)

# Configuring Automatic Scraping

Follow all of the steps in the Getting Started section. 

Then cd into the project directory to modify the .cron file. 

Change the <username> to your username on your machine. 
	
Make sure the path to python3.6 is correct, and that you have all of
the right packages installed. 

Run the command:  
crontab scraper.cron 

make sure it worked with:  
crontab -l

Check out the cron documentation:  
http://man7.org/linux/man-pages/man5/crontab.5.html

scrape responsibly, never scrape more than a couple times a week. This could
overload the server and get you blacklisted from the site!

Enjoy your daily structured data in the form of a JSON file, located in the project 
directory. 

# Future Plans
 
1. Make a web app for sending alerts if a player is 
	beginning a hit streak.  
2. Plot the stat history of each player.
