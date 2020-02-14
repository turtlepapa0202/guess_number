# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話，印出"終於猜對了！"
# 猜錯的話，要告訴他，比答案大/小

import random
number = random.randint(1, 100)

while True:
	guess_num = input('請猜1~100的數字: ')
	guess_num = int(guess_num)
	if guess_num == number:
		print('終於猜對了！')
		break
	elif guess_num > number:
		print('比答案大')
	elif guess_num < number:
		print('比答案小')
