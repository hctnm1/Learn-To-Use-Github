def fibonacci():
    n = int(input())
    n1, n2 = 0, 1
    cont = 0

    while cont <n:
        print(f'{n1}, ',end='')
        s = n1 + n2
        n1 = n2
        n2 = s
        cont += 1
        if cont == (n-1):
            print(f'{n1}')
            break
            
def main():
    fibonacci()

if __name__=='__main__':
    main()