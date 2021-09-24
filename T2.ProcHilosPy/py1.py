# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:32:26 2021

@author: Pabul
"""

import multiprocessing as mp


def tarea(cadena):
  print('Hola ',cadena)

if __name__=="__main__": #Define si lo estabas viendo como programa principal o de otra manera
  p=mp.Process(target=tarea,args=('Neo'))
  p.start()