# factorials with and without recursion, by Daniele Gargiulo 

while True: # user can endlessly insert numbers to get more factorials
   
    number = input("insert integer number ")

    def factorial(n):
        r = n
        while n > 1:
            r = r * (n-1)
            n -= 1
        return r

    def factorialWithRecursion(n):
        r = n
        if n > 1:
            r = r * factorialWithRecursion(n-1)
        return r

    try:
        val = int(number) #try to cast number as integer to make sure the user typed an integer number
        print(number + "! = " + str(factorialWithRecursion(val)))
    except ValueError:
        print("please make sure to insert integer number")

