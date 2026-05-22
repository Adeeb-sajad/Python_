
def nd_list(mylist, level=0, indent = True):    
    for i in mylist:

        if isinstance(i, list):

            nd_list(i, level + 1,indent)

        else:
            if indent:
              for j in range(level):
                print("\t", end="")
            
            print(i)

def nd_tuple(mylist, level=0, indent = True):    
    for i in mylist:

        if isinstance(i, tuple):

            nd_list(i, level + 1,indent)

        else:
            if indent:
              for j in range(level):
                print("\t", end="")
            
            print(i)

def nd_tuple(mylist, level=0, indent = True):    
    for i in mylist:

        if isinstance(i, tuple):

            nd_list(i, level + 1,indent)

        else:
            if indent:
              for j in range(level):
                print("\t", end="")
            
            print(i)            

def nd_set(mylist, level=0, indent = True):    
    for i in mylist:

        if isinstance(i, set):

            nd_list(i, level + 1,indent)

        else:
            if indent:
              for j in range(level):
                print("\t", end="")
            
            print(i)                        