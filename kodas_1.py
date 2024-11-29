def gauk_sumas_b(*args: int, info=False):
    suma_lyginiu = 0
    suma_nelyginiu = 0
    lyginiai = []
    nelyginiai = []
    for elem in args:
        if elem % 2 == 0:
            suma_lyginiu += elem
            lyginiai.append(elem)
        else:
            suma_nelyginiu += elem
            nelyginiai.append(elem)
    if info:
        print(f"Visi ivesti skaiciai {list(args)}")
        print(f"skaiciai lyginiai {lyginiai}")
        print(f"skaiciai nelyginiai {nelyginiai}")
        print(f"lyginiu skaiciu suma {sum(lyginiai)}")
        print(f"nelyginiu skaiciu suma {sum(nelyginiai)}")
    return suma_lyginiu, suma_nelyginiu


print(type(gauk_sumas_b(1, 1, 2, 2, info=True)))
print("-------")
