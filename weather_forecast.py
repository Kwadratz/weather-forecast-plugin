import os, requests, webbrowser, datetime, pickle
from colorama import Fore as col
from colorama import Style as r

global ver
global defcity
global callsleft4today

api_current = pickle.load(open("settings/apiKey.", "rb"))
defcity = pickle.load(open("settings/defCityLocation.", "rb"))

isDay = datetime.datetime.now()
isDay = isDay.strftime("%H")
isDay = int(isDay)
if isDay >= 7 and isDay < 19: isDay = True
else: isDay = False
ver = "1.0.0"
cloud_emoji = {
    "dClear": "☀️ Sky's Clear",
    "dLow": "🌤️ Few Clouds",
    "dSome": "⛅ Partly Cloudy",
    "dMostly": "🌥️ Mostly Cloudy",
    "dAll": "☁️ All Clouds",
    "nClear": "🌙 Partly Cloudy",
    "nAll": "☁️ Mostly Cloudy"
}
noData = "❌ No Data"

os.system(f"title Weather Forecast {ver} for PowerPrompt")

def menu():
    os.system("cls")
    print(f"{col.CYAN}Weather Forecast {ver}{r.RESET_ALL}\n{col.LIGHTBLACK_EX}a PowerPrompt plugin, made by {r.RESET_ALL}{col.WHITE}Kwadratz\n")
    match input(f"{col.LIGHTBLACK_EX}What do you want to do?\n"+f"""
    {r.RESET_ALL}{col.CYAN}1. Check current weather
    {r.RESET_ALL}{col.YELLOW}2. Check daily forecast
    {r.RESET_ALL}{col.GREEN}3. Plugin settings
    {r.RESET_ALL}{col.RED}4. Exit to PowerPrompt
    """+f"\n{r.RESET_ALL}{col.LIGHTBLACK_EX}Select an option... >{r.RESET_ALL}{col.WHITE} "):
        case "1": current()
        case "2": daily()
        case "3": settingsmenu()
        case other:
            quit() #CHANGE IT
            exitunsure()

def current():
    os.system("cls")
    city = input(f"{col.LIGHTBLACK_EX}Enter city name (if default, leave blank) > {r.RESET_ALL}{col.WHITE}")
    os.system("cls")
    if city == "":
        city = defcity
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_current}")
    prom = req.json() #u know, like promise

    city = city+f", {prom['sys']['country']}"
    temp = str(round(prom["main"]["temp"] - 273, 1))
    tempfl = str(round(prom["main"]["feels_like"] - 273, 1))
    clouds = prom["clouds"]["all"]
    cloudsprc = clouds
    wind = {
        "deg": prom["wind"]["deg"],
        "spd": prom["wind"]["speed"]
    }
    airpress = prom["main"]["pressure"]
    visibility = prom["visibility"]
    sun = {
        "rise": datetime.datetime.fromtimestamp(prom["sys"]["sunrise"]),
        "set": datetime.datetime.fromtimestamp(prom["sys"]["sunset"])
    }

    if isDay:
        if clouds >= 0 and clouds <= 9:
            clouds = cloud_emoji["dClear"]
        elif clouds >= 10 and clouds <= 29:
            clouds = cloud_emoji["dLow"]
        elif clouds >= 30 and clouds <= 59:
            clouds = cloud_emoji["dSome"]
        elif clouds >= 60 and clouds <= 89:
            clouds = cloud_emoji["dMostly"]
        elif clouds >= 90 and clouds <= 100:
            clouds = cloud_emoji["dAll"]
        else:
            clouds = noData
    else:
        if clouds >= 0 and clouds <= 9:
            clouds = cloud_emoji["dClear"]
        elif clouds >= 10 and clouds <= 29:
            clouds = cloud_emoji["dLow"]
        else:
            clouds = noData
    
    if wind["deg"] >= 0 and wind["deg"] <= 45:
        wind["deg"] = "⬆️"
    elif wind["deg"] >= 46 and wind["deg"] <= 89:
        wind["deg"] = "↗️"
    elif wind["deg"] >= 90 and wind["deg"] <= 135:
        wind["deg"] = "➡️"
    elif wind["deg"] >= 136 and wind["deg"] <= 179:
        wind["deg"] = "↘️"
    elif wind["deg"] >= 180 and wind["deg"] <= 225:
        wind["deg"] = "⬇️"
    elif wind["deg"] >= 226 and wind["deg"] <= 269:
        wind["deg"] = "↙️"
    elif wind["deg"] >= 270 and wind["deg"] <= 315:
        wind["deg"] = "⬅️"
    elif wind["deg"] >= 316 and wind["deg"] <= 360:
        wind["deg"] = "↖️"

    print(f"{col.LIGHTBLACK_EX}Here's your current weather data for {col.WHITE}{city}:"+f"""
    
    {r.RESET_ALL}{col.CYAN}Temperature: {r.RESET_ALL}{col.LIGHTBLUE_EX}{temp}*C {r.RESET_ALL}{col.LIGHTBLACK_EX}(feels like {tempfl}*C)
    {r.RESET_ALL}{col.YELLOW}Cloudiness: {r.RESET_ALL}{col.LIGHTYELLOW_EX}{clouds} {r.RESET_ALL}{col.LIGHTBLACK_EX}({cloudsprc}%)
    {r.RESET_ALL}{col.RED}Wind: {r.RESET_ALL}{col.LIGHTRED_EX}{round(wind["spd"]*3.6, 1)} km/h, {wind['deg']}
    {r.RESET_ALL}{col.GREEN}Air Pressure: {r.RESET_ALL}{col.LIGHTGREEN_EX}{airpress} hPa
    {r.RESET_ALL}{col.MAGENTA}Visibility: {r.RESET_ALL}{col.LIGHTMAGENTA_EX}{visibility} m {r.RESET_ALL}{col.LIGHTBLACK_EX}({visibility/1000} km)

    {r.RESET_ALL}{col.LIGHTBLACK_EX}Sunrise today: {col.YELLOW}{sun["rise"]}
    {r.RESET_ALL}{col.LIGHTBLACK_EX}Sunset today: {col.WHITE}{sun["set"]}
    """)
    input(f"{col.LIGHTBLACK_EX}Click {col.RED}ENTER {col.LIGHTBLACK_EX}to go back to the main menu.")
    menu()

def daily():
    os.system("cls")
    city = input(f"{col.LIGHTBLACK_EX}Enter city name (if default, leave blank) > {r.RESET_ALL}{col.WHITE}")
    os.system("cls")
    if city == "":
        city = defcity
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_current}")
    prom = req.json() #u know, like promise

    city = city+f", {prom['sys']['country']}"
    temp = str(round(prom["main"]["temp"] - 273, 1))
    tempfl = str(round(prom["main"]["feels_like"] - 273, 1))
    clouds = prom["clouds"]["all"]
    cloudsprc = clouds
    wind = {
        "deg": prom["wind"]["deg"],
        "spd": prom["wind"]["speed"]
    }
    airpress = prom["main"]["pressure"]
    visibility = prom["visibility"]
    sun = {
        "rise": datetime.datetime.fromtimestamp(prom["sys"]["sunrise"]),
        "set": datetime.datetime.fromtimestamp(prom["sys"]["sunset"])
    }

    if isDay:
        if clouds >= 0 and clouds <= 9:
            clouds = cloud_emoji["dClear"]
        elif clouds >= 10 and clouds <= 29:
            clouds = cloud_emoji["dLow"]
        elif clouds >= 30 and clouds <= 59:
            clouds = cloud_emoji["dSome"]
        elif clouds >= 60 and clouds <= 89:
            clouds = cloud_emoji["dMostly"]
        elif clouds >= 90 and clouds <= 100:
            clouds = cloud_emoji["dAll"]
        else:
            clouds = noData
    else:
        if clouds >= 0 and clouds <= 9:
            clouds = cloud_emoji["dClear"]
        elif clouds >= 10 and clouds <= 29:
            clouds = cloud_emoji["dLow"]
        else:
            clouds = noData
    
    if wind["deg"] >= 0 and wind["deg"] <= 45:
        wind["deg"] = "⬆️"
    elif wind["deg"] >= 46 and wind["deg"] <= 89:
        wind["deg"] = "↗️"
    elif wind["deg"] >= 90 and wind["deg"] <= 135:
        wind["deg"] = "➡️"
    elif wind["deg"] >= 136 and wind["deg"] <= 179:
        wind["deg"] = "↘️"
    elif wind["deg"] >= 180 and wind["deg"] <= 225:
        wind["deg"] = "⬇️"
    elif wind["deg"] >= 226 and wind["deg"] <= 269:
        wind["deg"] = "↙️"
    elif wind["deg"] >= 270 and wind["deg"] <= 315:
        wind["deg"] = "⬅️"
    elif wind["deg"] >= 316 and wind["deg"] <= 360:
        wind["deg"] = "↖️"

    print(f"{col.LIGHTBLACK_EX}Here's your current weather data for {col.WHITE}{city}:"+f"""
    
    {r.RESET_ALL}{col.CYAN}Temperature: {r.RESET_ALL}{col.LIGHTBLUE_EX}{temp}*C {r.RESET_ALL}{col.LIGHTBLACK_EX}(feels like {tempfl}*C)
    {r.RESET_ALL}{col.YELLOW}Cloudiness: {r.RESET_ALL}{col.LIGHTYELLOW_EX}{clouds} {r.RESET_ALL}{col.LIGHTBLACK_EX}({cloudsprc}%)
    {r.RESET_ALL}{col.RED}Wind: {r.RESET_ALL}{col.LIGHTRED_EX}{round(wind["spd"]*3.6, 1)} km/h, {wind['deg']}
    {r.RESET_ALL}{col.GREEN}Air Pressure: {r.RESET_ALL}{col.LIGHTGREEN_EX}{airpress} hPa
    {r.RESET_ALL}{col.MAGENTA}Visibility: {r.RESET_ALL}{col.LIGHTMAGENTA_EX}{visibility} m {r.RESET_ALL}{col.LIGHTBLACK_EX}({visibility/1000} km)

    {r.RESET_ALL}{col.LIGHTBLACK_EX}Sunrise today: {col.YELLOW}{sun["rise"]}
    {r.RESET_ALL}{col.LIGHTBLACK_EX}Sunset today: {col.WHITE}{sun["set"]}
    """)
    input(f"{col.LIGHTBLACK_EX}Click {col.RED}ENTER {col.LIGHTBLACK_EX}to go back to the main menu.")
    menu()


    # api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_current}
    # TO DO
    # add "day" variable and scrolling through days
    # yeah
    #
    #
    #

menu()