
# module imports
import os
import requests
from bs4 import BeautifulSoup
import time

# get codes from website
url = requests.get('https://nukacrypt.com/codes.json?r=')
txt = BeautifulSoup(url.text, 'html.parser')

# make the text from website into strings and form codes
site_alpha = str(txt)[10:18]
site_bravo = str(txt)[29:37]
site_charlie = str(txt)[50:58]

# print the codes
print("Site Alpha Code: " + site_alpha)
print("Site Bravo Code: " + site_bravo)
print("Site Charlie Code: " + site_charlie)

# credits
time.sleep(5)
print("Made by PUFFER (https://www.nigol.ee/)")
print("Enclave Database: https://www.enclavedb.net/")
print("NukaCrypt: https://nukacrypt.com/")
# prevent exe file from closing
time.sleep(1)
answer = input("Do you want to exit? (y/n): ").lower()
if answer == "y":
    exit()
elif answer == "n":
    print("Okay. CMD will stay open.")
    os.system("pause")
else:
    print("Oopsie. Your input was wrong. Closing program in 5 seconds.")
    time.sleep(5)
    exit()


