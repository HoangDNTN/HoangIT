def NhapDL():
    while True:
        n = int (input (" Nhập vô một số tự nhiên bất kì: "))
        if n > 50 :
            return n
            break

n = NhapDL()
print(" Số đã nhập là:",n)