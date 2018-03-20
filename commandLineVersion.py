def predict(a):
	return "How are you?"


class Bot:
	"""The bot class"""
	isTraining = False
	learnDeliminater = "|"

	def setIsTraining(self, newBool):
		self.isTraining = newBool

	def setDeliminator(self, deliminator):
		self.learnDeliminater = deliminator

bot = Bot()

def init():
	isTraining = raw_input("Am I training? [True/False]:")
	isTraining = isTraining.lower() == "true"
	bot.setIsTraining(isTraining)
	newDeliminator = raw_input("Select a new deliminator. [Char]: ")
	bot.setDeliminator(newDeliminator)
	print("These are the current settings:")
	print("┌─────────────┬─────────────┐")
	print("│ isTraining  │       " + str(" " if bot.isTraining else "") +
	      str(bot.isTraining) + " │")
	print("├─────────────┼─────────────┤")
	print('│ deliminator │         "' + bot.learnDeliminater + '" │')
	print('└─────────────┴─────────────┘')


init()

while (True):
	test = raw_input("\nYou >>>")
	reply = predict(test)
	print("\nBot >>> " + reply)
