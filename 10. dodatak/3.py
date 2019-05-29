x = input("Unesite troznamenkasti broj: ")
x = int(x)

if x < 100 or x > 999:
   print("Uneseni broj nije troznamenkasti!")
else:
   while x<1000:
      prva = x // 100
      zadnja = x % 10
      
      if prva == zadnja:
         print(x)
         break
      x+=1
