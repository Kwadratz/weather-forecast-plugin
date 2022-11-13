import os, requests, webbrowser
from colorama import Fore as col
from colorama import Style as r

global ver
global defcity
global apicurrent
global callsleft4today
api_current = "d678da607587d9c44127fba2d037162a"
ver = "1.0.0"

os.system(f"title Weather Forecast {ver} for PowerPrompt")

def menu():
    print(f"{col.CYAN}Weather Forecast {ver}{r.RESET_ALL}\n{col.LIGHTBLACK_EX}a PowerPrompt plugin, made by {r.RESET_ALL}{col.WHITE}Kwadratz\n")
    match input(f"{col.LIGHTBLACK_EX}What do you want to do?\n"+f"""
    {r.RESET_ALL}{col.CYAN}1. Check current weather
    {r.RESET_ALL}{col.YELLOW}2. Check daily forecast
    {r.RESET_ALL}{col.GREEN}3. Plugin settings
    {r.RESET_ALL}{col.RED}4. Exit to PowerPrompt
    """+f"\n{r.RESET_ALL}{col.LIGHTBLACK_EX}Select an option... >{r.RESET_ALL}{col.WHITE} "):
        case "1":
            current()
        case "2":
            daily()
        case "3":
            settingsmenu()
        case other:
            quit() #CHANGE IT
            exitunsure()

def current():
    os.system("cls")
    city = input("Enter city name (if default, leave blank) > ")
    if city == "":
        city = defcity
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_current}")
    prom = req.json() #u know, like promise

    temp = str(round(prom["main"]["temp"] - 273, 1))
    tempfl = str(round(prom["main"]["feels_like"] - 273, 1))
    clouds = prom["clouds"]["all"]
    
    # TO DO:
    # if for clouds, checking its value from 0 to 101
    #
    #
    #
    #

    print(f"Here's your weather data for {city}:"+f"""
    Temperature: {temp}*C (feels like {tempfl}*C)
    chmurki
    """)

menu()