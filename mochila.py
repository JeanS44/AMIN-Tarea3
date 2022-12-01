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

def determinarFitness(vector_beneficio):
    sum_v_beneficio = np.sum(vector_beneficio)
    vector_fitness = np.array([])
    for i in range(len(vector_beneficio)):
        vector_fitness = np.append(vector_fitness, np.ceil(np.divide((vector_beneficio[i]*100),sum_v_beneficio)))
    """ return "La suma total fue: ", suma_total, "el fitness es: ", fitness, " y la capacidad máxima de la mochila es: ", maximo_mochila """
    """ return fitness """
    return vector_fitness

def determinarPosArrayOrdenado(vector_fitness, vector_fitness_sorted):
    array = []
    return array

if len(sys.argv) == 3:
    # Asignación de parámetros.
    np.set_printoptions(threshold=sys.maxsize)
    np.set_printoptions(suppress=True)
    seed = int(sys.argv[1])
    tau = float(sys.argv[2])
    print("Nombre del archivo: ", sys.argv[0], " Seed:", seed, " Tau:", tau)
    # Término de asignación de parámetros.
    """ peso = np.array([94,506,416,992,649,237,457,815,446,422,791,359,667,598,7,544,334,766,994,893,633,131,428,700,617,874,720,419,794,196,997,116,908,539,707,569,537,931,726,487,772,513,81,943,58,303,764,536,724,789]) """
    peso = np.array([95, 4 , 60, 32, 23, 72, 80, 62, 65, 46])
    beneficio = np.array([55, 10, 47, 5, 4, 50, 8, 61, 85, 87])
    cap_max = 269
    random_solution = np.random.randint(2, size = len(peso))
    print("Solución generada:\n", random_solution)
    v_probabilidades = definirVectorProbabilidades(random_solution, tau)
    print("Vector de probabilidades:\n",v_probabilidades)
    v_proporciones = definirVectorProporciones(v_probabilidades)
    print("Vector de proporciones:\n",v_proporciones)
    v_ruleta = definirVectorRuleta(v_proporciones)
    print("Vector de ruleta:\n",v_ruleta)
    v_fitness = determinarFitness(beneficio)
    print("Vector de fitness:\n", v_fitness)
    v_fitness_sorted = np.array([], dtype=int)
    v_fitness_sorted = np.sort(v_fitness, kind='mergesort')
    print("Vector de fitness ordenado:\n", v_fitness_sorted)
    pos_arr_ordenado = determinarPosArrayOrdenado(v_fitness, v_fitness_sorted)
    print(pos_arr_ordenado)
else:
    print("Porfavor reingrese los parámetros de manera correcta.")
    print("Parametros a ingresar: 'Nombre del archivo' 'Semilla' 'Tau'")
    # .\mochila.py 1 1.4
    sys.exit(0)