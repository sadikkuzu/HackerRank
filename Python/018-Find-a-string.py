def count_substring(string, sub_string):
    x=0
    i=0
    while(i<=len(string)):
        j = string[i:].find(sub_string)
        i += j
        if j<0:
            break
        x += 1
        i += 1
    return x