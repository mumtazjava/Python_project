print("WELCOME to quiz game")

playing=input("DO YOU WANT TO PLAY? ")
if playing.lower() !="yes":
    quit()

print("Lets play")  
score=0  
answer=input("What does CPU stand for ")    
if answer.lower() =='central processing unit':
    print("correct!")
    score+=1
    
else:
    print("incorrect")   
answer=input("What does GPU stand for ")        
if answer.lower() =='graphics processing unit':
    print("correct!")
    score+=1
else:
    print("incorrect")  
answer=input("What does HDD")         
if answer.lower() =='hard disk drive':
    print("correct!")
    score+=1
else:
    print("incorrect") 
answer=input("What does RAM stand for ")          
if answer.lower() =='random access memory':
    print("correct!")
    score+=1
else:
    print("incorrect") 
answer=input("What does CPU stand for ")          
if answer.lower() =='central processing unit':
    print("correct!")
    score+=1
else:
    print("incorrect") 
    
print("You Total correct gess is  "+str(score))  
percentage = (score / 5) * 100
print("Your score percentage is: " + str(percentage) + "%")
       
                   
    
    
    