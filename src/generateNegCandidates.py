import glob, os, random, re

# given a pattern and the text, return a list of locations where all the strings satisfying the pattern
def locate_position(pattern, text):
    location = [(m.start(0), m.end(0)) for m in re.finditer(pattern, text)]
    return location
def locate(pattern,text):
    return re.finditer(pattern, text)
# given starting point and ending point of two strings, determine whether they are overlapping
def check_overlap(a_start, a_end, b_start, b_end):
    return (a_start <= b_end) & (b_start <= a_end)

def itor_to_obj(itor):
    tmp = list()
    for obj in itor:
        tmp.append(obj)
    return tmp

if __name__ == "__main__":
#os.chdir("/mydir")  # use to change the directory where .txt files locate
    for file in glob.glob("*.txt"):
        input_file = open(file, 'r')
        text = input_file.read()
        # find out the positive markups so that the negative candidates selected did not overlap with them
        p_pos =r'<pos>(.*)</pos>' 
        pos_words = re.findall(p_pos,text)
        pos_loc = locate_position(p_pos,text)
        pattern = list()
        # p1 is extracting Consecutive captitalized words with length 2 or more
        #(                # begin capture
        #  [A-Z]            # one uppercase letter  \ First Word
        #  [a-z]+           # 1+ lowercase letters  /
        #  (?=\s[A-Z])      # must have a space and uppercase letter following it
        #  (?:                # non-capturing group
        #    \s               # space
        #    [A-Z]            # uppercase letter   \ Additional Word(s)
        #    [a-z]+           # lowercase letter   /
        #  )+              # group can be repeated (more words)
        #)               #end capture
        p1 = r'([A-Z][a-z]+(?=\s[A-Z])(?:\s[A-Z][a-z]+)+)'
        pattern.append(p1)
        
        
        p2 = r'\b(at|from|in)\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)?'
        pattern.append(p2)
        loc_it = [locate(p,text) for p in pattern] # this is a list of iterators
        # filter out the empty list where no match is found
        # turn the iterator to a list of objects
        loc_obj = [itor_to_obj(it) for it in loc_it]
        rand_loc_obj = list()
        for l in loc_obj:
            if l:
                rand_loc_obj.append(random.choice(l))    
            else:
                rand_loc_obj.append(list())
        # print(rand_loc_obj)
        # conver iterator to location
        rand_loc = list()
        if rand_loc_obj[0]:
            rand_loc.append([rand_loc_obj[0].start(),rand_loc_obj[0].end()]) # p1
        if rand_loc_obj[1]:    
            rand_loc.append([rand_loc_obj[1].start()+len(rand_loc_obj[1].group(1))+1,rand_loc_obj[1].end()]) #p2
        # this list contains all the final negative examples
        select_loc = list()
        for i in rand_loc:      
            flag = 0
            for j in pos_loc:
                if check_overlap(i[0],i[1],j[0],j[1]):
                    flag = 1
            if flag != 1:
                select_loc.append(i)
        # debug: print out selected negative candidates
        for i in select_loc:
            #print(i[0],i[1])
            print(text[i[0]:i[1]])
        
            
                    
                    
                
                    