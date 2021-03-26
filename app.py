import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup as s
import os
import re
os.system('clear')




headers = {
     

         'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Language':'ar,en-US;q=0.7,en;q=0.3',
         
}

bot = telebot.TeleBot("token")



@bot.message_handler(commands=['start'])
def welcome_help(message):
    bot.send_message(message.chat.id, ' مطور بوت @AliS219')
        
    


@bot.message_handler(content_types=['text'])
def send_document(message):
    if message.chat.type == 'supergroup':
      if message.text.startswith("https://www.bartleby.com/questions-and-answers"):
            #bot.send_message(message.chat.id, 'سوف يتم ارسال الحل قريبا ',reply_to_message_id=message.message_id)
            r = requests.get(message.text, headers=headers)
            soup = s(r.content,'html.parser')
            x0=soup.find('h3')
            print(x0.text)
            if "This question hasn't been answered yet." in x0.text :
                print("no anser")
                bot.send_message(message.chat.id, 'لم يتم حل سوال ...تحقق من رابط ', reply_to_message_id=message.message_id)
            elif "Don't worry! We won't leave you hanging. Plus, we're giving you back one question for the inconvenience." in x0.text :
                print("out ans")
                bot.send_message(message.chat.id, 'تم حذف سوالك من قبل موقع ...تحقق من رابط ', reply_to_message_id=message.message_id)
            else:
                print(" Anser")



            
            
            




bot.polling(none_stop=True)








