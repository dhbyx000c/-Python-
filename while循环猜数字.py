# Author:FeiBuCat

'''for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j,i,i*j),end='')
    print()
'''

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



