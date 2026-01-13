#keegi vala even odd number checker using clever if jaisa kuch
if 0:
 def mehh(a):
    return ("ODD","EVEN")[a%2==0]

 print(mehh(5))

#Custom exception 
if 0:
 class ThisGuyIsChomuError (Exception):
   pass

 def TryThisGuy(x):
   if(x != "Adeeb" ):
     raise ThisGuyIsChomuError(f"{x} is chomu as he/she is not Adeeb")
    
 try:
  TryThisGuy("sehr")
 except ThisGuyIsChomuError as e:
  print(e)
  print("Be Adeeb or stay chomu")  

#Custom exeception with keegi
if 0:
 class TooStupidToTalkToAdeebError(Exception) :
   def __init__(self, message, value):
     self.message = message
     self.value = value

 def Lets_see_if_u_can_talk_to_Adeeb(x):
   if(x>1):
     raise TooStupidToTalkToAdeebError("You are not eligible to talk to Adeeb",f"As u have {x} back")


 try:
   name = input("Enter your name:")
   x = int(input("Enter the number of backs you have:"))
   Lets_see_if_u_can_talk_to_Adeeb(x)
 except TooStupidToTalkToAdeebError as e:
   print(e.message)
   print(e.value)
 else:
   print(f"{name} is eligible to talk to Adeeb")
 

