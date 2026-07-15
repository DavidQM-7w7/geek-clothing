from app.database import db


class VentaModel:

    @staticmethod
    def obtener_todas():
        return list(db.ventas.find({}, {"_id": 0}))

    @staticmethod
    def obtener_por_id(id):
        return db.ventas.find_one({"_id": id}, {"_id": 0})

    @staticmethod
    def insertar(datos):
        db.ventas.insert_one(datos)
        return datos

    @staticmethod
    def actualizar(id, datos):
        resultado = db.ventas.update_one(
            {"_id": id},
            {"$set": datos}
        )
        return resultado.modified_count

    @staticmethod
    def eliminar(id):
        resultado = db.ventas.delete_one({"_id": id})
        return resultado.deleted_count