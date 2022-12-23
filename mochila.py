# -*- coding: UTF-8 -*-
import sys
import time
import numpy as np
import pandas as pd
""" import igraph as ig """
import math
import random

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

def determinarFitness(vector_beneficio, vector_peso, vector_solucion):
    fitness = np.array([])
    pi = np.array([])
    max_pi = np.max(vector_beneficio)
    for i in range(len(vector_beneficio)):
        pi = np.append(pi, vector_beneficio[i]/(max_pi+1))
    for i in range(len(vector_solucion)):
        if vector_solucion[i] == 0:
            fitness = np.append(fitness, vector_peso[i]+pi[i])
        elif vector_solucion[i] == 1:
            fitness = np.append(fitness, vector_beneficio[i]+(1-pi[i]))
    return fitness

def seleccionarComponenteJ(vector_fitness_ordenado, vector_fitness):
    array = np.array([])
    for i in range(len(vector_fitness)):
        for j in range(len(vector_fitness_ordenado)):
            if vector_fitness_ordenado[i] == vector_fitness[j]:
                pos = j
                array = np.append(array, pos)
    return array

def determinarSelección(vector_solucion, vector_ruleta, iteraciones):
    vector_seleccion = np.empty_like(vector_solucion)
    vector_seleccion[:] = vector_solucion
    for i in range(iteraciones):
        for j in range(len(vector_seleccion)):
            azar = random.uniform(0, 1)
            if azar <= vector_ruleta[j]:
                pos = j
                if vector_seleccion[pos] == 1:
                    vector_seleccion[pos] = 0
                elif vector_seleccion[pos] == 0:
                    vector_seleccion[pos] = 1
    return vector_seleccion

def compararPesoYSolucion(sol, peso, cap_max):
    suma = 0
    for i in range(len(sol)):
        if sol[i]==1:
            suma+=peso[i]
    return suma

if len(sys.argv) == 5:
    # Asignación de parámetros.
    np.set_printoptions(threshold=sys.maxsize)
    np.set_printoptions(suppress=True)
    seed = int(sys.argv[1])
    iteraciones = int(sys.argv[2])
    tau = float(sys.argv[3])
    entrada = sys.argv[4]
    print("Nombre del archivo: ", sys.argv[0], " Seed:", seed, " Tau:", tau, " Archivo:", entrada)
    parametros = pd.read_csv(entrada, skiprows=1, delim_whitespace=True, header=None, nrows=3, usecols=[1]).to_numpy()
    """ print(parametros) """
    n = int(parametros[0])     
    c = int(parametros[1])     
    datos = pd.read_csv(entrada, skiprows=5, delimiter=',', header=None, nrows=n, usecols=[1, 2, 3]).transpose().to_numpy()
    """ print(datos) """
    # Término de asignación de parámetros.
    random_solution = np.random.randint(2, size = len(datos[0]))
    print("Solución generada:\n", random_solution)
    v_probabilidades = definirVectorProbabilidades(random_solution, tau)
    """ print("Vector de probabilidades:\n",v_probabilidades) """
    v_proporciones = definirVectorProporciones(v_probabilidades)
    """ print("Vector de proporciones:\n",v_proporciones) """
    v_ruleta = definirVectorRuleta(v_proporciones)
    """ print("Vector de ruleta:\n",v_ruleta) """
    i = 0
    best_sol0 = np.array([])
    s = 0
    while i < iteraciones:
        print("------------------ Iteración", i, "------------------")
        v_fitness = determinarFitness(datos[0], datos[1], random_solution)
        print("Vector de fitness:\n", v_fitness)
        v_fitness_sorted = np.array([], dtype=int)
        v_fitness_sorted = np.sort(v_fitness, kind='mergesort')
        print("Vector de fitness ordenado:\n", v_fitness_sorted)
        componente_j = seleccionarComponenteJ(v_fitness_sorted, v_fitness)
        """ print("Vector de componente J:\n",componente_j) """
        seleccion = determinarSelección(random_solution,v_ruleta, 100)
        print("Solución generada en selección:\n", seleccion)
        ran = compararPesoYSolucion(random_solution, datos[1], c)
        print(ran)
        sele = compararPesoYSolucion(seleccion, datos[1], c)
        print(sele)
        if ran < sele:
            best_sol0 = random_solution
            s = ran
        else:
            best_sol0 = seleccion
            s = sele
        print(best_sol0)
        i += 1
else:
    print("Porfavor reingrese los parámetros de manera correcta.")
    print("Parametros a ingresar: 'Nombre del archivo' 'Semilla' 'Tau' 'Nombre del archivo'")
    # python .\mochila.py 1 50 1.4 knapPI_15_20_1000.csv
    sys.exit(0)