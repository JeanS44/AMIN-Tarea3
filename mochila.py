# -*- coding: UTF-8 -*-
import sys
import time
import numpy as np
import pandas as pd
""" import igraph as ig """
import math

def definirVectorProbabilidades(rand_solution, tau):
    vector_probabilidades = np.array([], dtype=np.double)
    for i in range(1, len(rand_solution)+1):
        vector_probabilidades = np.append(vector_probabilidades, np.divide(1, math.pow(i, tau)))
    return vector_probabilidades

def definirVectorProporciones(vector_probabilidad):
    vector_proporciones = np.array([], dtype=np.double)
    for i in range(len(vector_probabilidad)):
        vector_proporciones = np.append(vector_proporciones, vector_probabilidad[i]/np.sum(vector_probabilidad))
    return vector_proporciones

def definirVectorRuleta(vector_proporcion):
    vector_ruleta = np.array([], dtype=np.double)
    vector_ruleta = np.append(vector_ruleta, vector_proporcion[0])
    for i in range(1, len(vector_proporcion)):
        vector_ruleta = np.append(vector_ruleta, vector_proporcion[i]+vector_ruleta[i-1])
    return vector_ruleta

if len(sys.argv) == 3:
    # Asignación de parámetros.
    np.set_printoptions(threshold=sys.maxsize)
    np.set_printoptions(suppress=True)
    seed = int(sys.argv[1])
    tau = float(sys.argv[2])
    print("Nombre del archivo: ", sys.argv[0], " Seed:", seed, " Tau:", tau)
    # Término de asignación de parámetros.
    random_solution = np.array([94,506,416,992,649,237,457,815,446,422,791,359,667,598,7,544,334,766,994,893,633,131,428,700,617,874,720,419,794,196,997,116,908,539,707,569,537,931,726,487,772,513,81,943,58,303,764,536,724,789])
    v_probabilidades = definirVectorProbabilidades(random_solution, tau)
    print(v_probabilidades)
    v_proporciones = definirVectorProporciones(v_probabilidades)
    print(v_proporciones)
    v_ruleta = definirVectorRuleta(v_proporciones)
    print(v_ruleta)
else:
    print("Porfavor reingrese los parámetros de manera correcta.")
    print("Parametros a ingresar: 'Nombre del archivo' 'Semilla' 'Tau'")
    # .\mochila.py 1 1.4
    sys.exit(0)
