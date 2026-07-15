from app.database import db


class MarcaModel:

    @staticmethod
    def obtener_todas():
        return list(db.marcas.find({}, {"_id": 0}))

    @staticmethod
    def obtener_por_id(id):
        return db.marcas.find_one({"_id": id}, {"_id": 0})

    @staticmethod
    def insertar(datos):
        db.marcas.insert_one(datos)
        return datos

    @staticmethod
    def actualizar(id, datos):
        resultado = db.marcas.update_one(
            {"_id": id},
            {"$set": datos}
        )
        return resultado.modified_count

    @staticmethod
    def eliminar(id):
        resultado = db.marcas.delete_one({"_id": id})
        return resultado.deleted_count