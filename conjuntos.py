# #set un conjunto no tiene elementos duplicados

# import this
# setconuntries= {'col', 'mex', 'bol', 'col'}
# print(setconuntries)
# print(type(setconuntries))

# setfrom= set('hola')
# print(setfrom)

# setfromtuples= set(('abc', 'cde', 'abc'))
# print(setfromtuples)

# numbers=[1, 2, 3, 1, 2, 3]
# setnumbers=set(numbers)
# print(setnumbers)
# uniqueNumbers=list(setnumbers)
# print(uniqueNumbers)

# #como modificar conjuntos
# #tamaño del conjunto
# setconuntries = {'col', 'mex', 'bol' }
# size=len(setconuntries)
# #print(size)
# #print('col' in setconuntries)

# #adicionar al conjunto
# setconuntries.add('pe')
# #print(setconuntries)

# #sumar un conjunto con otro

# setconuntries.update({'arg', 'ecua', 'pe'})
# #print(setconuntries)

# #remover elementos de los conjuntos
# setconuntries.remove('col')
# #print(setconuntries)

# setconuntries.remove('arg')
# #print(setconuntries)

# setconuntries.discard('bol')
# print(setconuntries)
# setconuntries.clear()
# print(setconuntries)
# print(len(setconuntries))

#Combinar conjuntos creando uno mas
# setA={'col', 'bol', 'mex'}
# setB={'pe', 'ven', 'col'}
# setC=setA.union(setB)
# #print(setC)
# #print(setA|setB)

# #intersection, este creando otro conjuntos nos da los conjuntos en común
# setD=setA.intersection(setB)
# print(setD)
# print(setA&setB)

#differrence diferencia entre un conjunto y otro lo resta y no da error
# setDifference= setA.difference(setB)
# print(setDifference)
# print(setB-setA)

#diferencia simetrica combina uno con el otro sin los que se repiten
# setDifSime=setA.symmetric_difference(setB)
# print(setDifSime)
# print(setB^setA)

# countries = {"MX", "COL", "ARG", "USA"}
# northAm = {"USA", "CANADA"}
# centralAm = {"MX", "GT", "BZ"}
# southAm = {"COL", "BZ", "ARG"}
# new_set=countries.union(northAm, centralAm, southAm)
# print(new_set)

#list convergention

numbers=[]
for element in range (1,11):
    numbers.append(element)
print(numbers)
