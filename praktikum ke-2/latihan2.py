def fizzbuzz(n):
    result = []
    for i in range (1, n+1):
          if  (i % 3 == 0 and i % 5 == 0):
            print("Fizzbuzz")
          elif i % 3 == 0:
            print ("Fizz")
          elif i % 5 == 0:
              print ("Buzz")
          elif i % 7 == 0:
              print ("sevent")
          else:
              print(i)
    return result

fizzbuzz(21)


                       
        




