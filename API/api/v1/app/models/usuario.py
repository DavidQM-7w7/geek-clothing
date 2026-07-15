from app.database import db


class UsuarioModel:

    @staticmethod
    def obtener_todos():
        usuarios = list(db.usuarios.find({}, {"_id": 0}))
        return usuarios
    
    @staticmethod
    def obtener_por_id(id):
        usuario = db.usuarios.find_one({"_id": id}, {"_id": 0})
        return usuario
    
    @staticmethod
    def insertar(datos):
        db.usuarios.insert_one(datos)
        return datos
    
    @staticmethod
    def actualizar(id, datos):
        resultado = db.usuarios.update_one(
        {"_id": id},
        {"$set": datos}
        )
        return resultado.modified_count
    
    @staticmethod
    def eliminar(id):
        resultado = db.usuarios.delete_one({"_id": id})
        return resultado.deleted_count