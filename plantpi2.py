import telebot
from telebot.types import InputFile
import time
import os
from datetime import datetime, timedelta
import shutil

#bot token from Telegram
bot = telebot.TeleBot(token="<YOUR TELEGRAM TOKEN>")

#selects current days picture variables
plantpic_folder = "<YOUR DIRECTORY PATH HERE>"
file_prefix = "plantpic_"
date_now = datetime.now()
date_str = date_now.strftime("%Y-%m-%d")
file_extension = ".jpg"

todays_file = f"{plantpic_folder}{file_prefix}{date_str}{file_extension}" 

#test image variable to use before using plantcam.py 
#image = "<YOUR DIRECTORY PATH HERE>/<YOUR TEST IMAGE>.jpg"
        
#send picture function 
def send_plant_pic():
    #print(f"New picture found: {todays_file}")
    bot.send_document(
    "<YOUR CHAT ID>",
    InputFile(todays_file)
    )

send_plant_pic()