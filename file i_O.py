f = open("/home/southville/cvtindell coredirection.txt","rb")
read= f.read()
# print(read)
# print(data)
f.close()


# how to write a file
f = open("/home/southville/cvtindell coredirection.txt","w")
st = "How are you buddy "
f.write(st)
f.close()

f = open("/home/southville/cvtindell coredirection.txt")
data3 = f.read()
print(data3)


f = open("/home/southville/cvtindell coredirection.txt","w")
f.write("/nThis is addition")
f.close()


f = open("/home/southville/cvtindell coredirection.txt")
data4 = f.read()
print(data4)