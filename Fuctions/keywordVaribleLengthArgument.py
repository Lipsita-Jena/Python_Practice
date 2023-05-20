# Keyword Variable Length Argument
# With variable  argument let sat we want the keyword associated with it
#kargs

def person(name,**data):
    print(name)
    print(data)
person('Lipsita',age=28,city='Mumbai')