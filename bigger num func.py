"""Write the above solution in a function which takes take numbers and return the bigger number
[topic covered: function]"""
a = int(input("enter the number"))
b = int(input("enter the number"))


def largest(x,y):
    c = max(x,y)
    print(c," is the largest.")


largest(a,b)
