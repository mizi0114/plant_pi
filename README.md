# plant_pi
Telegram Bot, running on PI Zero 2 that takes a picture daily of my plants and sends them via TeleBot.

Equipment List:
- Raspberry Pi Zero 2
- Raspberry Pi Camera Module 3
- Some plants

![PXL_20250301_160030228](https://github.com/user-attachments/assets/b273e57b-d1ad-4171-8e33-2f5879c670a6)

Using Crontab to schedule each script. First, at 10:00 plantcam.py is ran, taking, then saving the image of the day with the corresponding date. 

Then, at 10:05, 'plantpi2.py' is ran, selecting, then sending the new picture to a Telegram channel of your choice.

![Untitled](https://github.com/user-attachments/assets/38230bd4-24f6-43bd-ae24-d8d07ab21918)
