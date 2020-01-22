class finalscreen:
	def __init__(self):
		self.looks = """          .--.
::\`--._,'.::.`._.--'/::::
::::.  ` __::__ '  .::::::
::::::-:.`'..`'.:-::::::::
::::::::\ `--' /::::::::::
------------------------------
,adPPYba, 88       88  ,adPPYba,  ,adPPYba,  ,adPPYba, ,adPPYba, ,adPPYba,  
I8[    "" 88       88 a8"     "" a8"     "" a8P_____88 I8[    "" I8[    ""  
 `"Y8ba,  88       88 8b         8b         8PP"""""""  `"Y8ba,   `"Y8ba,   
aa    ]8I "8a,   ,a88 "8a,   ,aa "8a,   ,aa "8b,   ,aa aa    ]8I aa    ]8I  
`"YbbdP"'  `"YbbdP'Y8  `"Ybbd8"'  `"Ybbd8"'  `"Ybbd8"' `"YbbdP"' `"YbbdP"'
""".split("\n")

	def printit(self):
		print("\033[40m\033[32m")
		for i in range(len(self.looks)):
			for j in range(len(self.looks[i])):
				print(self.looks[i][j],end='')
			print()
		print('\033[0m')