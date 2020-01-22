class finalscreen:
	def __init__(self):
		self.looks = """          .--.
::\`--._,'.::.`._.--'/::::
::::.  ` __::__ '  .::::::
::::::-:.`'..`'.:-::::::::
::::::::\ `--' /::::::::::
------------------------------
___ _   _  ___ ___ ___  ___ ___ 
/ __| | | |/ __/ __/ _ \/ __/ __|
\__ \ |_| | (_| (_|  __/\__ \__ \

|___/\__,_|\___\___\___||___/___/
""".split("\n")

	def printit(self):
		print("\033[40m\033[32m")
		for i in range(len(self.looks)):
			for j in range(len(self.looks[i])):
				print(self.looks[i][j],end='')
			print()
		print('\033[0m')