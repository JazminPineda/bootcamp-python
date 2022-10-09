
# Online Python - IDE, Editor, Compiler, Interpreter
# Matriz de 3x3

"""
   0 1 2
0  1 2 3
1  4 5 6
2  7 8 9

"""
matriz = [[1,2,3],[4,5,6],[7,8,9]]


print(matriz[0][0],matriz[1][1],matriz[2][2])
# 6 7 2
print(matriz[1][2], matriz[2][0], matriz[0][1])

matriz_dic = {'0':{'0':1,'1':2 ,'2':3 },'1':{'0':4,'1':5,'2':6},'2':{'0':7,'1':8,'2':9}}

# print de la diagonal
print(matriz_dic['0']['0'], matriz_dic['1']['1'], matriz_dic['2']['2'])
# 5 3 8
print(matriz_dic['1']['1'], matriz_dic['0']['2'], matriz_dic['2']['1'])

print(matriz_dic.keys())
print(matriz_dic['0'].keys())

# 'clave1' 'clave2' 'clave3' 'clave4'