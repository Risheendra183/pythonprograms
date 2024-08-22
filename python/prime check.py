def prime(number):
    
        is_prime=True
        if number==1:
            is_prime==False
        for i in range(2,number):
            if number%i==0:
                is_prime=False
        if is_prime==True:
            print("prime no")
        else:
            print("not a prime")

number=int(input("enter number"))
prime(number)
    
