import main
import telebot
import time
import schedule
import requests

bot = telebot.TeleBot("TOKEN")

def daily_report():
	send_text = str(main.get_data())
	response = requests.get(send_text)
	return response.json()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['data'])
def send_data(message):	
	bot.reply_to(message, str(main.get_data()))


bot.infinity_polling()


schedule.every().day.at("10:25").do(daily_report)

while True:
    schedule.run_pending()
    time.sleep(1)
