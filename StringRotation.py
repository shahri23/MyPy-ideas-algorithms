# Check if a string/number is a roration of the other?

def isRotation(first,second):
    a,b=str(first),str(second)
    test=a+a
    
    if len(a) != len(b):
        return False
    elif b in test:
        return True
    else:
        return False
    
        
isRotation('apple','pleap')
