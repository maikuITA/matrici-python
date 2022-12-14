from array import array
from operator import inv
import numpy as np
import os
# ------------------------------------------------------------------------------------------- #
# Matrix functions - maiku"

# SYSTEM MESSAGES
maikumatrix = "# Matrix functions - maiku - Build 1.4.5"
toobig = "[#] Wrong matrix size (must be nxn)"

def main_menu(): # MENU PRINCIPALE
    print("[#] Select the operation to perform")
    print("[1] Calcolo det(A)")
    print("[2] Calcolo r(A)")
    print("[3] Trasposta (tA)")
    print("[4] Involutoria (A^2=I)")
    print("[5] Nilpotente (A^n=0)")
    print("[6] Idempotente (A^2=A)")
    print("[7] Simmetrica (tA=A)")
    print("[8] Antisimmetrica (tA=-A)")
    print("[9] Ortogonale (A*tA=I)")
    print("[-1] Exit the program")
    x = int(input(">"))
    return x

def end_menu(): # MENU FINE OPERAZIONE
    print(" ")
    print("[#] Select the operation to perform")
    print("[0] Go back to menu")
    print("[-1] Exit the program")
    x = int(input(">"))
    listx = [-1, 0]
    while(x not in listx):
        os.system('cls')
        print("[#] Select the operation to perform")
        print("[0] Go back to menu")
        print("[-1] Exit the program")
        x = int(input(">"))
    return x    

def print_matrix(matrix): # STAMPA LA MATRICE passata negli argomenti
    print("[#] Here is your matrix")
    print(" ")
    print("A="+ str(matrix))
    if(n == m):print("(nxn)")
    else:print("(nxm)")
    print(" ")

def matrix_too_big():
    if n != m:
        return True
    else:
        return False       

def det_matrice(matrix):
    if(matrix_too_big()):
        print(toobig)
    else:
        det = np.linalg.det(matrix.astype(float)) # CALCOLO det(A)
        print("det(A) = "+ str(int(det)))

def ran_matrice(matrix):    
    rango = np.linalg.matrix_rank(matrix.astype(float)) # CALCOLO r(A)
    print("r(A) = "+str(rango))

def tra_matrice(matrix):
    tra = np.transpose(matrix.astype(float)) # CALCOLO tra(A)
    print("tA=")
    print(tra)

def matrice_unita(): # CALCOLO MATRICE UNITA' (per ogni n dato che n=m) fatta da me
    unit?? = np.full(n*m, 0, dtype='float64')
    unit??[0] = 1
    i = 1
    while i < n*n:
        if ((i % (n+1)) == 0):
            unit??[i] = 1 
        i = i+1    
    unit?? = np.reshape(unit??, (n, m))
    return unit??

def matrice_simmetrica(matrix):
    if(matrix_too_big()):
        print(toobig)
    else:
        trans = np.transpose(matrix.astype(float)) # casting 'unsafe'
        trans = np.reshape(trans, (n, m))
        matrix = matrix.astype(float) # casting 'unsafe'
        # CONTROLLO FINALE
        print(maikumatrix)
        if np.allclose(matrix, trans):
            print("[#] La matrice ?? simmetrica dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("?? uguale alla sua trasposta")
            print(" ")
            print("tA=")
            print(trans)
        else:
            print("[#] La matrice NON ?? simmetrica dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("NON ?? uguale alla sua trasposta")
            print(" ")
            print("tA=")
            print(trans)

def matrice_antisimmetrica(matrix):
    if(matrix_too_big()):
        print(toobig)
    else:
        trans = np.transpose(matrix.astype(float)) # casting 'unsafe'
        trans = np.reshape(trans, (n, m))
        matrix = matrix.astype(float) # casting 'unsafe'
        matrix = matrix * -1
        # CONTROLLO FINALE
        print(maikumatrix)
        if np.allclose(matrix, trans):
            print("[#] La matrice ?? antisimmetrica dato che:")
            print(" ")
            print("tA=")
            print(trans)
            print(" ")
            print("?? uguale a -A")
            print(" ")
            print(matrix)
        else:
            print("[#] La matrice NON ?? antisimmetrica dato che:")
            print(" ")
            print("tA=")
            print(trans)
            print(" ")
            print("NON ?? uguale a -A")
            print(" ")
            print(matrix)

def matrice_involutoria(matrix):
    if(matrix_too_big()):
        print(toobig)
    else:
        invo = np.linalg.matrix_power(matrix.astype(float), 2)
        unit?? = np.identity(n) # sopra trovi anche la mia funzione
        # CONTROLLO FINALE
        print(maikumatrix)
        if np.allclose(invo, unit??):
            print("[#] La matrice ?? involutoria dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("moltiplicata per se stessa ha come risultato")
            print(" ")
            print("A^2=")
            print(invo)
            print(" ")
            print("che ?? uguale alla matrice unit??")
            print(" ")
            print("I=")
            print(unit??)
        else:
            print("[#] La matrice NON ?? involutoria dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("moltiplicata per se stessa ha come risultato")
            print(" ")
            print("A^2=")
            print(invo)
            print(" ")
            print("che NON ?? uguale alla matrice unit??")
            print(" ")
            print("I=")
            print(unit??)  

def matrice_nilpotente(matrix):
    if(matrix_too_big()):
        print(toobig)
    else:
        nulla = np.zeros((n,m)) # MATRICE NULLA
        nil = False
        for i in range(1, n+1):
            nilpotente = np.linalg.matrix_power(matrix.astype(float), i) # A^n
            if np.allclose(nilpotente, nulla): # CONTROLLO SE A = 0
                nil = True
                index = i
                break
        # CONTROLLO FINALE
        print(maikumatrix)
        if nil:
            print("[#] La matrice ?? nilpotente dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("elevata alla "+str(index)+"a")
            print(" ")
            print("A^"+str(index)+"=")
            print(nilpotente)
            print(" ")
            print("?? uguale alla matrice nulla")
        else:
            print("[#] La matrice NON ?? nilpotente dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("non ci sono n per i quali A^n ?? uguale alla matrice nulla (0)")

def matrice_idempotente(matrix):
    if(matrix_too_big):
        print(toobig)
    else:
        idem = np.linalg.matrix_power(matrix.astype(float), 2)
        matrix = matrix.astype(float) # casting 'unsafe'
        # CONTROLLO FINALE
        print(maikumatrix)
        if np.allclose(matrix, idem):
            print("[#] La matrice ?? idempotente dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("moltiplicata per se stessa ha come risultato")
            print(" ")
            print("A^2=")
            print(idem)
            print(" ")
            print("che ?? uguale a se stessa (A=A^2)")
        else:
            print("[#] La matrice NON ?? idempotente dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("moltiplicata per se stessa ha come risultato")
            print(" ")
            print("A^2=")
            print(idem)
            print(" ")
            print("che NON ?? uguale a se stessa (A!=A^2)")

def matrice_ortogonale(matrix):
    if(matrix_too_big):
        print(toobig)
    else:
        trans = np.transpose(matrix.astype(float)) 
        trans = np.reshape(trans, (n, m))
        matrix = matrix.astype(float) # casting 'unsafe'
        orto = np.dot(matrix,trans)
        unit?? = np.identity(n)
        print(maikumatrix)
        if np.allclose(orto, unit??):
            print("[#] La matrice ?? ortogonale dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("moltiplicata per la sua trasposta")
            print(" ")
            print("tA=")
            print(trans)
            print(" ")
            print("ha come risultato la matrice unit??")
            print(" ")
            print("I=")
            print(unit??)
        else:
            print("[#] La matrice NON ?? ortogonale dato che:")
            print(" ")
            print("A=")
            print(matrix)
            print(" ")
            print("moltiplicata per la sua trasposta")
            print(" ")
            print("tA=")
            print(trans)
            print(" ")
            print("ha come risultato la matrice B, diversa dalla matrice unit??")
            print(" ")
            print("B=")
            print(orto)

# ------------------------------------------------------------------------------------------- #
# Python matrix using numpy - maiku"
os.system('cls')
print(maikumatrix)
n = int(input("[#] Insert the row number > "))
m = int(input("[#] Insert the column number > "))

# Giving a shape to the matrix
matrix = np.full(n*m, 0, dtype='float64')

# Emptying the matrix
for i in range(0, matrix.size):
    matrix = np.delete(matrix, 0, 0)

print("[#] Filling the matrix")
for i in range(0, n):
    for j in range(0, m):
        j = (input(">"))
        matrix = np.append(matrix, j)
matrix = np.reshape(matrix, (n, m))

# Menu selection
os.system('cls')
x = 0
while x != 99:
    print(maikumatrix)
    print_matrix(matrix)
    # MENU SYSTEM
    if(x == 0):
        x = main_menu() # MAIN LOOP
    else:
        # SWITCH SYSTEM
        match x:
            case 1:
                # Calcolo det(A)
                os.system('cls')
                print(maikumatrix)
                print_matrix(matrix)
                det_matrice(matrix) # FUNZIONE
                x=-1 # ONLY FOR CASE 1 LOOP
                x = end_menu() # END LOOP
                os.system('cls')    
            case 2:
                # Calcolo r(A)
                os.system('cls')
                print(maikumatrix)
                print_matrix(matrix)
                ran_matrice(matrix) # FUNZIONE
                x = end_menu() # END LOOP 
                os.system('cls')
            case 3:
                # Trasposta (tA)
                os.system('cls')
                print(maikumatrix)
                print_matrix(matrix)
                tra_matrice(matrix) # FUNZIONE
                x = end_menu() # END LOOP 
                os.system('cls')
            case 4:
                # Involutoria (A^2 = I)
                os.system('cls')
                matrice_involutoria(matrix) # FUNZIONE
                x = end_menu() # END LOOP
                os.system('cls')
            case 5:
                # Nilpotente
                os.system('cls')
                matrice_nilpotente(matrix)
                x = end_menu() # END LOOP                
                os.system('cls')
            case 6:
                # Idempotente
                os.system('cls')
                matrice_idempotente(matrix) # FUNZIONE
                x = end_menu() # END LOOP
                os.system('cls')
            case 7:
                # Simmetrica
                os.system('cls')
                matrice_simmetrica(matrix) # FUNZIONE
                x = end_menu() # END LOOP
                os.system('cls')
            case 8:
                # Antisimmetrica
                os.system('cls')
                matrice_antisimmetrica(matrix) # FUNZIONE
                x = end_menu() # END LOOP 
                os.system('cls')
            case 9:
                # Ortogonale
                os.system('cls')
                matrice_ortogonale(matrix)
                x = end_menu() # END LOOP 
                os.system('cls')
            case -1:
                # Esci
                os.system('cls')
                x = 99  
            case other:
                x = 0 
                os.system('cls')     
                
# --maiku