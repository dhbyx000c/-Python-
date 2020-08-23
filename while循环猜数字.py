# Author:FeiBuCat

Feibucat =30
count =0
while count <3:
    guess = int(input("请输入数字： "))
    if guess == Feibucat:
        print("恭喜你答对了～！")
        break
    elif guess > Feibucat:
        print("猜大了。。。")
    else:
        print("猜小了。。。")
    count +=1
    if count ==3:
        continue_confirm = input("游戏是否继续？")
        if continue_confirm !='n':
            count =0



