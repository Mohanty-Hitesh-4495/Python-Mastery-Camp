
def add(a,b):
    if ismatrix(a) and ismatrix(b) and isequal(a,b):
        return [[a[j][i]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    return "Matrix Addition Not Possible: as matrices are not compatible :("

def ismatrix(a):
    dt = [True if isinstance(i,list) else False for i in a]
    return False if False in dt else True

def isequal(a,b):
    for x in a:
        for y in b:
            if len(x)!=len(y):
                return False
    return True 

