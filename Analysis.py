import numpy as np
from matplotlib import pyplot as plt

###########_______________Welcome_____________##########

print("\n_____________  Analysis of Cantilever Beam  ___________\n")
print('\n|               P\n|--------------\u2192\n|       L')


############-----------Data--------##########
L = float(input("\nEnter the length of the beam 'L' in mm: "))
P = float(input("Enter the magnitude of force 'P' in N: "))
E = float(input("Enter the modulous of elasticity 'E' of material in N/mm^2: "))
print("\nConsidering Circular Beam\n")

# b = float(input("Enter the width of the beam in mm: "))
# d = float(input("Enter the depth of the beam in mm: "))
A = float(input("Enter the Area of the beam in mm^2: "))

print('\n|               P\n|-- -- -- -- -- --\u2192\n\
|\n  Number of pieces  \n    ')

n = int(input("Enter the number of elements: "))


########------------Matrix formulation and Assembly--------##########

k_local = np.array([[1,-1],[-1,1]])
k_global = np.zeros((n+1, n+1))

#Assembly of elements
for i in range(n):
    k_temp = np.zeros((n+1, n+1))
    k_temp[i:i+2, i:i+2] = k_local
    k_global += k_temp

print("Global Stiffness Matrix: " , k_global)
k_global = n*((A*E)/L)*k_global


########------------Boundary condition deleting the first row and first col--------##########
k_global = np.delete(k_global, 0, 0)
k_global = np.delete(k_global, 0, 1)
        

# force matrix
F = np.zeros(n)
F[-1] = P

# displacement matrix
u = np.linalg.solve(k_global,F)

print("Displacement in element: ", u)


########------------Stress Calculation---------##########

#Stress matrix
S = u.copy()
print(S)

for i in range(n-1):
    S[i+1] = S[i+1] - u[i]


l = L/n         #length of element
S = (E/l)*S
print("stress in element: ",S) 


########------------Saving output to txt file--------##########

np.savetxt(""+str(n)+"Element(Disp).txt", u)
# np.savetxt(""+str(n)+"Element(Stress).txt", S)
