import math
import random
import statistics
import matplotlib.pyplot as plt
from scipy.stats import expon,uniform,triang
from numpy import random
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


def simulate_triangular(ps,ml,op):
    # TP1 TODO: Completar codigo
    # Esta funcion toma los 3 parametros de la distribucion triangular
    # y devuelve un numero psuedo-aleaotrio con esta distribucion.
    if op == ps:
        return ml
    else:
        triangular = random.triangular(ps, ml, op)
        return triangular
    #VER SI FUNCIONA
    #scipy.stats.triang o numpy.random.triangular
    # Tenemos que adaptar estos parametros a lo que recibe la funcion
    # triang.ppf para aplicar el metodo de la transformada inversa. .

    # Primero un chequeo: si op == ps, entonces no hay mucho para simular.
    # Por que?
    #tarea 4


    # Esta es la traduccion de parametros a realizar scipy.stats. Revisar la documentaicon
    # y entender como se representa la distribucion.
    #loc = op
    #scale = (ps - op)
    #c = (ml - loc)/scale

    # Si usan numpy.random, no son necesarias traducciones.


def simulate_tasks_duration(project_graph):
    tasks_times = []
    times = project_graph.get_tasks_dist_params()
    for i in range(len(times)):
        task_times.append(simulate_triangular(times[i])
    return tasks_times

    # TP1 TODO: Completar codigo
    # Esta funcion el grafo con n tareas, cada cual con sus parametros de la
    # correspondiente distribucion triangular, y devuelve una lista de
    # n elementos, donde la posicion i corresponde a la duracion de la i-esima
    # tarea.
    # Sugerencia: recordar que la distribucion de la tarea i se encuentra en el
    # diccionario project_graph.d[i]

    # Sacar el pass y reemplzar por el codigo
    #pass
    #VER SI USAMOS MÉTODO O DICCIONARIO DIRECTAMENTE

def get_path_duration(path, tasks_times):
    pathduration = 0
    for task in path:
        pathduration += tasks_times[task]


    # TODO TP1: Completar codigo
    # Dado un camino, representado por path y la secuencia de tareas, y la
    # duracion de cada tarea (donde tasks_times[i] es la duracion de la i-esima
    # tarea, la funcion devuelve la duracion del camino dados esos tiempos.

    # Sacar el pass y reemplzar por el codigo
    pass

def get_project_duration(project_graph, tasks_times):
    projectduration = 0
    project = project_graph.get_paths()
    for path in project:
        path_duration = get_path_duration(path, tasks_times)
        if path_duration > projectduration:
            projectduration = path_duration
    return projectduration


#ALTERNATIVA
# paths = graph.get_paths()
# max_duration = 0
# for path in paths:
#     new_duration = get_path_duration(path, tasks_times)
#     max_duration = max(max_duration, new_duration)

#Ahi max_duration tiene la duracion del camino mas largo


    # TODO TP1: Completar codigo
    # La duracion del proyecto corresponde al maximo de las duraciones de los caminos.
    # Recordatorio: los caminos se encuentran en project_graph.paths, y se pueden
    # obtener con el proyecto get_paths()

    # La funcion debe computar la duracion de cada uno de los caminos y retornar el maximo.


    # Sacar el pass y reemplzar por el codigo
    pass

def simulate(n_sim, project_graph):
    simulations = []

    simulations.append(get_project_duration(X))
    # TODO TP1: Completar codigo
    # Esta funcion realiza n_sim simulaciones y analiza los resultados necesarios para el
    # arbol de decision.
    # Idealmente, puede devolver una lista con la duracion para cada una de las
    # simulaciones para su posterior analisis.

    # Sacar el pass y reemplzar por el codigo
    pass

def get_prob_in_range(vals, a, b):
    # TODO TP1: Completar codigo
    # Funcion auxiliar para analisis de resultados y calculo de probabilidades.
    # Dada una muestra de valores vals, calcula la proporcion de x in vals tales que
    # a < x <= b.

    # Sacar el pass y reemplzar por el codigo
    pass

def main():
    # TODO TP1: Completar codigo

    # Fijamos la semilla, por reproducibilidad.
    random.seed(0)

    # 300k por perder el deadline. Por ahora, 47.0
    # 150k por terminar en 40 o menos. Por ahora, mantenemos 40.0
    # Estos son los limites que nos importan.
    deadline = 47.0
    incentive = 40.0

    # Primer paso: consideramos el escenario sin contrataciones extra.
    graph_no_hire = ProjectGraph()

    print(graph_no_hire.dist_params[2])

    # TODO: simular en este contexto!


    # TODO: Analizar los resultados.

    # Segundo paso: analizar en el contexto que se hace la contratacion.
    # Esto lo representamos modifiando la duracion de las tarea 2.
    graph_hire = graph_no_hire

    graph_hire.dist_params[2] = (6.0, 9.0, 13.0)
    print(graph_hire.dist_params[2])
    print(graph_hire.dist_params[2][0], graph_hire.dist_params[2][1], graph_hire.dist_params[2][2])

    # TODO: simular en este contexto!


    # TODO: Analizar los resultados.


if __name__ == "__main__":
    main()
