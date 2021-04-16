for b in range(int(input("enter the limit"))):
    a = "fizz" if b%15==0 else "buzz" if b%5==0 else "fizzbuzz" if b%3==0 else str(b)
    print(a)