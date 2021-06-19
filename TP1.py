import math
import statistics
import random
import matplotlib.pyplot as plt
from scipy.stats import expon,uniform,triang
import numpy as np
import sys

class ProjectGraph:
    def __init__(self):
        self.n = 14
        self.m = 6
        self.paths = self._load_paths()
        self.dist_params = self._load_tasks_dist_params()

    def get_paths(self):
        return self.paths

    def get_n_tasks(self):
        return self.n

    def get_tasks_dist_params(self):
        return self.dist_params

    def _load_tasks_dist_params(self):
        # Define los parametros de la distribucion triang para cada tarea.
        # Notar que es estatico, pero podria ser dinamico (tomarse de alguna
        # otra fuente). Usa un diccionario.
        d = {}
        d[0] = (1.0, 2.0, 3.0)
        d[1] = (2.0, 3.5, 8.0)
        d[2] = (6.0, 9.0, 18.0)
        d[3] = (4.0, 5.5, 10.0)
        d[4] = (1.0, 4.5, 5.0)
        d[5] = (4.0, 4.0, 10.0)
        d[6] = (5.0, 6.5, 11.0)
        d[7] = (5.0, 8.0, 17.0)
        d[8] = (3.0, 7.5, 9.0)
        d[9] = (3.0, 9.0, 9.0)
        d[10] = (4.0, 4.0, 4.0)
        d[11] = (1.0, 5.5, 7.0)
        d[12] = (1.0, 2.0, 3.0)
        d[13] = (5.0, 5.5, 9.0)
        return d

    def _load_paths(self):
        # Define los caminos.
        # Notar que es estatico. Podria ser conveniente tener otra
        # representacion e, incluso, otra estructura para el grafo general.
        return [[0,1,2,3,6,7,12],[0,1,2,4,7,12],[0,1,2,4,5,9,10,13],[0,1,2,4,5,9,11,13],[0,1,2,8,9,10,13],[0,1,2,8,9,11,13]]


def simulate_triangular(ps, ml, op):
    # TP1 TODO: Completar codigo
    # Esta funcion toma los 3 parametros de la distribucion triangular
    # y devuelve un numero psuedo-aleaotrio con esta distribucion.
    if op == ps:
        return ml
    else:
        triangular = np.random.triangular(ps, ml, op)
        return triangular
    #opcional usar scipy para que se vea método de transformada inversa

def simulate_tasks_duration(project_graph):
    ret = []
    for i in range(project_graph.n):
        ret.append(simulate_triangular(project_graph.get_tasks_dist_params()[i][0], project_graph.get_tasks_dist_params()[i][1], project_graph.get_tasks_dist_params()[i][2]))
    return ret


    # TP1 TODO: Completar codigo
    # Esta funcion el grafo con n tareas, cada cual con sus parametros de la
    # correspondiente distribucion triangular, y devuelve una lista de
    # n elementos, donde la posicion i corresponde a la duracion de la i-esima
    # tarea.
    # Sugerencia: recordar que la distribucion de la tarea i se encuentra en el
    # diccionario project_graph.d[i]


def get_path_duration(path, ret):
    pathduration = 0
    for task in path:
        pathduration += ret[task]
    return pathduration

    # TODO TP1: Completar codigo
    # Dado un camino, representado por path y la secuencia de tareas, y la
    # duracion de cada tarea (donde ret[i] es la duracion de la i-esima
    # tarea, la funcion devuelve la duracion del camino dados esos tiempos.


def get_project_duration(project_graph, ret):
    projectduration = 0
    paths = project_graph.get_paths()
    for i in range(project_graph.m):
        path_duration = get_path_duration(paths[i], ret)
        if path_duration > projectduration:
            projectduration = path_duration
    return projectduration


#ALTERNATIVA
# paths = graph.get_paths()
# max_duration = 0
# for path in paths:
#     new_duration = get_path_duration(path, ret)
#     max_duration = max(max_duration, new_duration)
#Ahi max_duration tiene la duracion del camino mas largo


def simulate(n_sim, project_graph):
    vals = []
    for i in range(n_sim):
        ret = simulate_tasks_duration(project_graph)
        vals.append(get_project_duration(project_graph, ret))
    return vals
    # TODO TP1: Completar codigo
    # Esta funcion realiza n_sim simulaciones y analiza los resultados necesarios para el
    # arbol de decision.
    # Idealmente, puede devolver una lista con la duracion para cada una de las
    # simulaciones para su posterior analisis.



    # TODO TP1: Completar codigo
    # Funcion auxiliar para analisis de resultados y calculo de probabilidades.
    # Dada una muestra de valores vals, calcula la proporcion de x in vals tales que
    # a < x <= b.

    # Sacar el pass y reemplzar por el codigo
def get_prob_in_range(vals, a, b):
    counter = 0
    for time in vals:
        if time > a and time <= b:
            counter += 1
    return str(round((counter / len(vals))*100)) + "%"

#def get_prob_in_range(vals, a, b):
    # TODO TP1: Completar codigo
    # Funcion auxiliar para analisis de resultados y calculo de probabilidades.
    # Dada una muestra de valores vals, calcula la proporcion de x in vals tales que
    # a < x <= b.



def main():
    # Fijamos la semilla, por reproducibilidad.
    np.random.seed(0)
    # 300k por perder el deadline. Por ahora, 47.0
    # 150k por terminar en 40 o menos. Por ahora, mantenemos 40.0
    # Estos son los limites que nos importan.
    deadline = 47.0
    incentive = 40.0

    # Primer paso: consideramos el escenario sin contrataciones extra.
    graph_no_hire = ProjectGraph()
    vals = simulate(1000, graph_no_hire)

    # TODO: Analizar los resultados.

    print("Probabilidades de que el proyecto tarde: \n"+"(Sin contratar mano de obra extra)")
    print("Menos de 40 semanas: " +get_prob_in_range(vals, 0, incentive))
    print("Entre 40 y 47 semanas: " +get_prob_in_range(vals, incentive, deadline))
    print("Más de 47 semanas: " +get_prob_in_range(vals, deadline, 1000))
    # Segundo paso: analizar en el contexto que se hace la contratacion.
    # Esto lo representamos modifiando la duracion de las tarea 2.
    graph_hire = graph_no_hire
    graph_hire.dist_params[2] = (6.0, 9.0, 13.0)

    vals_h = simulate(1000, graph_hire)
    # TODO: simular en este contexto!
    print("Probabilidades de que el proyecto tarde: \n"+"(Contratando mano de obra extra)")
    print("Menos de 40 semanas: " +get_prob_in_range(vals_h, 0, incentive))
    print("Entre 40 y 47 semanas: " +get_prob_in_range(vals_h, incentive, deadline))
    print("Más de 47 semanas: " +get_prob_in_range(vals_h, deadline, 1000))

    # TODO: Analizar los resultados.


if __name__ == "__main__":
    main()
