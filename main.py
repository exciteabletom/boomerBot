import amanobot
from amanobot.loop import MessageLoop

from private import prodToken, devToken

import time

boomerWords = (
	"millennial", "liberal", "milennial", "these days", "kids these days", "back in", "in my day",
	"when i was young", "we used to", "we never", "snowflake", "lazy", "entitled", "use our imagination",
	"damn kids", "out of hand", "gone too far", "gone to far", "the war", "the depression", "aoc", "trump",
	"stupid kids", "stop complaining", "republican", "trump", "bernie", "biden", "clinton", "conservative",
	"liberal" "politics", "out of hand", ":))", ":((", "@okboomer_bot", "get over it", "not that bad",
	"maga", "pence",
)


def main_loop(msg):
	contentType, chatType, chatId = amanobot.glance(msg)

	if contentType == "text":
		msgText = msg["text"].lower()
		for boomerWord in boomerWords:
			if boomerWord in msgText:
				message = f"Ok, Boomer.\n\nTriggered by the phrase '{boomerWord}'"
				bot.sendMessage(chatId, message)
				break 

bot = amanobot.Bot(prodToken)

MessageLoop(bot, main_loop).run_as_thread()  # constantly checks for new messages, if new message call main_loop()

while True:
	time.sleep(1)
