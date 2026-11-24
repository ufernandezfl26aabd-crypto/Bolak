
class Bola:

    def __init__(self, zenbakia, pisua):
        self.zenbakia = zenbakia
        self.pisua = pisua


class Balanza:

    def pisatu(self, taldea1, taldea2):
        pisua1 = sum(b.pisua for b in taldea1)
        pisua2 = sum(b.pisua for b in taldea2)

        if pisua1 > pisua2:
            return 1
        elif pisua1 < pisua2:
            return -1
        else:
            return 0


# 8 bolak sortu
bolak = [Bola(i, 10) for i in range(1, 9)]

# 7. bolak pisu handiagoa dauka
bolak[6].pisua = 11

balantza = Balanza()

# LEHENENGO PISAKETA: 3 vs 3
emaitza = balantza.pisatu(bolak[:3], bolak[3:6])

if emaitza == 1:
    susmagarriak = bolak[:3]
elif emaitza == -1:
    susmagarriak = bolak[3:6]
else:
    susmagarriak = bolak[6:8]

# BIGARREN PISAKETA: 1 vs 1
emaitza = balantza.pisatu(susmagarriak[:1], susmagarriak[1:2])

if emaitza == 1:
    aurkituta = susmagarriak[0]
elif emaitza == -1:
    aurkituta = susmagarriak[1]
else:
    aurkituta = susmagarriak[2]

print("Bola desberdina hau da:", aurkituta.zenbakia)
