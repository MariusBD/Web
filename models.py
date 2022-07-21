from sqlalchemy import Column, Integer, String, Boolean
import db
class Tarea(db.Base): #creacion tabla tarea
    __tablename__="tarea"
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    categoria = Column(String(200),nullable=False)
    fecha = Column(String(50),nullable=False)

    def __init__(self, contenido, hecha, categoria, fecha):
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria
        self.fecha = fecha

    def __str__(self): #visualizacion
        return "Persona({}:{},{})".format(self.id, self.contenido, self.hecha, self.categoria, self.fecha)