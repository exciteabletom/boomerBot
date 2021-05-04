import amanobot  # telegram bot lib
from amanobot.loop import MessageLoop  # loop to check for messages

from private import prodToken, devToken

import time

boomerWords = (
	"millennial", "liberal", "milennial", "these days", "kids these days", "back in", "in my day",
	"when i was young", "we used to", "we never", "snowflake", "lazy", "entitled", "use our imagination",
	"damn kids", "out of hand", "gone too far", "gone to far", "the war", "the depression", "aoc", "trump",
	"stupid kids", "stop complaining", "republican", "trump", "bernie", "biden", "clinton", "conservative",
	"liberal" "politics", "out of hand", ":))", ":((", "@okboomer_bot", "get over it", "not that bad",
	"not that bad", "maga", "pence",
)


def main_loop(msg):
	contentType, chatType, chatId = amanobot.glance(msg)

	if contentType == "text":
		msgText = msg["text"].lower()  # message sent converted to lower case

		for boomerWord in boomerWords:  # loop through array of boomer words
			for msgWord in msgText.split(" "):
				if msgWord == boomerWord:  # if a boomer word is in the message
					message = f"Ok, Boomer.\n\nTriggered by the phrase '{boomerWord}'"
					bot.sendMessage(chatId, message)  # send epic ok boomer roast
					break  # if roast is sent stop loop


bot = amanobot.Bot(prodToken)

MessageLoop(bot, main_loop).run_as_thread()  # constantly checks for new messages, if new message call main_loop()

while True:  # keeps program alive
	time.sleep(10)
