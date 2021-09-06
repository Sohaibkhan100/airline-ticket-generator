

              #airline  service
              #code gernereator
def code():
    import random
    i1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9"]
    for j in range(0,5):        
        print(random.choice(i1))
     
               #funtions
def function1():
    x=open("systemfile1","w")
    d1=str(input("enter your name ="))
    d2=str(input("enter your age ="))
    d3=str(input("enter your CNIC ="))
    d4=str(input("enter your passport number ="))
    d5=str(input("you want to travel from? ="))
    d6=str(input("you want to travel to? ="))
    d7=str("------------------------------------------------------------")
    x.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n" .format(d1,d2,d3,d4,d5,d6,d7))
    print("")
    print("thank you",d1)
    print("sir here is your flight code")  
    code()
    print("")
    
def function2():
    y=open("systemfile2","a")
    d1=str(input("enter your name ="))
    d2=str(input("enter your age ="))
    d3=str(input("enter your CNIC ="))
    d4=str(input("enter your passport number ="))
    d5=str(input("you want to travel from? ="))
    d6=str(input("you want to travel to? ="))
    d7=str("------------------------------------------------------------")
    y.write("{}\n{}\n{}\n{}\n{}\n{}\n" .format(d1,d2,d3,d4,d5,d6,d7))
    print("")
    print("thank you",d1)
    print("sir here is your flight code")  
    code()
    print("") 
    

def function3():
    z=open("systemfile3","a")
    d1=str(input("enter your name ="))
    d2=str(input("enter your age ="))
    d3=str(input("enter your CNIC ="))
    d4=str(input("enter your passport number ="))
    d5=str(input("you want to travel from? ="))
    d6=str(input("you want to travel to? ="))
    d7=str("------------------------------------------------------------")
    z.write("{}\n{}\n{}\n{}\n{}\n{}\n" .format(d1,d2,d3,d4,d5,d6,d7))
    print("")
    print("thank you",d1)
    print("sir here is your flight code")  
    code()
    print("")               
 

                #loop and conditions

i=0
while i == 0:
      print("********WELCOME TO TIMEAIRLINES**********")
      print("####select your ticket class####")
      d=int(input("enter any letter to exit and number to contniue ="))
      print("for firstclass press (1)")
      print("for buisness class press (2)")
      print("for economic class press (3)")
      c=int(input("enter class code="))
     
      if(c == 1):
          function1()
    
      elif(c == 2):
          function2()
    
      elif(c == 3):
           function3()





















    