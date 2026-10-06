
def __init__(self, aldiz = 0):
        self.aldiz = aldiz

def pisatu(self, bola1, bola2):

        pisua1 = sum(bola.pisua for bola in bola1)
        pisua2 = sum(bola.pisua for bola in bola2)
        self.aldiz += 1

        if pisua1 > pisua2:
            return 1
        elif pisua1 < pisua2:
            return -1
        else:
            return 0

def emaitza(self, bola):

        if(bola.pisua > 1):
            return "Asmatu duzu gehien piesatzen duen bola  " + str(self.aldiz) + " aldiz erabili da"
        else:
            return "Ez duzu asmatu"