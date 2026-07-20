from flask import Blueprint, jsonify
from app.database import db
from app.auth import token_required

reportes_bp = Blueprint("reportes", __name__)

#Marcas que tienen al menos una venta
@reportes_bp.route("/reportes/marcas-con-ventas", methods=["GET"])
@token_required
def marcas_con_ventas():

    resultado = list(db.ventas.aggregate([

        {
            "$unwind": "$detalle"
        },

        {
            "$lookup": {
                "from": "prendas",
                "localField": "detalle.prendaId",
                "foreignField": "_id",
                "as": "prenda"
            }
        },

        {
            "$unwind": "$prenda"
        },

        {
            "$lookup": {
                "from": "marcas",
                "localField": "prenda.marcaId",
                "foreignField": "_id",
                "as": "marca"
            }
        },

        {
            "$unwind": "$marca"
        },

        {
            "$group": {
                "_id": "$marca._id",
                "nombre": {
                    "$first": "$marca.nombre"
                }
            }
        },

        {
            "$project": {
                "_id": 0,
                "marcaId": "$_id",
                "nombre": 1
            }
        }

    ]))

    return jsonify(resultado)

#Prendas vendidas y stock restante
@reportes_bp.route("/reportes/prendas-stock", methods=["GET"])
@token_required
def prendas_stock():

    resultado = list(db.ventas.aggregate([

        {
            "$unwind": "$detalle"
        },

        {
            "$lookup": {
                "from": "prendas",
                "localField": "detalle.prendaId",
                "foreignField": "_id",
                "as": "prenda"
            }
        },

        {
            "$unwind": "$prenda"
        },

        {
            "$project": {
                "_id": 0,
                "prenda": "$prenda.nombre",
                "cantidadVendida": "$detalle.cantidad",
                "stockRestante": "$prenda.stock"
            }
        }

    ]))

    return jsonify(resultado)

#Top 5 marcas más vendidas
@reportes_bp.route("/reportes/top5-marcas", methods=["GET"])
@token_required
def top5_marcas():

    resultado = list(db.ventas.aggregate([

        {
            "$unwind": "$detalle"
        },

        {
            "$lookup": {
                "from": "prendas",
                "localField": "detalle.prendaId",
                "foreignField": "_id",
                "as": "prenda"
            }
        },

        {
            "$unwind": "$prenda"
        },

        {
            "$group": {
                "_id": "$prenda.marcaId",
                "ventas": {
                    "$sum": "$detalle.cantidad"
                }
            }
        },

        {
            "$lookup": {
                "from": "marcas",
                "localField": "_id",
                "foreignField": "_id",
                "as": "marca"
            }
        },

        {
            "$unwind": "$marca"
        },

        {
            "$project": {
                "_id": 0,
                "marca": "$marca.nombre",
                "ventas": 1
            }
        },

        {
            "$sort": {
                "ventas": -1
            }
        },

        {
            "$limit": 5
        }

    ]))

    return jsonify(resultado)