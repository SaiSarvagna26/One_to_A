def one_to_A(number):
    if number>0:
        one_to_A(number-1)
        print(number,end=" ")
    else:
        return

number=int(input())
one_to_A(number)
