def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += (len(string)-i)
        else:
            stuart += (len(string)-i)

    if kevin > stuart:
        print ("Kevin", kevin)
    elif kevin < stuart:
        print ("Stuart", stuart)
    else:
        print ("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
    
# CONCEPT:
""" 
For BANANA
B        1
N        2
BA       1
NA       2
BAN      1
NAN      1
BANA     1
NANA     1
BANAN    1
BANANA   1
"""
    
  
# For input BANANA, winner will be Stuart with 12 points...
