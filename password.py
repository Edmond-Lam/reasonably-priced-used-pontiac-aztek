import math

def taskOne(pswrd):
    return (not(not[x for x in pswrd if x.isupper()])) and (not(not[x for x in pswrd if x.islower()])) and (not(not[x for x in pswrd if x.isdigit()]))

print taskOne("App1e")

def taskTwo(pswrd):
    print pswrd
    a = [x for x in pswrd]
    if taskOne(pswrd):
        score = len([x for x in a if x.isupper()])/1.5 + len([x for x in a if x.isdigit()]) + len([x for x in a if x.islower()])/1.5 + len([x for x in a if x in ".?!&#,;:-_*"])
        if score>10:
            return 10;
        else:
            return int(math.floor(score) + 1);
    else:
        return "The password is not valid."

print taskTwo("Grovyle_12251999")

print taskTwo("groV?!1grov")

        
