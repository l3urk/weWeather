import sys
import os
import argparse
import platform
import requests
import time
import datetime
import re
from pytz import timezone 
from timezonefinder import TimezoneFinder
import pyfiglet
from simple_chalk import chalk

if(platform.system() == "Linux"):
    os.system('clear')
if(platform.system() == "Windows"):
    os.system('cls')

ascii_art=r'''
                 __      __               __  .__                  
  __  _  __ ____/  \    /  \ ____ _____ _/  |_|  |__   ___________ 
  \ \/ \/ // __ \   \/\/   // __ \\__  \\   __\  |  \_/ __ \_  __ \
   \     /\  ___/\        /\  ___/ / __ \|  | |   Y  \  ___/|  | \/
    \/\_/  \___  >\__/\  /  \___  >____  /__| |___|  /\___  >__|   
               \/      \/       \/     \/          \/     \/       
'''
author_sign="""
    For Finding Weather Condition.
    @author  - leurk
    @version - 1.0
"""
print(chalk.blue(ascii_art))
print(chalk.red(author_sign))

try:
    api_key = "598a65c54ec48d30c8ecd97a1b60fc25"
    def_url = "http://api.openweathermap.org/data/2.5/weather"
    current_time = datetime.datetime.now()
    pattern = r'^[+-]?\d+(\.\d+)?$'
    user_input=0
    fav_file="weWeather_fav-list.txt"
    printing_control=0

    parser_arg=argparse.ArgumentParser(description='Arguments for weather api')
    parser_arg.add_argument('-search',type=str,help='Search Argument')
    parser_arg.add_argument('--fav',action='store_true',help='for adding in favourite list')
    args=parser_arg.parse_args()
    
    def cal_time(latitude,longitude):
        tf=TimezoneFinder()
        tz_finds=tf.timezone_at(lat=latitude,lng=longitude)
        target_timezone=timezone(tz_finds)
        searched_current_time=datetime.datetime.now(target_timezone)
        return searched_current_time

    def loc_desc(loc):
        url=f"{def_url}?q={loc}&appid={api_key}&units=metric"
        while True:
            if printing_control == 0:
                if platform.system() == "Linux":
                    os.system("clear")
                if platform.system() == "Windows":
                    os.system("cls")

            response=requests.get(url)
            if response.status_code == 200:
                data=response.json()
                print_name=data['name']
                loc_lat=data['coord']['lat']
                loc_lon=data['coord']['lon']
                time_current=cal_time(loc_lat,loc_lon)
                formatted_date=time_current.strftime("%d-%m-%Y")
                formatted_time=time_current.strftime("%H:%M:%S")
                current_weather=data['weather'][0]['main']
                weather_des=data['weather'][0]['description']
                current_temp=data['main']['temp']
                temp_feels=data['main']['feels_like']
                current_humidity=data['main']['humidity']
                print(chalk.blue(pyfiglet.figlet_format(f"   {print_name}")))
                print(f"Date\t\t- {formatted_date}")
                print(f"Time\t\t- {formatted_time}")
                print(f"Weather\t\t- {current_weather}")
                print(f"Description\t- {weather_des}")
                print(f"Temperature\t- {current_temp} [in degree celcius]")
                print(f"Feels Like\t- {temp_feels} [in degree celcius]")
                print(f"Humidity\t- {current_humidity}")
                if printing_control == 1:
                    break
                time.sleep(10)
            else:
                print(chalk.red(f"\n[!] weWeather Cannot Seem to Find Information on {loc}."))
                sys.exit()

    def coordinate_desc(temp_lat,temp_lon):
        url=f"{def_url}?lat={temp_lat}&lon={temp_lon}&appid={api_key}&units=metric"
        while True:
            if platform.system() == "Linux":
                os.system("clear")
            if platform.system() == "Windows":
                os.system("cls")

            response=requests.get(url)
            if response.status_code == 200:
                data=response.json()
                print_name=data['name']
                temp_lat=data['coord']['lat']
                temp_lon=data['coord']['lon']
                time_current=cal_time(temp_lat,temp_lon)
                formatted_date=time_current.strftime("%d-%m-%Y")
                formatted_time=time_current.strftime("%H:%M:%S")
                current_weather=data['weather'][0]['main']
                weather_des=data['weather'][0]['description']
                current_temp=data['main']['temp']
                temp_feels=data['main']['feels_like']
                current_humidity=data['main']['humidity']
                print(chalk.blue(pyfiglet.figlet_format(f"   {print_name}")))
                print(f"Date\t\t- {formatted_date}")
                print(f"Time\t\t- {formatted_time}")
                print(f"Weather\t\t- {current_weather}")
                print(f"Description\t- {weather_des}")
                print(f"Temperature\t- {current_temp} [in degree celcius]")
                print(f"Feels Like\t- {temp_feels} [in degree celcius]")
                print(f"Humidity\t- {current_humidity}")
                time.sleep(10)
            else:
                print(chalk.red(f"\n[!] weWeather Cannot Seem to Find Information For these Coordinates."))
                sys.exit()

    def weweather_menu():
        print("\nweWeather Menu :-")
        print(f"{chalk.green([1])} Search By Name")
        print(f"{chalk.green([2])} Search By Pincode")
        print(f"{chalk.green([3])} Search By Latitude And Longitude")
        print(f"{chalk.green([4])} My Favourites")

    if args.search:
        if args.fav:
            with open(fav_file,'a') as fav_list:
                fav_list.write(args.search+"\n")
        loc_desc(args.search)
    else:
        turns=0
        while True:
            if turns>0:
                if platform.system() == "Linux":
                    os.system("clear")
                    print(chalk.blue(ascii_art))
                    print(chalk.red(author_sign))
                if platform.system() == "Windows":
                    os.system("cls")
                    print(chalk.blue(ascii_art))
                    print(chalk.red(author_sign))

            weweather_menu()
            user_input=input(chalk.green("\n[=] "))

            if user_input=='1':
                input_name=input(chalk.green("[=] Enter the Name - "))
                if re.match(pattern,input_name):
                    print(chalk.red("\n[!] Enter the Name Correctly."))
                else:
                    loc_desc(input_name)

            if user_input=='2':
                input_pincode=input(chalk.green("[=] Enter the Pincode - "))
                if input_pincode.isdigit():
                    loc_desc(input_pincode)
                else:
                    print(chalk.red("\n[!] Enter the Pincode Correctly"))
        
            if user_input=='3':
                lat=input(chalk.green("[=] Enter Latitude = "))
                lon=input(chalk.green("[=] Enter Longitude = "))
                if (re.match(pattern,lat)) and (re.match(pattern,lon)):
                    coordinate_desc(lat,lon)
                else:
                    print(chalk.red("\n[!] Enter the Latitude and Longitude Correctly"))

            if user_input=='4':
                print("\nFavourite List Menu:-")
                print(f"{chalk.green([1])} Weather Of Favourite List")
                print(f"{chalk.green([2])} List Favourite List")
                print(f"{chalk.green([3])} Add In Favourite List")
                print(f"{chalk.green([4])} Clear Favourite List")
                fav_choice=input(chalk.green("\n[=] "))
                if fav_choice == '1':
                    printing_control=1
                    try:
                        with open(fav_file,'r') as fav_list:
                            for each_item in fav_list:
                                each_item=each_item.strip()
                                loc_desc(each_item)
                    except FileNotFoundError:
                        with open(fav_file,'w'):
                            pass
                    sys.exit()
        
                if fav_choice == '2':
                    try:
                        with open(fav_file,'r') as fav_list:
                            for each_item in fav_list:
                                print(each_item,end='')
                    except FileNotFoundError:
                        with open(fav_file,'w'):
                            pass
                    sys.exit()

                if fav_choice == '3':
                    fav_add=input("\nWhat to Add - ")
                    with open(fav_file,'a') as fav_list:
                        fav_list.write(fav_add+"\n")
                    print(chalk.green(f"\n[+] {fav_add} Got Added To the weWeather Favourite List Successfully"))
                    time.sleep(2)

                if fav_choice == '4':
                    with open(fav_file,'w') as fav_list:
                        pass
                    print(chalk.green("\n[!] The weWeather Favorite List Cleared Successfully"))
                    time.sleep(2)

            turns+=1

except Exception as e:
    print(chalk.red(f"\n[!] Error - {e}"))

except KeyboardInterrupt:
    print(chalk.red("\n[!] Exiting From the Script .."))
    time.sleep(0.5)
