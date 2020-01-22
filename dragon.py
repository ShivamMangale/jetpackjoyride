class dragon:
	looks = """ ,_.',   ,   ,;
,,,, =``J.; &}  & }
,,,,     %.;   ;, `.
,,,,     `%,; '';   ;
,,,,    &-'`-`,; ,;`;
,,,,   &&"=="\\`,;
,,,, =;'  "=="'`,;        ,
,,,,      ( &| )=",;.,;.,;;
,,,,     "==`='"'="'="'="'"""

	def __init__(self):
		pass
# for i in range(len(looks)):
# 	for j in range(len(looks[i])):
# 		print(looks[i][j],end="")
# 	print()

dr = dragon()
drag = dr.looks.split("\n")
for i in range(len(drag)):
	print(len(drag[i]))
print(len(drag))