with open("/home/southville/cvtindell coredirection.txt") as f:
    c = f.read()
    print(c)
    if "Twinkle" in c:
        print("present")
    else:
        print("not found")