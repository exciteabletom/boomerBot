import telepot  # telegram bot lib
from telepot.loop import MessageLoop  # loop to check for messages

from private import prodToken, devToken

import time

boomerWords = ["millennial", "liberal", "milennial", "these days", "kids these days", "back in","in my day", "when i was young", "we used to", "we never", "snowflake", "lazy",
               "entitled", "use our imagination", "damn kids", "out of hand", "gone too far", "gone to far", "the war", "the depression", "aoc", "trump", "stupid kids",
               "stop complaining", "republican", "trump", "bernie", "biden", "clinton", "conservative", "liberal" "politics", "out of hand",":))", ":((", "@OkBoomer_Bot",
			   "get over it", "it's not that bad", "its not that bad"]

def main_loop(msg):
    contentType, chatType, chatId = telepot.glance(msg)

    if contentType == "text":
        msgText = msg["text"].lower()  # message sent converted to lower case

        for word in boomerWords:  # loop through array of boomer words
            if word in msgText:  # if a boomer word is in the message
                message = f"Ok, Boomer.\n\nTriggered by the phrase '{word}'" 
                bot.sendMessage(chatId, message)  # send epic ok boomer roast
                break  # if roast is sent stop loop



bot = telepot.Bot(prodToken)

MessageLoop(bot, main_loop).run_as_thread()  # constantly checks for new messages, if new message call main_loop()

while True:  # keeps program alive
    time.sleep(10)
