# explain touple in detail
# unordered
# unchanged
# duplicate value allow
#  [ ]    ()
# list touples
# no single item  X  , More than one

# wap to print touple and perform below action
# add new touple
# add and remove any one element from index value
# unpacked done



x = ("a","b","c")
print(x)

# add new touple
y = x + ("d",)
print(y)

# add and remove any one element from index value
y = y[:2] + ("e",) + y[3:]
print(y)

# unpacked done
for i in y:
    print(i)


