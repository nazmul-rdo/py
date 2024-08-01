book=["a","b","aa","bb"]
#<class 'list'>

bookset={"a","b","aa","bb"}
#<class 'set'>

bookdict = {"a" : "$5", "b" : 6}
#<class 'dict'>

print(type(book))
print(type(bookset))
print(type(bookdict))

#String
x = "Hello Programmers is a platform for all the programmers seeking their carrrer in programming field.."

x=x[6:-1]

print(x)

x=x.replace("field", "sector")

print(x)
if "Programmers" in x:
    print(x)
else:
    print("Invalid")