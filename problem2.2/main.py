bilangan = int(input())
def cetak_faktor(bilangan):
    for i in range(bilangan, 0, -1):
        if bilangan % i == 0:
            print(i)

input_bilangan_1 = 6
print(f"bilangan {input_bilangan_1} adalah:")
cetak_faktor(input_bilangan_1)

input_bilangan_2 = 20
print(f"\nbilangan {input_bilangan_2} adalah:")
cetak_faktor(input_bilangan_2)