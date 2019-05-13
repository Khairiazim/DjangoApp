jantina = input("jantina anda (lelaki/perempuan)")
berat = float(input("berat:"))
tinggi = float(input("tinggi:"))
umur = float(input("umur:"))

formula = float(10 * berat + 6.25 * tinggi - 5 * umur)
if jantina == "lelaki":
    bmr = formula + 5

if jantina == "perempuan":
    bmr = formula - 161

print("bmr:", bmr)
kalori = float(bmr * 1.2)
print("kalori seharian:", kalori)
