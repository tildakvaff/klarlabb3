
from bintreeFileengelska import Bintree



#Lägger in de svenska orden i ett binärt träd som kallas svenska --> den kod vi fått i uppgiftsbeskrivningen
svenska = Bintree()
with open("Laboration 3\word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()              # Ett trebokstavsord per rad
        if ordet in svenska:            #om ordet redan finns i trädet kommer dubletten skrivas ut. Det kommer inte finnas några dubletter i trädet men alla ord finns med
            print(ordet, end = " ") 
            
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")




#skapar ett träd med engelska ord
engelska = Bintree()

#funktion som läser raderna från filen och sparar varje ord i en lista
def läs_in_engelska():
    engelsk_ordlista = []
    with open("Laboration 3\engelska.txt", "r", encoding = "utf-8") as engelskfil:
        for rad in engelskfil:
            for ord in rad.split():
                engelsk_ordlista.append(ord)
        return engelsk_ordlista


#funktion som rensar lista på tecken
def ta_bort_tecken(engelsk_ordlista):
    tecken1 = '"'
    tecken2 = ','
    tecken3 = '.'
    tecken4 = '!'
    borttagning1 = [element.replace(tecken1, '') for element in engelsk_ordlista]
    borttagning2 = [element.replace(tecken2, '') for element in borttagning1]
    borttagning3 = [element.replace(tecken3, '') for element in borttagning2]
    borttagning4 = [element.replace(tecken4, '') for element in borttagning3]
    return borttagning4

#funktion som gör alla bokstäver små i orden. Vissa ord förekommer 2 gånger fast med stora resp. små bokstäver. Programmet ser inte att orden är "samma" då
def små_bokstäver(engelsk_ordlista):
    ord_små =[]
    for ord in engelsk_ordlista:
        ord_små.append(ord.lower())
    return ord_små


#lägger in de engelska orden i det engelska träder
def lägg_in_träd(engelsk_ordlista):
    for ord in engelsk_ordlista:
        if ord in engelska:
            pass #Om ordet redan fanns gör du ingenting --> instruktion från uppgiftsbeskrivningen
        else:
            if ord in svenska: #här sker jämförelse. Om ett ord som ska läggas in i trädet också finns i det svenska trädet kommer det att printas
                print(ord)
                engelska.put(ord)
            else:
                pass
            



#_____________________________ANROP__________________________________
lista = läs_in_engelska()
formaterad_lista = ta_bort_tecken(lista)
engelsk_lista = små_bokstäver(formaterad_lista)

lägg_in_träd(engelsk_lista)






































# def läs_in_svenska():
#     svensk_ordlista = []
#     with open("Laboration 3\word3.txt", "r", encoding = "utf-8") as svenskfil:
#         for rad in svenskfil:
#             for ord in rad.split():
#                 svensk_ordlista.append(ord)
#     return svensk_ordlista




# def ta_bort_dubletter(engelsk, svensk):
#     matches = [i for i in engelsk if i in svensk]
#     return matches





# svensk_lista = läs_in_svenska()

# matchningar = ta_bort_dubletter(engelsk_lista, svensk_lista)

# for varje_ord in matchningar:
#     engelska.put(varje_ord)


# print(engelska.write())





















































