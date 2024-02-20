bilangan = int(input())
faktor = []
for i in range(1, bilangan +1):
    if bilangan % i == 0:
        faktor.append(i)

print(f"angka dari bilangan {bilangan} adalah:")
for f in faktor:
    print(f)