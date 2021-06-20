#Importamos las librerías que utilizaremos para el código
import random
import numpy as np
import sys
#Importamos la clase ProjectGraph desde el archivo en donde está
from Class_ProjectGraph import ProjectGraph

def simulate_triangular(ps, ml, op):
    # Si el escenario pesimista es igual al optimista, esta función devuelve
    # la duración del escenario más probable.
    # Si ello no es así, esta funcion toma los 3 parámetros de la distribución
    # triangular y devuelve un numero psuedo-aleaotrio con esta distribución.
    if ps == op:
        return ml
    else:
        triangular = np.random.triangular(ps, ml, op)
        return triangular

def simulate_tasks_duration(project_graph):
    # Esta funcion toma un objeto de la clase ProjectGraph con n tareas,
    # cada cual con sus parámetros de la correspondiente distribución
    # triangular y devuelve una lista de n elementos, donde la posicion i
    # corresponde a la duracion de la i-ésima tarea.
    ret = []
    for i in range(project_graph.n):
        ret.append(simulate_triangular \
        (project_graph.get_tasks_dist_params()[i][0], \
        project_graph.get_tasks_dist_params()[i][1], \
        project_graph.get_tasks_dist_params()[i][2]))
    return ret

def get_path_duration(path, ret):
    # Dado un camino, representado por path y una lista que contiene las
    # duraciones de las tareas (donde ret[i] es la duracion de la i-esima
    # tarea), la funcion devuelve la duracion total del camino.
    pathduration = 0
    for task in path:
        pathduration += ret[task]
    return pathduration

def get_project_duration(project_graph, ret):
    # Esta función toma un objeto de la clase ProjectGraph con m caminos
    # y devuelve el máximo de las duraciones de los m caminos del proyecto.
    projectduration = 0
    paths = project_graph.get_paths()
    for i in range(project_graph.m):
        path_duration = get_path_duration(paths[i], ret)
        if path_duration > projectduration:
            projectduration = path_duration
    return projectduration

def simulate(n_sim, project_graph):
    # Esta funcion realiza n_sim simulaciones y devuelve una lista con n_sim
    # duraciones de proyectos simuladaspara su posterior análisis.
    vals = []
    for i in range(n_sim):
        ret = simulate_tasks_duration(project_graph)
        vals.append(get_project_duration(project_graph, ret))
    return vals

def get_prob_in_range(vals, a, b):
    # Esta función calcula la proporción de tiempos simulados de duración del
    # proyecto que se encuentran dentro de a < x <= b.
    # Así, podremos analizar la probabilidad de obtener un incentivo o
    # sufrir una penalización en su ejecución.
    counter = 0
    for time in vals:
        if time > a and time <= b:
            counter += 1
    return str(round(((counter / len(vals))*100), 1)) + "%"



def main():
    # Fijamos la semilla para poder reproducir los resultados obtenidos.
    np.random.seed(0)

    # Fijamos los parámetros temporales que determinarán si obtenemos un
    # incentivo o una penalización en el pago del proyecto.
    deadline = 47.0 #Pendalización por tardar más de 47 semanas.
    incentive = 40.0 #Incentivo por tardar menos de 40 semanas.

    # Primer paso: consideramos el escenario sin contrataciones extra.
    # Creamos un objeto de la clase ProjectGraph que representa el grafo
    # sin contratar mano de obra extra.
    graph_no_hire = ProjectGraph()

    # Obtenemos una lista con n_sim duraciones de proyectos simuladas.
    vals = simulate(1000, graph_no_hire)

    # Obtenemos las probabilidades de obtener el incentivo o sufrir la
    # penalización de acuerdo con la duración del proyecto.
    print("Probabilidades de que el proyecto tarde: \n"+"(Sin contratar mano de obra extra)")
    print("Menos de 40 semanas: " +get_prob_in_range(vals, 0, incentive))
    print("Entre 40 y 47 semanas: " +get_prob_in_range(vals, incentive, deadline))
    print("Más de 47 semanas: " +get_prob_in_range(vals, deadline, 1000))

    # Segundo paso: analizar en el contexto en donde se hace la contratacion.
    # Para ellos, creamos un objeto idéntico al creado en el escenario anterior
    # y modificamos el parámetro que contiene la duración de la tarea 2.
    graph_hire = ProjectGraph()
    graph_hire.dist_params[2] = (6.0, 9.0, 13.0)

    # Obtenemos una lista con n_sim duraciones de proyectos simuladas en el
    # nuevo escenario.
    vals_h = simulate(1000, graph_hire)

    # Obtenemos las probabilidades de obtener el incentivo o sufrir la
    # penalización de acuerdo con la duración del proyecto.
    print("Probabilidades de que el proyecto tarde: \n"+"(Contratando mano de obra extra)")
    print("Menos de 40 semanas: " +get_prob_in_range(vals_h, 0, incentive))
    print("Entre 40 y 47 semanas: " +get_prob_in_range(vals_h, incentive, deadline))
    print("Más de 47 semanas: " +get_prob_in_range(vals_h, deadline, 1000))

if __name__ == "__main__":
    main()
