country = input('請問你來自哪個國家： ')
age = input('你今年幾歲： ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('恭喜！你可以考駕照囉')
	else:
		print('還不能考駕照')
elif country == '美國':
	if age >= 16:
		print('恭喜！你可以考駕照囉')
	else:
		print('還不能考駕照')