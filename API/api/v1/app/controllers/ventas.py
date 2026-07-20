from flask import Blueprint, jsonify, request
from app.models.venta import VentaModel
from app.auth import token_required

ventas_bp = Blueprint("ventas", __name__)


@ventas_bp.route("/ventas", methods=["GET"])
@token_required
def obtener_ventas():
    return jsonify(VentaModel.obtener_todas())


@ventas_bp.route("/ventas/<int:id>", methods=["GET"])
@token_required
def obtener_venta(id):

    venta = VentaModel.obtener_por_id(id)

    if venta:
        return jsonify(venta), 200

    return jsonify({"mensaje": "Venta no encontrada"}), 404


@ventas_bp.route("/ventas", methods=["POST"])
@token_required
def insertar_venta():

    datos = request.get_json()

    VentaModel.insertar(datos)

    return jsonify({
        "mensaje": "Venta agregada correctamente"
    }), 201


@ventas_bp.route("/ventas/<int:id>", methods=["PUT"])
@token_required
def actualizar_venta(id):

    datos = request.get_json()

    actualizado = VentaModel.actualizar(id, datos)

    if actualizado:
        return jsonify({
            "mensaje": "Venta actualizada correctamente"
        }), 200

    return jsonify({
        "mensaje": "Venta no encontrada o sin cambios"
    }), 404


@ventas_bp.route("/ventas/<int:id>", methods=["DELETE"])
@token_required
def eliminar_venta(id):

    eliminado = VentaModel.eliminar(id)

    if eliminado:
        return jsonify({
            "mensaje": "Venta eliminada correctamente"
        }), 200

    return jsonify({
        "mensaje": "Venta no encontrada"
    }), 404