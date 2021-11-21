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
    #print("VLAVO x " + str(x) + "y " + str(y) + "h " + str(cislo_hrabania))

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
    #print("VPRAVO x " + str(x) + "y " + str(y) + "h " + str(cislo_hrabania))
    if (x < pos_x and y < pos_y and array[x][y] == 0):
        array[x][y] = cislo_hrabania
        y += 1
        generacia[cislo_generacie].fitnes += 1
        chod_vpravo(x, y, cislo_genu, smer, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    elif(y == 0 and x < pos_x and array[x][y] != 0):
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
    if (x >=0 and y >=0 and x < pos_x and y < pos_y and array[x][y] == 0):
        array[x][y] = cislo_hrabania
        x -= 1
        generacia[cislo_generacie].fitnes += 1
        chod_hore(x, y, cislo_genu, smer, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    elif (x == pos_x-1 and array[x][y] != 0):
        return jedinec
    elif (x + 1 < pos_x and y + 1 < pos_y and x >= 0 and y + 1 >= 0 and array[x+1][y + 1] == 0):
        zacni_hrabat(x + 1, y + 1, cislo_genu, 3, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    elif (x + 1 < pos_x and y - 1 < pos_y and x >= 0 and y - 1 >= 0 and array[x+1][y-1] == 0):
        zacni_hrabat(x + 1, y - 1, cislo_genu, 1, jedinec, pos_x, pos_y,cislo_generacie,cislo_hrabania)
    else:
        if (x - 1 < 0 or y == pos_y-1 or y == 0):
            pass
            #print("JE TO OK " + str(cislo_hrabania))
        else:
            #print("VRACAT HORE " + str(cislo_hrabania))
            for x in range(pos_x):
                for y in range(pos_y):
                    if (array[x][y] == cislo_hrabania):
                        array[x][y] = 0
                        generacia[cislo_generacie].fitnes -= 1


def vyber_zaciatok_koniec(POCET_JEDINCOV,pocet_genov,PRAVDEPODOBNOST_KRIZENIE):
    for jedinec_index in range(int(POCET_JEDINCOV/2)):
        for geny in range(pocet_genov):
            flag_selekcia = False
            if(random.randint(0,100) < PRAVDEPODOBNOST_KRIZENIE):
                for kontrola in range(pocet_genov):
                    if(generacia[POCET_JEDINCOV- jedinec_index - 1].gen[geny] == generacia[jedinec_index].gen[kontrola]):
                        #print("FLAG")
                        flag_selekcia = True
                        break

                if flag_selekcia == False:
                    #print("GEN PR: " + str(generacia[d].gen) + " GEN " + str( generacia[POCET_JEDINCOV- d - 1].gen[r]) )
                    generacia[jedinec_index].gen[geny] = generacia[POCET_JEDINCOV - jedinec_index - 1].gen[geny]
                    #print("GEN PO: " + str(generacia[d].gen))


def tournament_selection(generacia,pocet_genov,POCET_JEDINCOV):


    tournament_array = []

    for i in range(POCET_JEDINCOV):
        random_id = int(random.randint(0,POCET_JEDINCOV-1))
       # print("GEN RANDOM FITNESS:" + str(generacia[random_id].fitnes) + " RANDOM ID: " + str(random_id))
        tournament_array.append(generacia[random_id])


    fittest = tournament_array[0];

    for max in tournament_array:
        if(fittest.fitnes < max.fitnes):
            fittest = max


   # print("BEST FIT " + str(fittest.fitnes))
    return fittest


def crossover(PRAVDEPODOBNOST_CROSSOVER,individual_1,indivual_2,pocet_genov):
    sample_array =  [0] * pocet_genov
    new_jedinec = Jedinec(0,sample_array)

    for i in range(pocet_genov):
        #print("I: " + str(i))
        if random.randint(0,100) <= PRAVDEPODOBNOST_CROSSOVER:
            new_jedinec.gen[i] = individual_1.gen[i]
        else:
            new_jedinec.gen[i] = indivual_2.gen[i]

    return new_jedinec


def main():

    #### NASTAVENIE ALGORITMU


    POCET_JEDINCOV = 65
    POCET_GENERACII = 1500
    ODKIAL_MUTOVAT = 2
    MUTACIA_PRAVDEPODOBNOST = 100
    PRAVDEPODOBNOST_CROSSOVER = 50
    PRAVDEPODOBNOST_KRIZENIE = 100

    fitnes_min = -1
    fitnes_max = 0


    global generacia
    generacia = []
    najlepsi_jedinec = "";
    kamene = ""
    fitnes_goal = 0

    tournament = True
    #VSTUP

    print("Insert size of garden: X- riadky Y- stlpce")
    pos_x = int(input())
    pos_y = int(input())


    global array
    array = [[ 0 for x in range(pos_y)] for y in range(pos_x)]

    print("Select selection  [ 1 ] Tournamnet [ 2 ] Strongest-Weakness ")
    input_algo = int(input())

    if input_algo == 1:
        tournament = True
    else:
        tournament = False

    print("Insert number of stones: ")
    number_of_stones = int(input())


    pocet_genov = int((2 * pos_x + 2 * pos_y)/2 + number_of_stones)
    fitnes_goal = pos_x * pos_y - number_of_stones


    for i in range(number_of_stones):
        print("Insert where to place stone X-riadok Y-stlpec: ")
        x = int(input())
        y = int(input())
        array[x][y] = -1

    empty_array = [[array[x][y] for y in range(len(array[0]))] for x in range(len(array))]


    for g in range(POCET_JEDINCOV):
        generacia.append(Jedinec(pocet_genov,vytvorenie_kombinacii(pocet_genov,pos_y,pos_x)))
        #print(generacia[g].gen)


    for x in range(len(array)):
        for y in range(len(array[0])):
            print(array[x][y],end= " ")
            #print("]i: " + str(i) + " j: " + str(j) + " [",end= "")
        print("")


    vchod = 16

    cislo_hrabania = 0
    najdene_riesenie = False
    najlepsie_riesenie_fitnes = 0
    najlepsie_riesenie_geny = []

    for generacie_iterator in range(POCET_GENERACII):

        #print(empty_array)
        #print(array)
        fitnes_max = 0
        fitnes_min = 999999
        if najdene_riesenie:
            break
        priemer = 0
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
                if(vchod < pos_y):
                    zacni_hrabat(0,vchod,cislo_genu,0,generacia[jedinec_iterator],pos_x,pos_y,jedinec_iterator,cislo_hrabania)
                elif (vchod < pos_x + pos_y):
                    zacni_hrabat(vchod%pos_y,pos_y-1,cislo_genu,1,generacia[jedinec_iterator],pos_x,pos_y,jedinec_iterator,cislo_hrabania)
                elif (vchod < 2 * pos_x + pos_y):
                    zacni_hrabat(pos_x-1,(pos_y-1)-(vchod % (pos_x + pos_y)),cislo_genu,2,generacia[jedinec_iterator],pos_x,pos_y,jedinec_iterator,cislo_hrabania)
                else:
                    zacni_hrabat(((pos_x-1)-(vchod % (2*pos_x+pos_y))),0,cislo_genu,3,generacia[jedinec_iterator],pos_x,pos_y,jedinec_iterator,cislo_hrabania)


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
                if fitnes_max > najlepsie_riesenie_fitnes:
                    najlepsie_riesenie_fitnes = generacia[jedinec_iterator].fitnes
                    najlepsie_riesenie_geny = generacia[jedinec_iterator].gen
                    najlepšie_riesenie_generacia = generacie_iterator

            if (fitnes_min > generacia[jedinec_iterator].fitnes):
                fitnes_min = generacia[jedinec_iterator].fitnes

            #priemer
            priemer += generacia[jedinec_iterator].fitnes

            if (generacia[jedinec_iterator].fitnes == fitnes_goal):
                najdene_riesenie = True
                print("NAŠLO SA RIEŠENIE  GENERACIA Č: " + str(generacie_iterator) + " FITNESS : " + str(generacia[jedinec_iterator].fitnes))
                print("VÝSLEDNÉ POHRABANÉ POLE ")
                for i in range(pos_x):
                    for j in range(pos_y):
                        print(array[i][j], end=" ")
                        if (array[i][j] <= 9 and array[i][j] >= 0):
                            print("", end=" ")
                        # print("]i: " + str(i) + " j: " + str(j) + " [",end= "")
                    print("")
                break
            else:
                # sortnuta generácia
                new_generation = []
                mutovanie_iter = POCET_JEDINCOV / ODKIAL_MUTOVAT

                if (tournament):
                   for i in range(POCET_JEDINCOV):
                       individual1 = tournament_selection(generacia,pocet_genov,POCET_JEDINCOV)
                       individual2 = tournament_selection(generacia,pocet_genov,POCET_JEDINCOV)
                       new_individual = crossover(PRAVDEPODOBNOST_CROSSOVER,individual1, individual2,pocet_genov)
                       new_generation.append(new_individual)
                   array = new_generation
                   sorted_generation = sorted(generacia, key=lambda x: x.fitnes, reverse=True)
                   generacia = sorted_generation
                else:
                    sorted_generation = sorted(generacia, key=lambda x: x.fitnes, reverse=True)
                    generacia = sorted_generation
                    vyber_zaciatok_koniec(POCET_JEDINCOV,pocet_genov,PRAVDEPODOBNOST_KRIZENIE)


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
        print("GENERACIA: " + str(generacie_iterator) + " FITNES MAX: " + str(fitnes_max) + " FITNES MIN: " + str(fitnes_min) + " PRIEMER: " + str(int(priemer/POCET_JEDINCOV)))

    print("---------------------------------------------------")
    print("NAJLEPŠIE RIEŠENIE BOLO:")
    print("FITNESS: "+ str(najlepsie_riesenie_fitnes))
    print("CHYBALO POHRABAŤ " + str((fitnes_goal - najlepsie_riesenie_fitnes)))
    print("GENY: " + str(najlepsie_riesenie_geny))
    print("GENERACIA: " + str(najlepšie_riesenie_generacia))


if __name__ == '__main__':
    main()
