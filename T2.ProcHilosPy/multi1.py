# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:33:16 2021

@author: Pablo
"""
import multiprocessing as mp

def tarea(cadena):
    print("Hola ", cadena)

if __name__=='__main__':
  p=mp.Process(target=tarea, args=('Lucas C. ',))
  p.start()
  p.join()
  
def calc_cuad(numeros):
    print('calcula el cuadrado de los numeros')
    for n in numeros:
        print('cuadrado:', n*n)

nums=range(10)
p1=mp.Process(target=calc_cuad, args=(nums,))
p1.start()
p1.join()

print('termmina la ejecucion numerica')
import time

def calc_cub(numeros):
    print('calcula el cubo de los numeros')
    for n in numeros:
        time.sleep(0.5)
        print('cubo:', n*n*n)

def calc_cuad(numeros):
    print('calcula el cuadrado de los numeros')
    for n in numeros:
        time.sleep(0.5)
        print('cuadrado:', n*n)

nums=range(10)

p1=mp.Process(target=calc_cuad, args=(nums,))
t=time.time()
p2=mp.Process(target=calc_cub, args=(nums,))

p1.start()
p2.start()

p1.join()
p2.join()

print('Tiempo de ejecución: ', time.time()-t)
print('termmina la ejecucion numerica')