import random

global array
pos_x = 0
pos_y = 0

class Jedinec:
    def __init__(self,pocet_genov,gen):
        self.pocet_genov = pocet_genov
        self.gen = gen
        self.fitnes = 0


def vytvorenie_kombinacii(velkost_generacie):
    array_generacie = []
    #array_generacie = random.randint(velkost_generacie, size=(velkost_generacie))
    #array_generacie = random.sample(range(1, velkost_generacie + 1),velkost_generacie)
    #print(array_generacie)
    return random.sample(range(1, velkost_generacie + 1),velkost_generacie)

def zacni_hrabat(x,y,cislo_genu,smer,jedinec,pos_x,pos_y,):

    if (smer == 0):
        return chod_dole(x,y,cislo_genu,smer,jedinec,pos_x,pos_y)

    if(smer == 1):
        return chod_vlavo(x,y,cislo_genu,smer,jedinec,pos_x,pos_y)

    if (smer == 2):
        return chod_hore(x,y,cislo_genu,smer,jedinec,pos_x,pos_y)

    if (smer == 3):
        return chod_vpravo(x,y,cislo_genu,smer,jedinec,pos_x,pos_y)


def chod_vlavo(x, y, cislo_genu, smer, jedinec, pos_x, pos_y):
    #print("X: " + str(x) + "< " + str(pos_x) + "Y: " + str(y) + "< " + str(pos_y))


    if (x >=0 and y >=0 and x < pos_x and y < pos_y and array[x][y] == 0):
        array[x][y] = cislo_genu
        print(array[x][y])
        y -= 1
        chod_vlavo(x, y, cislo_genu, smer, jedinec, pos_x, pos_y)
    elif(y == pos_y-1 and array[x][y] != 0 or y == 0):
        print("VLAVO FIRST FALSE")
        return False
    elif(x+1 < pos_x and y < pos_y and y > 0 and x+1 > 0 and array[x+1][y+1] == 0):
        print("ELIF 1")
        zacni_hrabat(x+1,y+1,cislo_genu,0,jedinec,pos_x,pos_y)
    elif(x-1< pos_x and y < pos_y and y > 0 and x+1 > 0 and array[x-1][y+1] == 0):
        print("ELIF 2 vlavo")
        zacni_hrabat(x-1,y+1,cislo_genu,2,jedinec,pos_x,pos_y)
    else:
        print("FALse")
        return True

def chod_vpravo(x, y, cislo_genu, smer, jedinec, pos_x, pos_y):
    print("VPRAVO")
    print("X: " + str(x) + "< " + str(pos_x) + "Y: " + str(y) + "< " + str(pos_y))
    if (x < pos_x and y < pos_y and array[x][y] == 0):
        array[x][y] = cislo_genu
        print(array[x][y])
        y += 1
        chod_vpravo(x, y, cislo_genu, smer, jedinec, pos_x, pos_y)
    elif(y == 0 and array[x][y] != 0):
        return False
    elif(x + 1 < pos_x and y < pos_y and x + 1 > 0 and y > 0 and array[x+1][y-1] == 0):
        print("ELIF 1")
        zacni_hrabat(x+1,y-1,cislo_genu,0,jedinec,pos_x,pos_y)
    elif(x-1 < pos_x and y < pos_y and x-1 > 0 and y > 0 and array[x-1][y-1] == 0):
        print("ELIF 2")
        zacni_hrabat(x-1,y-1,cislo_genu,2,jedinec,pos_x,pos_y)
    else:
        print("FALse")
        return True


def chod_dole(x,y,cislo_genu,smer,jedinec,pos_x,pos_y):
    print("X: " + str(x) +  "< " + str(pos_x) + "Y: " + str(y) + "< " + str(pos_y))
    if(x < pos_x and y < pos_y and array[x][y] == 0):
        array[x][y] = cislo_genu
        print(array[x][y])
        x += 1
        chod_dole(x,y,cislo_genu,smer,jedinec,pos_x,pos_y)
    elif (x == 0 and array[x][y] != 0):
        return False
    elif (x  < pos_x and y+ 1 < pos_y and y + 1 > 0 and x > 0 and array[x-1][y + 1] == 0):
        print("ELIF 1 vpravo")
        zacni_hrabat(x - 1, y + 1, cislo_genu, 3, jedinec, pos_x, pos_y)
    elif (x < pos_x and y - 1 < pos_y and x > 0 and y - 1 > 0 and array[x-1][y - 1] == 0):
        print("ELIF 2")
        zacni_hrabat(x - 1, y - 1, cislo_genu, 1, jedinec, pos_x, pos_y)
    else:
        print("FALse ")
        return True

def chod_hore(x, y, cislo_genu, smer, jedinec, pos_x, pos_y):
    print("HORE")
    print("X: " + str(x) + "< " + str(pos_x) + "Y: " + str(y) + "< " + str(pos_y))
    if (x >=0 and y >=0 and array[x][y] == 0):
        array[x][y] = cislo_genu
        print(array[x][y])
        x -= 1
        chod_hore(x, y, cislo_genu, smer, jedinec, pos_x, pos_y)
    elif (x == pos_x-1 and array[x][y] != 0):
        return False
    elif (x < pos_x and y + 1 < pos_y and x > 0 and y + 1 > 0 and array[x+1][y + 1] == 0):
        print("HORE- vpravo")
        zacni_hrabat(x + 1, y + 1, cislo_genu, 3, jedinec, pos_x, pos_y)
    elif (x < pos_x and y - 1 < pos_y and x > 0 and y - 1 > 0 and array[x+1][y-1] == 0):
        print("HORE - vlavo")
        zacni_hrabat(x + 1, y - 1, cislo_genu, 1, jedinec, pos_x, pos_y)
    else:
        print("FALse")
        return True





def main():

    POCET_JEDINCOV = 10
    POCET_GENERACII = 1

    generacia = []
    najlepsi_jedinec = "";
    kamene = ""
    fitnes_goal = ""

    pocet_genov = 11

    #VSTUP

    print("Insert size of garden:")
    pos_x = int(input())
    pos_y = int(input())

    global array
    array = [[ 0 for i in range(pos_x)] for j in range(pos_y)]
    ''' 
    for i in range(1):
        print("Insert where to place stone X-riadok Y-stlpec: ")
        x = int(input())
        y = int(input())
        array[x][y] = -1

    '''
    print(vytvorenie_kombinacii(11))


    for g in range(POCET_JEDINCOV):
        generacia.append(Jedinec(pocet_genov,vytvorenie_kombinacii(pocet_genov)))
        #print(generacia[g].gen)



    for populacia in range(POCET_GENERACII):
        for jedinec in generacia:
            print(jedinec.gen)

    print("ARRAY")

    for i in range(pos_x):
        for j in range(pos_y):
            print(array[i][j],end= "")
            #print("]i: " + str(i) + " j: " + str(j) + " [",end= "")
        print("")


    vchod = 16


    test_jedinec =  Jedinec(5,[1,2,6,9,17])
    test_generacia = []
    test_generacia.append(test_jedinec)

    print("TEST JEDINEC" + str(test_jedinec.gen))


    for i in range(test_generacia[0].pocet_genov):
        print("VCHOD: " + str(vchod))
        vchod = test_generacia[0].gen[i]
        print("GENERACIA: ")
        cislo_genu = test_generacia[0].gen[i]
        if(vchod < pos_x):
            print("vchod")
            print(array[0][vchod])
            print(("POS X") + str(pos_x))
            print(zacni_hrabat(0,vchod,cislo_genu,0,generacia[0],pos_x,pos_y))
        elif (vchod < pos_x + pos_y):
            print(array[vchod%pos_x][pos_x-1])
            print(zacni_hrabat(vchod%pos_x,pos_x-1,cislo_genu,1,generacia[0],pos_x,pos_y))
        elif (vchod < 2 * pos_x + pos_y):
            print(array[pos_y-1][(pos_x-1)-(vchod % (pos_x + pos_y))])
            print(zacni_hrabat(pos_y-1,(pos_x-1)-(vchod % (pos_x + pos_y)),cislo_genu,2,generacia[0],pos_x,pos_y))
        else:
            print("ELSE")
            print(array[(pos_y-1)-(vchod % (2*pos_x+pos_y))][0])
            print(zacni_hrabat(((pos_y-1)-(vchod % (2*pos_x+pos_y))),0,cislo_genu,3,generacia[0],pos_x,pos_y))

        print("ARRAY AFTER ")

        for i in range(pos_x):
            for j in range(pos_y):
                print(array[i][j],end= " ")
                if(array[i][j]< 9):
                    print("",end=" ")
                #print("]i: " + str(i) + " j: " + str(j) + " [",end= "")
            print("")
































if __name__ == '__main__':
    main()