print("masukkan bilangan yang akan dihitung :")

jum_data =5
total = 0
data = []
for i in range(0,jum_data):
    bilangan=int(input("bilangan:"))
    data.append(bilangan)
    total = total + bilangan

rerata = total / 5.0
print("rata - rata : ",rerata)

print()
print("daftar nilai diatas rata-rata")

for i in range (0,jum_data):
    if data[i] > rerata:
        print(data[i])
