# for i in range (1,100):
# if(i%2 == 0):
# print(i)
# name = input("Enter your name: ")
# good_credit = True
# criminal_record = True
# if good_credit and criminal_record:
# print('You are eligible for loan')
# else:
#  print("You are not")
# temperatue = int(input("Enter today's Temperature: "))
# if(temperatue>=30):
# print("It's hot day")
# elif(temperatue<=10):
# print("It's cold day")
# else:
# print("Neither hot nor cold")
# Checking Character:
# name = input('Enter your name: ')
# if len(name) < 3:
# print('Your name must be atleast 3 characters long')
# elif len(name) > 50:
# print('Your name should be maximum 50 characters long')
# else:
#   print("Name looks good!")
# Weight Converter:
# weight = int(input('Enter weight: '))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == 'L':
#     converted = weight*0.45
#     print(f"Weight is {converted} Kilograms")
# else:
#     converted = weight//0.45
#     print(f"weight is{converted} pounds")
# number = 4
# while number<=5:
#    print(number)
#    number+=1
# print('Done')
sentence = input('Enter sentence ')
words_count = {}

for n in sentence:
    keys = words_count.keys()
    if n in keys:
        words_count[n] += 1
    else:
        words_count[n] = 1
print(words_count)
