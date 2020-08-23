# Author:FeiBuCat

Feibucat =30
count =0
for i in range(3):
    guess = int(input("请输入数字： "))
    if  guess == Feibucat:
        print("恭喜你猜对了")
        break
    elif guess > Feibucat:
        print("猜大了。。")
    else:
        print("猜小了。。。")
    count +=1
else:
    print("次数超出限制。。。。")