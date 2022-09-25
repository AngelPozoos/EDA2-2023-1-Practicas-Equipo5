import random
def GenerarNumeros(A,k):
    A.append(0)
    for i in range(k-1):
        A.append(random.randint(0, k))

def CountingSort(A,k): # A es la lista y k es el valor máximo de la lista
   C=[0 for _ in range(k+1)]
   B=[0 for _ in range(len(A))]
   for j in range(0,len(A)):
       C[A[j]]=C[A[j]]+1
   for i in range (1,k+1):
       C[i]=C[i]+C[i-1]
   for j in range (len(A)-1,-1,-1):
       B[C[A[j]]-1]=A[j]
       C[A[j]]=C[A[j]]-1
   return B 
   
Condicion=True
while Condicion:
    k=int(input("Ingresa el rango superior de la lista: "))
    if k>10 and k<30:
        A=[]
        GenerarNumeros(A, k)
        print(A)
        A=CountingSort(A,k)
        print(A)
        Condicion=False
    else:
        print("Ingresa valores mayor a 10 y menores a 30")

