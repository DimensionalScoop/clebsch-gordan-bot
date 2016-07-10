import telepot
import time
import os
import sys
import numpy


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, 'Theva ist ein Genie.')


bot = telepot.Bot('246042888:AAFmv3oelFG3gVnAYeFo5E7r1QAsJyTZsj0')
bot.message_loop(handle)

while 1:
    time.sleep(10)
