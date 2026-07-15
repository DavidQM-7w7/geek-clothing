from app.database import db


class PrendaModel:

    @staticmethod
    def obtener_todas():
        return list(db.prendas.find({}, {"_id": 0}))

    @staticmethod
    def obtener_por_id(id):
        return db.prendas.find_one({"_id": id}, {"_id": 0})

    @staticmethod
    def insertar(datos):
        db.prendas.insert_one(datos)
        return datos

    @staticmethod
    def actualizar(id, datos):
        resultado = db.prendas.update_one(
            {"_id": id},
            {"$set": datos}
        )
        return resultado.modified_count

    @staticmethod
    def eliminar(id):
        resultado = db.prendas.delete_one({"_id": id})
        return resultado.deleted_count