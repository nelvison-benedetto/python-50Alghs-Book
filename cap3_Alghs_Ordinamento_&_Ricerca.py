
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

# def bubble_sort(elements):  #solo un po piu leggibile 
#   for i in range(len(elements)-1, 0, -1):
# 	swapped = False
# 	for j in range(i):
# 	   if(elements[j]> elements[j+1]):
# 		elements[j], elements[j+1] = elements[j+1], elements[j]
# 		swapped = true;
# 	if not swapped:
# 	   break;
#   return elements

def selection_sort(elements):  #[5, 2, 6, 1, 3]
    for fill_slot in range(len(elements)-1, 0, -1):  #fc 4->0 (quindi 4-3-2-1)  cammini all'indietro
        max_index = 0   #fc fill_slot=4
        for location in range(1, fill_slot+1):  #fc 1->5(4+1) (quindi 1-2-3-4) | sc(secondcycle) solo 1->4(quindi 1-2-3) dunque non controlla l'ultimo item(che è quello piu Big trovato ne Cycle precedente)
            if elements[location] > elements[max_index]:
                max_index = location   
        #ora il puntatore max_index punta all'item piu grande
        elements[fill_slot], elements[max_index] = elements[max_index], elements[fill_slot]
           #scambia di posto, quindi in posizione [fill_slot] finirà l'item piu big selezionato da max_index. per il prossimo cycle fill_slot sarà uno in meno quindi questo item non verrà piu toccato
    return elements

# def selection_sort(elements):  #solo un po più leggibile
#   for i in range( len(elements)-1, 0, -1 ):
#      max_idx = 0;
#      for j in range(1, i+1):  #xk deve contare anche l'i stesso
#          if( elements[j] > elements[max_idx]):
#              max_idx = j
#      elements[i], elements[max_idx] = elements[max_idx], elements[i]
#   return elements

def insertion_sort(elements):  #INSERTION SORT
    for i in range(1, len(elements)):  #se l'arr è 5 elementi, allora fa 1-2-3-4 non include il 5!
        key = elements[i]       # elemento current chiave
        j = i - 1
        while j >= 0 and elements[j] > key:
            elements[j + 1] = elements[j]     #first cicle here diventa da [5, 2, 6, 1, 3] a  [5, 5, 6, 1, 3]
            j -= 1  #first cycle here j diventa da 0 a -1
        elements[j + 1] = key   #first cycle here j=0, modifico questo elemento = key, first cycle here diventa [2, 5, 6, 1, 3]
        #qua cmnq la lista elements viene continuamente modificata ad ogni ciclo, e viene riusata nel prossimo ciclo
    return elements   #classico return finale per dare la risposta ultimata


def merge_sort(elements):  #MERGE SORT, divide et impera! 🔥 (anche nei casi peggiori è stabile, ideale x grandi datasets)
    if len(elements) <= 1:
        return elements
    mid = len(elements) // 2  #// is divisione intera e.g. 5//2 =2, quindi se ci sono 5 elems, 2 andranno in left e 3 in right
      #NON USARE (0+(len(elems)-1))//2 !!quello va bene solo x binary_search , altrimenti qua elems=2 sarebbe mid=0 quindi con left e right fanno ricorsione infinita error StackOverflow!
    left = elements[:mid]   #create new list
    right = elements[mid:]  #create new list

    merge_sort(left)  #non continuare il codice, finche non ti viene restituito qualcosa dall'interno. stessa cosa per tutti i figli interni.
    merge_sort(right)
    #-- first cycle here arrive WHEN elements = 2items, merge_sort(left)->ha eseguito merge_sort(with 1 item) e gli è stato restituito, same for merge_sort(right)
    #-- second cycle here arrive WHEN ritornano i 2 segmenti piu piccoli possibili (2elements ora ordinati)-(2elements ora ordinati) or (2elements ora ordinati)-(1elements)

    a,b,c = 0,0,0  #a x scandire left, b x scandire right, c x index in list Elements
    while a<len(left) and b<len(right):  #gira solo fino a quando o A o B hanno scandito tutti i loro items nella loro lista
        if left[a] < right[b]:
            elements[c] = left[a]  #first cycle modifica item in index 0 in lista originale (di questo segmento)
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

def shell_sort(elements):   #[5, 2, 6, 1, 3] ,  anche se è migliore di Insertion, Bubble o Selection Sort, NON supera MergeSort, TimSort o QuickSort ed è anche non stabile(non garantisce di mantenere l'ordine tra elementi equivalenti)
    distance = len(elements) //2  #first cycle 5//2 =2
    while distance >0:  #first cycle finche è 2>0
        for i in range(distance, len(elements)):  #2->5(dunque 2-3-4) , quindi fc elements [6,1,3]
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


def quick_sort(elements):  #🔥 O(n^2)(ma normalmente è O(n log n)), è stabile, è veloce(in media), su array enormi puo dare err RecursionError. [5, 2, 6, 1, 3] 
      #here è non-inplace per didattica, ma la versione reale non crea nuove liste temps ma sposta gli elements
    if len(elements) <= 1:
        return elements
    pivot = elements[ len(elements) // 2 ]   # fc pivot = elements[1] #qua in realta ci serve solo un valore random della lista, non necessariamente il medio. dunque si puo fare anche pivot=random.choice(elements)
       #NON USARE (0+(len(elems)-1))//2 !!quello va bene solo x binary_search
    left, middle, right = [], [], [] #arrays con rispettivamente solo i valori: minori del pivot, equali al pivot, maggiori del pivot.
    for item in elements:
        if item == pivot:
            middle.append(item)
        elif item < pivot:
            left.append(item)
        else:  #item > pivot
            right.append(item)
    # left = [x for x in elements if x < pivot]  #array con tutti gli elementi di valore minore del pivot
    # middle = [x for x in elements if x == pivot]  #array con tutti gli elementi di valore uguale al pivot
    # right = [x for x in elements if x > pivot]  #array con tutti gli elementi di valore maggiore del pivot
    return quick_sort(left) + middle + quick_sort(right)  #concatena i pezzi ordinandoli, e passa il result all'annidamento superiore


def partition3_Xquicksortrandom(A, l, r):
    """
    3-way partitioning
    - A[l..r] is partitioned into:
        A[l..m1-1] < pivot
        A[m1..m2] == pivot
        A[m2+1..r] > pivot
    Returns (m1, m2)
    """
    pivot = A[l]
    m1 = l       #first index of pivot
    m2 = l       #last index of pivot
    for i in range(l + 1, r + 1):
        if A[i] < pivot:
            m1 += 1
            A[i], A[m1] = A[m1], A[i]  # swap element < pivot to left
            if m1 != m2:
                m2 += 1
                A[i], A[m2] = A[m2], A[i]  # shift equal pivot to middle
        elif A[i] == pivot:
            m2 += 1
            A[i], A[m2] = A[m2], A[i]      # swap element == pivot to middle
    A[l], A[m1] = A[m1], A[l]  # move pivot to its final place
    return m1, m2
def quick_sort_randomized(A, l=0, r=None):   #🔥🔥🔥 non è stabile(non garantisce di mantenere l'ordine tra elementi equivalenti)
    """
    QuickSort ottimizzato con:
    -pivot random: riduce enormemente per prob di avere caso peggiore O(n**2)
    -3-way partitioning: ricude enormemente squilibli con molti cloni ed eviti ricursioni inutili. scegli pivot x,metti a sx gli elems <x,  dx gli elems >x, al centro quelli ==x, 
        #ottieni indexes m_1 and m_2 che delimitano il segmento ==x. 
    -tail recursion sulla metà più grande convertita in loop: riduci profondita massima delle ricursione O(logn) (in media) 
       #facendo ricorsione sul segmento piu small, e per il segmento big usi while().
    #w pivot riandom+3-way partition ottieni i segmenti bilanciati(cioe che sono +- della stessa length), dunque la profondita ricorsiva è log_n
       #(se fosse sbilanciato cioe pivot sempre min/max profondita ricorsiva +- n. quindi il caso peggiore sarebbe O(n**2))
    """
    if r is None:
        r = len(A) - 1
    while l < r:  # loop per sostituire la ricorsione sulla metà più grande
        # scegliere un pivot casuale e metterlo all'inizio
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        # partizionamento in 3 parti
        m1, m2 = partition3_Xquicksortrandom(A, l, r)
        # ricorsione solo sulla metà più piccola
        if (m1 - l) < (r - m2):
            quick_sort_randomized(A, l, m1 - 1)
            l = m2 + 1  # tail recursion sulla metà più grande
        else:
            quick_sort_randomized(A, m2 + 1, r)
            r = m1 - 1  # tail recursion sulla metà più grande
    return A


def heap_sort(elements):   #O(n log n), non è stabile, è in-place, va bene anche per array molto grandi
    n = len(elements)
    def heapify(arr, n, i):  # serve per mantenere la proprietà dell'heap (padre >= figli)
        largest = i           # supponiamo che la radice sia il più grande
        left = 2 * i + 1      # figlio sinistro
        right = 2 * i + 2     # figlio destro
        # se il figlio sinistro esiste ed è maggiore della radice
        if left < n and arr[left] > arr[largest]:
            largest = left
        # se il figlio destro esiste ed è maggiore del massimo trovato finora
        if right < n and arr[right] > arr[largest]:
            largest = right
        # se il massimo non è la radice, scambia e continua a sistemare ricorsivamente
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            heapify(arr, n, largest)
    # 1. Costruzione dell'heap massimo (max-heap)
    # Partiamo dal primo nodo non-foglia e risaliamo fino alla radice
    for i in range(n // 2 - 1, -1, -1):
        heapify(elements, n, i)
    # 2. Estrazione degli elementi uno per uno
    # spostiamo la radice (massimo) in fondo, riduciamo la dimensione dell'heap, e sistemiamo con heapify
    for i in range(n - 1, 0, -1):
        elements[0], elements[i] = elements[i], elements[0]  # sposta il massimo in fondo
        heapify(elements, i, 0)  # sistema l'heap con la radice ridotta
    return elements


#def intro_sort()  #🔥(quick_sort + se sta andando male passa a heap_sort), non è stabile, è in-place, è robusto
  #un problema del quick_sort è che se array è gia ordinato ed pivot scelto male, algh degrada a O(n**2)
  #intro_sort invece parte come quick_sort, ma se la profondità della ricorsione supera c log n (dunque il partizionamento sta andando male),
    #passa a heap_sort (che è un O(nlogn))(e rimane anche in-place!)


#def tim_sort(elements, run=2):   #🔥(standart in enterprise & standart predefinito in molti linguaggi (e.g.JAVA), è stabile, è adattivo, O(n log n) nel caso peggiore, è ottimo su dati del real world(dove cmnq i dati arrivano gia ordinati/parzialmente ordinati)) 
   #combina insertion_sort (per creare dei segmenti gia ordinati) + merge_sort     #here run piccolo per esempio, 
def insertion_sort_TIM(arr, left, right):
    """Insertion sort limitato tra left e right inclusi"""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def merge_TIM(arr, l, m, r):
    """Merge tra due sottoliste ordinate: arr[l:m+1] e arr[m+1:r+1]"""
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
def tim_sort(arr):
    n = len(arr)
    RUN = 32
    # 1️⃣ Ordina ogni blocco piccolo con insertion sort
    for start in range(0, n, RUN):
        end = min(start + RUN - 1, n - 1)
        insertion_sort_TIM(arr, start, end)
    # 2️⃣ Fai il merge dei blocchi in modo progressivo
    size = RUN
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2*size - 1), (n - 1))
            if mid < right:
                merge_TIM(arr, left, mid, right)
        size *= 2
    return arr


# IntroSort (Quick + Heap fallback): standard in C++ STL (std::sort) → molto comune in applicazioni enterprise.
# Heap Sort: complessità O(n log n) garantita, ma in pratica più lento di quick/merge → usato come fallback in introsort.
# Radix Sort / Counting Sort: O(n) su casi specifici (chiavi numeriche limitate) → molto usato in sistemi embedded, grafica, compilatori.

list1 = [5, 2, 6, 1, 3]
list2 = [9, 2,  6, 1, 5,  4,3,8]
list3 = [2,3,4,5,6]
list4 = [2, 4, 6, 9, 12, 18, 24]

print(bubble_sort(list1))
print(insertion_sort(list1))
print(merge_sort(list2))
print(shell_sort(list1))
print(selection_sort(list1))
print(quick_sort(list1))

###########################Searching Alghs

def linear_search(elements,item):
    index = 0
    isFound = False
    while index <len(elements) and isFound is False:  #itera per ciascuno item della lista e lo compara con l'item da trovare dato
        if elements[index] == item:
            isFound = True
        else:
            index = index +1
    return isFound

def binary_search(elements,item):  #🔥 #[2,3,4,5,6][3]  per funzionare gli elements devono già essere ordinati
    first = 0
    last = len(elements)-1  #fc  =4     #importante -1 !!
    isFound = False
    while first <=last and not isFound:  #!importante <= !!
        midpoint = (first+last) //2  #divisione intera
          #mid=first+(last-first)/2;  in c++/java questo è pro per evitare stackoverflow se first e last sono davvero bigs
        if elements[midpoint] == item:
            return True
        else:  #consideri o la parte sx o la parte dx di Midpoint, l'altra parte la  butti e non verrà mai piu utilizzata
            if item <elements[midpoint]:
                last = midpoint -1
            else:
                first = midpoint +1
    return False

def interpolation_search(elements,item):  #[2, 4, 6, 9, 12, 18, 24][18]  per funzionare gli elements devono già essere ordinati
    idx0 = 0
    idxn = (len(elements)-1)  #fc  =6
    isFound = False
    while idx0 <= idxn and item >= elements[idx0] and item <= elements[idxn]:

        if elements[idxn] == elements[idx0]:  #evita divisione per zero
            if elements[idx0] == item:
                return True
            else:
                return False

        mid = idx0 + int(   (   ( float(idxn-idx0) / (elements[idxn] - elements[idx0]) )   *   (item - elements[idx0])  )  )
          #formula interpolazione lineare, fc mid=4 | sc(secondcycle) mid=5
        if elements[mid] == item:
            return True
        if elements[mid] < item:  #fc execute this
            idx0 = mid +1  #x next cycle seziono(prendo in consideraione) solo la parte a dx di mid
        else:
            idxn = mid - 1
    return False


print(linear_search(list1,2))
print(binary_search(list3,3))
print(interpolation_search(list4,18))

#in reality in enterprise su big datasets si utilizzno:
#binarysearch su array ordinati poco dinamici,
#Hashing (python->dict/set,java->HashMap,HashSet,C#->Dictionary,HashSet),  //ricerca superveloce
#alberi bilanciati (python->blist,bintrees java->TreeMap,TreeSet C#->SortedDictionary,SortedSet)  //se ti serve completo CRUD oltre che alla ricerca

