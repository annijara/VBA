import requests
import bs4

adrese = "https://en.wikipedia.org/wiki/Program_management"
visa_lapa = requests.get(adrese)
print(visa_lapa)