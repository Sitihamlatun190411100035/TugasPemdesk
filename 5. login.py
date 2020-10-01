uname={"sitihamlatun"}
Pasword = 17062002
i = 1
while True:
    Uname = input("Masukkan username = ")
    if Uname == Uname:
        break
    else:
        print("Username tidak sama")
while i <= 3:
    Pasword = int(input("Masukkan pasword = "))
    if Pasword == Pasword:
        print("Anda berhasil login")
        break
    else:
        print("Pasword anda salah")
    if i == 3:
        print("Username atau psword salah, coba lagi nanti")
        break
    i += 1
        
        
