import random


global array
global generacia
pos_x = 0
pos_y = 0

class Jedinec:
    def __init__(self,pocet_genov,gen):
        self.pocet_genov = pocet_genov
        self.gen = gen
        self.fitnes = 0


def vytvorenie_kombinacii(velkost_generacie,pos_y,pos_x):
    array_generacie = []
    #array_generacie = random.randint(velkost_generacie, size=(velkost_generacie))
    #array_generacie = random.sample(range(1, velkost_generacie + 1),velkost_generacie)
    #print(array_generacie)
    return random.sample(range(1, 2 * pos_x + 2 * pos_y ),velkost_generacie)

def zacni_hrabat(x,y,cislo_genu,smer,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania):

    if (smer == 0):
        return chod_dole(x,y,cislo_genu,smer,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania)

    if(smer == 1):
        return chod_vlavo(x,y,cislo_genu,smer,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania)

    if (smer == 2):
        return chod_hore(x,y,cislo_genu,smer,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania)

    if (smer == 3):
        return chod_vpravo(x,y,cislo_genu,smer,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania)


def chod_vlavo(x, y, cislo_genu, smer, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania):
    #print("X: " + str(x) + "< " + str(pos_x) + "Y: " + str(y) + "< " + str(pos_y))


    if (x >=0 and y >=0 and x < pos_x and y < pos_y and array[x][y] == 0):
        array[x][y] = cislo_hrabania
        #print(array[x][y])
        y -= 1
        generacia[cislo_generacie].fitnes += 1
        chod_vlavo(x, y, cislo_genu, smer, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    elif(y == pos_y-1 and array[x][y] != 0 or y == 0):
        return jedinec
    elif(x+1 < pos_x and y < pos_y and y >= 0 and x+1 >=0 and array[x+1][y+1] == 0):
        zacni_hrabat(x+1,y+1,cislo_genu,0,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania)
    elif(x-1< pos_x and y < pos_y and y >= 0 and x+1 >= 0 and array[x-1][y+1] == 0):
        zacni_hrabat(x-1,y+1,cislo_genu,2,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania)
    else:
        if (y - 1 < 0 or x == pos_x-1 or x == 0):
           #print("JE TO OK")
            pass
        else:
            for x in range(pos_x):
                for y in range(pos_y):
                    if (array[x][y] == cislo_hrabania):
                        array[x][y] = 0
                        generacia[cislo_generacie].fitnes -= 1

def chod_vpravo(x, y, cislo_genu, smer, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania):
    if (x < pos_x and y < pos_y and array[x][y] == 0):
        array[x][y] = cislo_hrabania
        y += 1
        generacia[cislo_generacie].fitnes += 1
        chod_vpravo(x, y, cislo_genu, smer, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    elif(y == 0 and array[x][y] != 0):
        return jedinec
    elif(x + 1 < pos_x and y < pos_y and x + 1 >= 0 and y >= 0 and array[x+1][y-1] == 0):
        zacni_hrabat(x+1,y-1,cislo_genu,0,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania)
    elif(x-1 < pos_x and y < pos_y and x-1 >= 0 and y >= 0 and array[x-1][y-1] == 0):
        zacni_hrabat(x-1,y-1,cislo_genu,2,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania)
    else:
        if(y + 1 > pos_y or x == pos_x-1 or x == 0):
            pass
        else:
            for x in range(pos_x):
                for y in range(pos_y):
                    if(array[x][y] == cislo_hrabania):
                        array[x][y] = 0
                        generacia[cislo_generacie].fitnes -= 1


        return jedinec


def chod_dole(x,y,cislo_genu,smer,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania):
    if(x < pos_x and y < pos_y and array[x][y] == 0):
        array[x][y] = cislo_hrabania
        x += 1
        generacia[cislo_generacie].fitnes +=1
        chod_dole(x,y,cislo_genu,smer,jedinec,pos_x,pos_y,cislo_generacie,cislo_hrabania)
    elif (x == 0 and array[x][y] != 0):
        return jedinec
    elif (x  < pos_x and y + 1 < pos_y and y + 1 >= 0 and x >= 0 and array[x-1][y + 1] == 0):
        zacni_hrabat(x - 1, y + 1, cislo_genu, 3, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    elif (x < pos_x and y - 1 < pos_y and x >= 0 and y - 1 >= 0 and array[x-1][y - 1] == 0):
        zacni_hrabat(x - 1, y - 1, cislo_genu, 1, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    else:
        if (x + 1 > pos_x or y == pos_y-1 or y == 0):
            pass
        else:
            for x in range(pos_x):
                for y in range(pos_y):
                    if (array[x][y] == cislo_hrabania):
                        array[x][y] = 0
                        generacia[cislo_generacie].fitnes -= 1

def chod_hore(x, y, cislo_genu, smer, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania):
    if (x >=0 and y >=0 and array[x][y] == 0):
        array[x][y] = cislo_hrabania
        x -= 1
        generacia[cislo_generacie].fitnes += 1
        chod_hore(x, y, cislo_genu, smer, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    elif (x == pos_x-1 and array[x][y] != 0):
        return jedinec
    elif (x < pos_x and y + 1 < pos_y and x >= 0 and y + 1 >= 0 and array[x+1][y + 1] == 0):
        zacni_hrabat(x + 1, y + 1, cislo_genu, 3, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    elif (x < pos_x and y - 1 < pos_y and x >= 0 and y - 1 >= 0 and array[x+1][y-1] == 0):
        zacni_hrabat(x + 1, y - 1, cislo_genu, 1, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    else:
        if (x - 1 < 0 or y == pos_y-1 or y == 0):
            pass
        else:
            for x in range(pos_x):
                for y in range(pos_y):
                    if (array[x][y] == cislo_hrabania):
                        array[x][y] = 0
                        generacia[cislo_generacie].fitnes -= 1


def vyber_zaciatok_koniec(POCET_JEDINCOV,pocet_genov):
    for d in range(int(POCET_JEDINCOV/2)):
        for r in range(pocet_genov):
            #TODO prepísať 100
            if(random.randint(0,100) < 100):
                generacia[POCET_JEDINCOV- d - 1].gen[r] = generacia[d].gen[r]




def main():

    POCET_JEDINCOV = 100
    POCET_GENERACII = 1500
    ODKIAL_MUTOVAT = 2
    MUTACIA_PRAVDEPODOBNOST = 100

    fitnes_min = -1
    fitnes_max = 0

    global generacia
    generacia = []
    najlepsi_jedinec = "";
    kamene = ""
    fitnes_goal = 0



    #VSTUP

    print("Insert size of garden:")
    pos_x = int(input())
    pos_y = int(input())


    global array
    array = [[ 0 for i in range(pos_x)] for j in range(pos_y)]

    print("Insert number of stones: ")
    number_of_stones = int(input())

    pocet_genov = pos_x + pos_y + number_of_stones
    fitnes_goal = pos_x * pos_y - number_of_stones


    for i in range(number_of_stones):
        print("Insert where to place stone X-riadok Y-stlpec: ")
        x = int(input())
        y = int(input())
        array[x][y] = -1

    empty_array = [[array[x][y] for y in range(len(array[0]))] for x in range(len(array))]

    print("empty arr")
    print(empty_array)





    #print(vytvorenie_kombinacii(11))


    for g in range(POCET_JEDINCOV):
        generacia.append(Jedinec(pocet_genov,vytvorenie_kombinacii(pocet_genov,pos_y,pos_x)))
        #print(generacia[g].gen)



    for populacia in range(1):
        for jedinec in generacia:
            print(jedinec.gen)

    print("ARRAY")

    for i in range(pos_x):
        for j in range(pos_y):
            print(array[i][j],end= "")
            #print("]i: " + str(i) + " j: " + str(j) + " [",end= "")
        print("")


    vchod = 16




    #print("TEST JEDINEC" + str(test_jedinec.gen))

    cislo_hrabania = 0
    najdene_riesenie = False

    for generacie_iterator in range(POCET_GENERACII):

        #print(empty_array)
        #print(array)
        fitnes_max = 0
        fitnes_min = -1
        if najdene_riesenie:
            break

        for jedinec_iterator in range(POCET_JEDINCOV):
            cislo_hrabania = 0
            array = [[empty_array[x][y] for y in range(len(empty_array[0]))] for x in range(len(empty_array))]
            generacia[jedinec_iterator].fitnes = 0
            for i in range(generacia[jedinec_iterator].pocet_genov):
                #cislo_generacie = cislo_generacie
                vchod = generacia[jedinec_iterator].gen[i]
                cislo_genu = generacia[jedinec_iterator].gen[i]
                #vchod = int(input())
                #cislo_genu = vchod
                cislo_hrabania += 1;
                if(vchod < pos_x):
                    zacni_hrabat(0,vchod,cislo_genu,0,generacia[jedinec_iterator],pos_x,pos_y,jedinec_iterator,cislo_hrabania)
                elif (vchod < pos_x + pos_y):
                    zacni_hrabat(vchod%pos_x,pos_x-1,cislo_genu,1,generacia[jedinec_iterator],pos_x,pos_y,jedinec_iterator,cislo_hrabania)
                elif (vchod < 2 * pos_x + pos_y):
                    zacni_hrabat(pos_y-1,(pos_x-1)-(vchod % (pos_x + pos_y)),cislo_genu,2,generacia[jedinec_iterator],pos_x,pos_y,jedinec_iterator,cislo_hrabania)
                else:
                    zacni_hrabat(((pos_y-1)-(vchod % (2*pos_x+pos_y))),0,cislo_genu,3,generacia[jedinec_iterator],pos_x,pos_y,jedinec_iterator,cislo_hrabania)

                ''' 
                print("ARRAY PO ")
                for i in range(pos_x):
                    for j in range(pos_y):
                        print(array[i][j],end= " ")
                        if(array[i][j]< 9):
                            print("",end=" ")
                        #print("]i: " + str(i) + " j: " + str(j) + " [",end= "")
                    print("")
                '''


            if(fitnes_max < generacia[jedinec_iterator].fitnes):
                fitnes_max = generacia[jedinec_iterator].fitnes

            if (generacia[jedinec_iterator].fitnes == fitnes_goal):
                najdene_riesenie = True
                print("NAŠLO SA RIEŠENIE  GENERACIA Č: " + str(generacie_iterator) + " FITNESS : " + str(generacia[jedinec_iterator].fitnes))
                print("ARRAY AFTER ")
                for i in range(pos_x):
                    for j in range(pos_y):
                        print(array[i][j], end=" ")
                        if (array[i][j] <= 9 and array[i][j] >= 0):
                            print("", end=" ")
                        # print("]i: " + str(i) + " j: " + str(j) + " [",end= "")
                    print("")
                break
            else:
                # print("GENERACIA Č: " + str(generacie_iterator))

                sorted_generation = sorted(generacia, key=lambda x: x.fitnes, reverse=True)

                generacia = sorted_generation
                #print("SORTED LIST ")

                #for i in sorted_generation:
                #    print(i.fitnes)

                # sortnuta generácia
                new_generation = []
                mutovanie_iter = POCET_JEDINCOV / ODKIAL_MUTOVAT

                vyber_zaciatok_koniec(POCET_JEDINCOV,pocet_genov)


                # mutacia druhej polky jedincov ak sme zadali 2


                for mutovanie in range(int(mutovanie_iter)):
                    if (random.randint(0, 100) < MUTACIA_PRAVDEPODOBNOST):
                        prvy = random.randint(0, pocet_genov - 1)
                        druhy = random.randint(0, pocet_genov - 1)

                        #print("PRED MUTACIOU: " + str(generacia[mutovanie].gen[prvy]) + " DRUHY: " + str(generacia[mutovanie].gen[druhy]))

                        prehodenie = generacia[mutovanie].gen[prvy]
                        generacia[mutovanie].gen[prvy] = generacia[mutovanie].gen[druhy]
                        generacia[mutovanie].gen[druhy] = prehodenie





                        #print("PO MUTACII: " + str(generacia[mutovanie].gen[prvy]) + " DRUHY: " + str(generacia[mutovanie].gen[druhy]))

            #print("JEDINEC NUM: " +  str(jedinec_iterator) + " genfit: " + str(sorted_generation[jedinec_iterator].fitnes))
        print("GENERACIA: " + str(generacie_iterator) + " FITNES MAX: " + str(fitnes_max))





if __name__ == '__main__':
    main()
