

#########DP (Dynamic Programming)

# Knapsack(W):   #using repetitions(l'item ha disponibilita illimitata)
# value(0)<-0
# for w from 1 to W:
#   value(w)<-0
#   for i from 1 to n:
#      if w_1<=w:
# 	value<-value(w-w_1)+v_1  #item clones illimitati
# 	if val>value(w):
# 	  value(w)<-val
# return value(W)

# Knapsack(W):   #no repetitions (0/1)(1 sola versione di quell'item da mettere nello zaino)
# initialize all value(0,j)<-0
# initialize all value(w,0)<-0
# for i from 1 to n:
#   for w from 1 to W:
#      value(w,i)<-value(w,i-1)
#      if w_1<=w:
#  	val<-value(w-w_1,i-1)+v_1  #item clones solo 1
# 	if value(w,i)<val
# 	  value(w,i)<-val
# return value(W,n)

# for i from 1 to n:  //better use this O(W) (quello nel code now is O(n*W))
#    for w from W downto w_i:
#        value(w) = max(value(w), value(w-w_i)+v_i)


# Knapsack(W):   #ricorsive + memoization using top-down
# if w is in hash table:
#   return value(w)
# value(w)<-0
# for i from 1 to n:
#    if w_1<= w:
#      val<-Knapsack(w-w_1)+v_1
#      if val>value(w)
#        value(w)<-val
# insert value(w) into hash table with key w
# return value(w)
#O(n*W) dove n è il numero di items e W la capacità massima

#remember than the use of iterative algh is faster than recursion since it han no recursion overhead.
#ci sono casi quando non hai bisogno di clacolare il sottoproblema, e.g. se W e w_i sono multipli di 100, allora il valore w non è necessario se w non è divisibile per 100.

