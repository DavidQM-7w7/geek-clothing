from flask import Blueprint, jsonify, request
from app.models.marca import MarcaModel
from app.auth import token_required

marcas_bp = Blueprint("marcas", __name__)


@marcas_bp.route("/marcas", methods=["GET"])
@token_required
def obtener_marcas():
    return jsonify(MarcaModel.obtener_todas())


@marcas_bp.route("/marcas/<int:id>", methods=["GET"])
@token_required
def obtener_marca(id):

    marca = MarcaModel.obtener_por_id(id)

    if marca:
        return jsonify(marca), 200

    return jsonify({"mensaje": "Marca no encontrada"}), 404


@marcas_bp.route("/marcas", methods=["POST"])
@token_required
def insertar_marca():

    datos = request.get_json()

    MarcaModel.insertar(datos)

    return jsonify({
        "mensaje": "Marca agregada correctamente"
    }), 201


@marcas_bp.route("/marcas/<int:id>", methods=["PUT"])
@token_required
def actualizar_marca(id):

    datos = request.get_json()

    actualizado = MarcaModel.actualizar(id, datos)

    if actualizado:
        return jsonify({
            "mensaje": "Marca actualizada correctamente"
        }), 200

    return jsonify({
        "mensaje": "Marca no encontrada o sin cambios"
    }), 404


@marcas_bp.route("/marcas/<int:id>", methods=["DELETE"])
@token_required
def eliminar_marca(id):

    eliminado = MarcaModel.eliminar(id)

    if eliminado:
        return jsonify({
            "mensaje": "Marca eliminada correctamente"
        }), 200

    return jsonify({
        "mensaje": "Marca no encontrada"
    }), 404