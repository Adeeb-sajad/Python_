def print_list(a,indx):
 if(indx>=0):
   print(a[indx-1])
   print_list(a,indx-1)
 else:
   return  
  
a = [1,2,3,4,5]
print_list(a,5) 

class student:
 @staticmethod
 def col_name():
  print("abc colage")