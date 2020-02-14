# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話，印出"終於猜對了！"
# 猜錯的話，要告訴他，比答案大/小
# bonus：邊猜邊顯示猜了第幾次

import random
a = input('請決定隨機數字範圍開始值: ')
a = int(a)
b = input('請決定隨機數字範圍結束值: ')
b = int(b)
number = random.randint(a, b)
x = 1
while True:
	guess_num = input('請猜範圍內數字: ')
	guess_num = int(guess_num)
	if guess_num == number:
		if x == 1:
			print('厲害，一次就猜對！')
		else:
			print('終於猜對了！')
			print('總共猜了', x, '次')
		break
	elif guess_num > number:
		print('比答案大')
	elif guess_num < number:
		print('比答案小')
	
	print('目前猜了', x, '次')
	print('')
	x += 1
	
