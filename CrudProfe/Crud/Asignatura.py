class Asignatura:
    def __init__(self, id, titulo, numHoras, idProfesor):
        self.id = id
        self.titulo = titulo
        self.numHoras = numHoras
        self.idProfesor = idProfesor

    def __str__(self):
        return (f"ID: {self.id}, "f"Título: {self.titulo}, "f"Número de Horas: {self.numHoras}, "f"ID del Profesor: {self.idProfesor}")