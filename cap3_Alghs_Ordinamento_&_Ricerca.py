
def bubble_sort(elements):  #BUBBLE SORT
    last_elem_index = len(elements)-1
    for pass_no in range(last_elem_index, 0, -1):
    #'cammina' all'indietro, ad ogni cycle il max sara tutto a dx, duqnue si toglie -1 da controllare x il prossimo cycle
        swapped = False
        for idx in range(pass_no):
            if elements[idx] > elements[idx+1]:
                elements[idx], elements[idx+1] = elements[idx+1], elements[idx]  #inverte i valori
                swapped = True
        if not swapped:
            #se non c'è stato nemmeno uno swap, allora la lista è gia ordinata, chiudi tutto e return il result
            break
    return elements

def insertion_sort(elements):  #INSERTION SORT
    for i in range(1, len(elements)):
        key = elements[i]       # elemento current chiave
        j = i - 1
        while j >= 0 and elements[j] > key:
            elements[j + 1] = elements[j]     #first cicle here diventa [5, 5, 6, 1, 3]
            j -= 1  #first cycle here j diventa da 0 a -1
        elements[j + 1] = key   #first cycle here j=0, modifico questo elemento = key
    return elements   #first cycle result [2, 5, 6, 1, 3]

def merge_sort(elements):  #MERGE SORT, divide et impera!
    if len(elements) <= 1:
        return elements
    mid = len(elements) // 2  #// is divisione intera e.g. 5//2 =2, quindi se ci sono 5 elems, 2 andranno in left e 3 in right
    left = elements[:mid]   #create new list
    right = elements[mid:]  #create new list

    merge_sort(left)  #non continuare il codice, finche non ti viene restituito qualcosa dall'interno. stessa cosa per tutti i figli interni.
    merge_sort(right)
    #-- first cycle here arrive WHEN elements = 2items, merge_sort(left)->ha eseguito merge_sort(with 1 item) e gli è stato restituito, same for merge_sort(right)

    a,b,c = 0,0,0  #a x scandire left, b x scandire right, c x index in list Elements
    while a<len(left) and b<len(right):  #gira solo fino a quando o A o B hanno scandito tutti i loro items nella loro lista
        if left[a] < right[b]:
            elements[c] = left[a]  #first cycle modifica item in index 0 in lista originale
            a += 1  #first cycle avanza di 1index per lista left
        else:
            elements[c] = right[b]
            b += 1
        c += 1  #first cycle avanza di 1 index su lista originale

    while a<len(left):  #se ci sono altri elementi nella meta sx
        elements[c] = left[a]
        a += 1
        c += 1
    while b<len(right):  #se ci sono altri elementi nella meta dx
        elements[c] = right[b]
        b += 1
        c += 1
    return elements  #fist cycle here elements=2items, ora questi 2items sono ordinati
    #ora si confronterà con i risultati dell'altro ramo (che anche lui aveva elements=2 oppure elements=1 )

def shell_sort(elements):   #[5, 2, 6, 1, 3]
    distance = len(elements) //2  #first cycle 5//2 =2
    while distance >0:  #first cycle finche è 2>0
        for i in range(distance, len(elements)):  #2->5(dunque 2-3-4)
            temp = elements[i]  #firstcycle temp=6
            j=i  #fc  j=2
            while j >=distance and elements[j-distance] >temp:  #fc 2>=2 && elements[0]>temp
                elements[j] = elements[j-distance]  #secondcycle now list is [5, 2, 6, 2, 3]
                j= j-distance  #secondcycle j=1
            elements[j] = temp  #assegni, ma cmnq rimane uguale
            #NEW CYCLE where i will be 3, temp=elements[3], j=3, distance always =2
            #NEW CYCLE where i will be 4, temp=elements[4], j=4, distance always =2
        distance = distance//2
        #NEW CYCLE where distance will be =1,   inner FC  i=1 temp=elements[1] j=1
    return elements

def selection_sort(elements):  #[5, 2, 6, 1, 3]
    for fill_slot in range(len(elements)-1, 0, -1):  #fc 4->0 (quindi 4-3-2-1)
        max_index =0  #fc fill_slot=4
        for location in range(1, fill_slot+1):  #fc 1->5 (quindi 1-2-3-4) | sc(secondcycle) solo 1->4(quindi 1-2-3) dunque non controlla l'ultimo item(che è quello piu Big trovato ne Cycle precedente)
            if elements[location] > elements[max_index]:
                max_index = location
        elements[fill_slot], elements[max_index] = elements[max_index], elements[fill_slot]
           #scambia di posto, quindi in posizione [fill_slot] finirà l'item piu big selezionato da max_index. per il prossimo cycle fill_slot sarà uno in meno quindi questo item non verrà piu toccato
    return elements



list1 = [5, 2, 6, 1, 3]
list2 = [9, 2,  6, 1, 5,  4,3,8]
print(bubble_sort(list1))
print(insertion_sort(list1))
print(merge_sort(list2))
print(shell_sort(list1))
print(selection_sort(list1))


