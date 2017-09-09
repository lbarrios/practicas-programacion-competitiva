#!/usr/local/bin/python
#-*- coding: utf-8 -*-
P = input()

# Tengo dos arrays, p0 y p1
P0 = P[0]
P1 = P[1]
# quiero tener dos arrays del largo de p0
# para guardar el largo de la mejor opción en 
# cada posición de p0, y la clave correspondiente 
# en p1 a esa opción, respectivamente.
best_P0_vs_P1 = list(P0) # O(len(P0)) < O(len(P))
best_P1_keys_vs_P0 = list(P0) # O(len(P0)) < O(len(P))

# voy a recorrer p1 desde 0 hasta len(p1)-1
p1_index = 0
max_p1_index = len(P1) - 1

for p0_index in xrange(len(P0)): # O(len(P))
    p0_val = P0[p0_index]
    p1_val = P1[p1_index]
    best_P0_vs_P1[p0_index] = abs(p0_val - p1_val)
    best_P1_keys_vs_P0[p0_index] = p1_index
    # voy a iterar, buscando mejores opciones para este índice, siempre y cuando
    # la siguiente opción sea mejor que la que tengo, y me encuentre dentro
    # del rango de p1
    p1_next_val = P1[min(p1_index+1,max_p1_index)]
    while p1_index<max_p1_index and abs(p0_val - p1_next_val)<abs(p0_val - p1_val):
        p1_index+=1
        p0_val = P0[p0_index]
        p1_val = P1[p1_index]
        best_P0_vs_P1[p0_index] = abs(p0_val - p1_val)
        best_P1_keys_vs_P0[p0_index] = p1_index
        p1_next_val = P1[min(p1_index+1,max_p1_index)]
    # if abs(p0_val - p1_next_val)<abs(p0_val - p1_val):
    #     p1_index=p1_next_val
    #     best_P0_vs_P1[p0_index] = abs(p0_val - p1_next_val)
    #     best_P1_keys_vs_P0[p0_index] = p1_index

print "P0=%s"%P0
print "P1=%s"%P1
print "best_P0_vs_P1=%s"%best_P0_vs_P1
print "best_P1_keys_vs_P0=%s"%best_P1_keys_vs_P0

mini_k = 0
mini = best_P0_vs_P1[mini_k]
for k in xrange(len(best_P0_vs_P1)):
    if mini>best_P0_vs_P1[k]:
      mini = best_P0_vs_P1[k]
      mini_k = k
    #print "for k=%s, mini=%s"%(k,mini)
print "\nResultado:"
print "P0[%s]=%s"%(mini_k, P0[mini_k])
print "P1[%s]=%s"%(best_P1_keys_vs_P0[mini_k], P1[best_P1_keys_vs_P0[mini_k]])
start = min(P0[mini_k],P1[best_P1_keys_vs_P0[mini_k]])
end = max(P0[mini_k],P1[best_P1_keys_vs_P0[mini_k]])
print "P[%s:%s]"%(start,end)