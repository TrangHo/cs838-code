# FEATURE 3 : CONTAIN COLLEGE
#
# TO CHECK IF AN EXTRACTED STRING CONTAINS THE WORD "College" OR NOT
#     TRUE - CONTAINS "College"
#     FALSE - OTHERWISE
#
#====================================================================================================

def relevant(word):
    if (word == "of") or (word == "at") or (word == "in") or (word == "for"):
        return False
    else:
        return True

def preprocessing(s):
    s = s.replace(",", " ").replace("-", " ").replace(".", " ")

def test(s):
    words = s.split()
    toreturn = False
    for word in words:
        if (word == 'College'):
            toreturn = True
            break
    return toreturn
