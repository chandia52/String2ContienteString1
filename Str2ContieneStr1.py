from collections import Counter
str1 = input("Ingrese su primer cadena:")
str2 = input("Ingrese su segunda cadena:")
def contiene(str1,str2):
        str1 = Counter(str1)
        str2 = Counter(str2)
        if str1 & str2 == str1:
            print (True)
        else: 
            print(False)    

contiene(str1,str2)

