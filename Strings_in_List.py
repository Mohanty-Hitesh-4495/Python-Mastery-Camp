# return a list of names if length of strings is less than 7 from a given list of strings

def strlist(l):
    return [x for x in l if isinstance(x,str) and len(x)<7]

l=["bsc","fhjdffvb","efuwv","fh","vhjbdfhvd","vchs",6,79,] 
print(strlist(l))







