import random
restart2=True
while restart2==True:
    n=random.randint(0,50)  #range of numbers to choose a random number from
    check=-1
    score=11
    restart1=True
    while restart1==True:
        check+=1
        score-=1
        m=int(input('Guess the number: '))
        if m==n:
            print('YOU WIN!')
            print('Your Score: ',score,'/10')
            r=input('Play Again?(Y/N)')
            if r not in ['Y','y']:
                restart=False
        elif check==0:
            print('Try Again')
            if n%2==0:
              j='It is an even number'
            else:
                j='It is an odd number'
            print('HINT: ', j)
        elif check==2:
            print('Try Again')
            if n in range(0,10):
                j='It is a single digit number'
            else:
                j='It is a two digit number'
            print('HINT: ',j)
        elif check==4:
            print('Try Again')
            if n<25:
                j='It is less than 25'
            else:
                j='it is greater than or equal to 25'
            print('HINT: ',j)
        elif check==6:
            if n%5==0:
                j='it is a multiple of 5'
            else:
                j='it is not a multiple of 5'
            print('HINT: ',j)
        elif check==8:
            if n>m:
                j='no it is greater than that'
            else:
                j='no it is less than that'
            print('HINT: ',j)
        elif check==9:
            print('GAME OVER!')
            print('The Number Was: ',n)
            r=input('Play Again?(Y/N)')
            if r not in ['Y','y']:
                restart1=False
                restart2=False
            else:
                restart1=False
        else:
            pass
