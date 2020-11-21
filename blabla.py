print ("hello player")
name = input("what is your name?")
#int means converting anything typed into integer for python
age = int(input ( "what is your age?"))
health=100
if age >= 18:
    print  ('Welcome',name,'to the new world')

else:  
    print ('sorry',name,'you are not qualified to enter.') 
    #.lower means converting anything you type into lower cases 
    want_to_play= input("do you want to continue?").lower()
    if want_to_play == "yes":
        print ("welcome",name," to the new world")
    else:
        print ("Goodbye player")

print ("you have been reborn as a hero who has healing capabilites with",health,"health points")

left_or_right = input("You descend into a town filled with demons. There are two diverging paths to the castle, which road do you take?(Left or Right)").lower()
if left_or_right == "left":
    print (" you encountered a High class demon. Get ready to fight!")



else:
    print ("you see a woman in the progress of transforming into a demon. You have the option to heal her or kill her. Note:healing her has 50 percent chance of saving her.(Heal or Kill)").lower()

