#Definimos el constructor de la clase ProjectGraph
class ProjectGraph:
    def __init__(self):
        self.n = 14 #Número de tareas
        self.m = 6 #Número de caminos
        self.paths = self._load_paths()
        self.dist_params = self._load_tasks_dist_params()

    #Definimos los métodos para acceder a los parámetros de la clase
    def get_paths(self):
        return self.paths

    def get_n_tasks(self):
        return self.n

    def get_tasks_dist_params(self):
        return self.dist_params

    #Definimos los métodos para cargar los parámetros de la clase
    def _load_tasks_dist_params(self):
        # Define los parametros de la distribucion triangular para cada tarea.
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
        # Define los caminos que se deben realizarse dentro del proyecto.
        return [[0,1,2,3,6,7,12],[0,1,2,4,7,12],[0,1,2,4,5,9,10,13], \
        [0,1,2,4,5,9,11,13],[0,1,2,8,9,10,13],[0,1,2,8,9,11,13]]
