for i in dir(tuple()):
    if "__"not in i:
        print(i)

demet=("onur","askin","1997","onur")
count=demet.count("onur")
print(count)
index=demet.index("onur")
print(index)