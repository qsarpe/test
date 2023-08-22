import requests
import json
from colorama import Fore, Back, Style

def start():

    # IP address to test
    ip_address = input(Fore.CYAN + "\n[*] Enter the IP you would like to search: " + Fore.RED)


    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    print(result)
    Fore.RESET

    #nick is a dirty ass nigger you mother fucker