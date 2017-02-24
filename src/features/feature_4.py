# FEATURE 4 : START WITH UNIVERSITY
#
# TO CHECK IF AN EXTRACTED STRING STARTS WITH THE WORD "University" OR NOT
#     TRUE - STARTS WITH THE WORD "University"
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

def feature4(s):
    words = s.split()
    if words[0] == "University" or words[-1] == "University":
        return True
    else:
        return False