class Profesor:
    def __init__(self, id, nombre, apellidos, telefono, direccion, cc):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion
        self.cc = cc


    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre} {self.apellidos} | "f"Teléfono: {self.telefono} | Dirección: {self.direccion} | "f"CC: {self.cc}")