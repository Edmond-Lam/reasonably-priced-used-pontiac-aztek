def taskOne(pswrd):
    a = [x for x in pswrd]
    return (not(not[x for x in a if x.isupper()])) and (not(not[x for x in a if x.islower()])) and (not(not[x for x in a if x.isdigit()]))
    
print taskOne("App1e")