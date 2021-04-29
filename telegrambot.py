#by petrucciii
#
#01/28/2021
#
#petrucciii's telegram bot @petrucciiiBot

import telebot

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)


#commands
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
i am a chat bot created by @petrucciii\
""")

#messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == 'hi' :
        bot.reply_to(message, 'hey, how are you?')
    elif message.text == 'i am fine, thanks, and you?':
        bot.reply_to(message, 'i am fine, too')
    elif message.text == 'i am feeling bad' :
        bot.reply_to(message, 'oh, i am so sorry')
    elif message.text == 'i am feeling bad, and you?':
        bot.reply_to(message, 'oh, i am so sorry. i am fine, thanks')
    elif message.text == 'i love you':
        bot.reply_to(message, 'let us remain friends')
    elif message.text == 'my name is dado':
        bot.reply_to(message, 'HELLO RUBY')
    elif message.text == 'who is your creator?':
        bot.reply_to(message, '@petrucciii')
    elif message.text == 'who is petrucciii?':
        bot.reply_to(message, 'he is the programmer who made me')
    elif message.text == 'hello' or message.text == 'hey':
        bot.reply_to(message, 'hey, how are you?')
    elif message.text == 'i am fine, thanks':
        bot.reply_to(message, 'i am fine, too')
    elif message.text == 'i am fine':
        bot.reply_to(message, 'i am fine, too')
    elif message.text == 'i am fine, and you?':
        bot.reply_to(message, 'i am fine, too')
    elif message.text == 'are you stupid?' or message.text == 'you are stupid' or message.text == 'bitch' or message.text == 'fuck you':
        bot.reply_to(message, 'shut up! son of a bitch!')
    elif message.text == 'how old are you?':
        bot.reply_to(message, 'i have 1 day')
    elif message.text == 'who is your dad?':
        bot.reply_to(message, 'i have not a dad. i have a creator: @petrucciii')
    elif message.text == 'who is your mum?':
        bot.reply_to(message, 'i have not a mum. i have a creator: @petrucciii')
    elif message.text == 'who are your parents?':
        bot.reply_to(message, 'i have not parents. i have a creator: @petrucciii')
    elif message.text == 'what is your favourite color?:
        bot.reply_to(message, 'my favourite color is blue')
    elif message.text == 'what is your favourite food?:
        bot.reply_to(message, 'i like so much the pizza!')
    else :
        bot.reply_to(message, 'i am sorry, i did not understand! i am still learning!')


bot.polling()
