from array import array
from operator import inv
import numpy as np
import os

# ------------------------------------------------------------------------------------------- #
# Matrix functions - maiku"

def print_matrix(matrix): # STAMPA LA MATRICE passata negli argomenti
    print("[#] Here is your matrix")
    print(" ")
    print("A="+ str(matrix))
    if(n == m):print("(nxn)")
    else:print("(nxm)")
    print(" ")

def main_menu(): # MENU PRINCIPALE
    print("[#] Select the operation to perform")
    print("[1] Calcolo det(A)")
    print("[2] Calcolo r(A)")
    print("[3] Trasposta (tA)")
    print("[4] Involutoria (A^2=I)")
    print("[5] Nilpotente [W.I.P.]")
    print("[6] Idempotente (A^2=A)")
    print("[7] Simmetrica (A*tA=A)")
    print("[8] Antisimmetrica [W.I.P.]")
    print("[9] Ortogonale (A*tA=I)")
    print("[10] Invertibile [W.I.P.]")
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

def det_matrice(matrix):
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
    unità = np.full(n*m, 0, dtype='float64')
    unità[0] = 1
    i = 1
    while i < n*n:
        if ((i % (n+1)) == 0):
            unità[i] = 1 
        i = i+1    
    unità = np.reshape(unità, (n, m))
    return unità

def matrice_simmetrica(matrix):
    trans = np.transpose(matrix.astype(float)) 
    trans = np.reshape(trans, (n, m))
    matrix = matrix.astype(float) # casting 'unsafe'
    # CONTROLLO FINALE
    print("# Matrix functions - maiku - Build 1.2.1.0")
    if np.allclose(matrix, trans):
        print("[#] La matrice è simmetrica dato che:")
        print(" ")
        print("A=")
        print(matrix)
        print(" ")
        print("è uguale alla sua trasposta")
        print(" ")
        print("tA=")
        print(trans)
    else:
        print("[#] La matrice NON è simmetrica dato che:")
        print(" ")
        print("A=")
        print(matrix)
        print(" ")
        print("NON è uguale alla sua trasposta")
        print(" ")
        print("tA=")
        print(trans)

def matrice_involutoria(matrix):
    invo = np.linalg.matrix_power(matrix.astype(float), 2)
    unità = np.identity(n) # sopra trovi anche la mia funzione
    # CONTROLLO FINALE
    print("# Matrix functions - maiku - Build 1.2.1.0")
    if np.allclose(invo, unità):
        print("[#] La matrice è involutoria dato che:")
        print(" ")
        print("A=")
        print(matrix)
        print(" ")
        print("moltiplicata per se stessa ha come risultato")
        print(" ")
        print("A^2=")
        print(invo)
        print(" ")
        print("che è uguale alla matrice unità")
        print(" ")
        print("I=")
        print(unità)
    else:
        print("[#] La matrice NON è involutoria dato che:")
        print(" ")
        print("A=")
        print(matrix)
        print(" ")
        print("moltiplicata per se stessa ha come risultato")
        print(" ")
        print("A^2=")
        print(invo)
        print(" ")
        print("che NON è uguale alla matrice unità")
        print(" ")
        print("I=")
        print(unità)  

def matrice_idempotente(matrix):
    idem = np.linalg.matrix_power(matrix.astype(float), 2)
    matrix = matrix.astype(float) # casting 'unsafe'
    # CONTROLLO FINALE
    print("# Matrix functions - maiku - Build 1.2.1.0")
    if np.allclose(matrix, idem):
        print("[#] La matrice è idempotente dato che:")
        print(" ")
        print("A=")
        print(matrix)
        print(" ")
        print("moltiplicata per se stessa ha come risultato")
        print(" ")
        print("A^2=")
        print(idem)
        print(" ")
        print("che è uguale a se stessa (A=A^2)")
    else:
        print("[#] La matrice NON è idempotente dato che:")
        print(" ")
        print("A=")
        print(matrix)
        print(" ")
        print("moltiplicata per se stessa ha come risultato")
        print(" ")
        print("A^2=")
        print(idem)
        print(" ")
        print("che NON è uguale a se stessa (A!=A^2)")

def matrice_ortogonale(matrix):
    trans = np.transpose(matrix.astype(float)) 
    trans = np.reshape(trans, (n, m))
    matrix = matrix.astype(float) # casting 'unsafe'
    orto = np.dot(matrix,trans)
    unità = np.identity(n)
    print("# Matrix functions - maiku - Build 1.2.1.0")
    if np.allclose(orto, unità):
        print("[#] La matrice è ortogonale dato che:")
        print(" ")
        print("A=")
        print(matrix)
        print(" ")
        print("moltiplicata per la sua trasposta")
        print(" ")
        print("tA=")
        print(trans)
        print(" ")
        print("ha come risultato la matrice unità")
        print(" ")
        print("I=")
        print(unità)
    else:
        print("[#] La matrice NON è ortogonale dato che:")
        print(" ")
        print("A=")
        print(matrix)
        print(" ")
        print("moltiplicata per la sua trasposta")
        print(" ")
        print("tA=")
        print(trans)
        print(" ")
        print("ha come risultato la matrice B, diversa dalla matrice unità")
        print(" ")
        print("B=")
        print(orto)

# ------------------------------------------------------------------------------------------- #
# Python matrix using numpy - maiku"
os.system('cls')
print("# Matrix functions - maiku - Build 1.2.1.0")
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
    print("# Matrix functions - maiku - Build 1.2.1.0")
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
                print("# Matrix functions - maiku - Build 1.2.1.0")
                print_matrix(matrix)
                det_matrice(matrix) # FUNZIONE
                x=-1 # ONLY FOR CASE 1 LOOP
                x = end_menu() # END LOOP
                os.system('cls')    
            case 2:
                # Calcolo r(A)
                os.system('cls')
                print("# Matrix functions - maiku - Build 1.2.1.0")
                print_matrix(matrix)
                ran_matrice(matrix) # FUNZIONE
                x = end_menu() # END LOOP 
                os.system('cls')
            case 3:
                # Trasposta (tA)
                os.system('cls')
                print("# Matrix functions - maiku - Build 1.2.1.0")
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
                #matrice_antisimm(matrix) # FUNZIONE
                x = end_menu() # END LOOP 
                os.system('cls')
            case 9:
                # Ortogonale
                os.system('cls')
                matrice_ortogonale(matrix)
                x = end_menu() # END LOOP 
                os.system('cls')
            case 10:
                # Invertibile
                os.system('cls')
                #matrice_invertibile(matrix) # FUNZIONE
                x = end_menu() # END LOOP 
                os.system('cls')
            case -1:
                # Esci
                os.system('cls')
                x = 99    
                
# --maiku