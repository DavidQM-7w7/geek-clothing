from flask import Blueprint, jsonify, request
from app.models.prenda import PrendaModel
from app.auth import token_required

prendas_bp = Blueprint("prendas", __name__)


@prendas_bp.route("/prendas", methods=["GET"])
@token_required
def obtener_prendas():
    return jsonify(PrendaModel.obtener_todas())


@prendas_bp.route("/prendas/<int:id>", methods=["GET"])
@token_required
def obtener_prenda(id):

    prenda = PrendaModel.obtener_por_id(id)

    if prenda:
        return jsonify(prenda), 200

    return jsonify({"mensaje": "Prenda no encontrada"}), 404


@prendas_bp.route("/prendas", methods=["POST"])
@token_required
def insertar_prenda():

    datos = request.get_json()

    PrendaModel.insertar(datos)

    return jsonify({
        "mensaje": "Prenda agregada correctamente"
    }), 201


@prendas_bp.route("/prendas/<int:id>", methods=["PUT"])
@token_required
def actualizar_prenda(id):

    datos = request.get_json()

    actualizado = PrendaModel.actualizar(id, datos)

    if actualizado:
        return jsonify({
            "mensaje": "Prenda actualizada correctamente"
        }), 200

    return jsonify({
        "mensaje": "Prenda no encontrada o sin cambios"
    }), 404


@prendas_bp.route("/prendas/<int:id>", methods=["DELETE"])
@token_required
def eliminar_prenda(id):

    eliminado = PrendaModel.eliminar(id)

    if eliminado:
        return jsonify({
            "mensaje": "Prenda eliminada correctamente"
        }), 200

    return jsonify({
        "mensaje": "Prenda no encontrada"
    }), 404