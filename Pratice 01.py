# Cahnge the  Attribute
print("Change Class Attribute :")
class Sample:
    a = "akash"

obj=Sample()
obj.a="TanVir"

print(obj.a)
print(Sample.a)


# Change the Attribute
Sample.a='akash'
print(Sample.a)