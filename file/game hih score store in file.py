with open("/home/southville/cvtindell.txt","w") as f:

        existing = f.read().split()
        for i in range(1, 10):
            print(i)
        if i not in f:
            f.write(str(i))

with open("/home/southville/cvtindell.txt") as f:
    print(f.read(),'here the highest ')