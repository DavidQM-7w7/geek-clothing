from flask import Blueprint, jsonify, request
from app.models.usuario import UsuarioModel
from app.auth import token_required

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/usuarios", methods=["GET"])
@token_required
def obtener_usuarios():
    usuarios = UsuarioModel.obtener_todos()
    return jsonify(usuarios)

@usuarios_bp.route("usuarios/<int:id>", methods=["GET"])
def obtener_usuario(id):
    usuario = UsuarioModel.obtener_por_id(id)

    if usuario:
        return jsonify(usuario), 200

    return jsonify({"mensaje": "Usuario no encontrado"}), 404

@usuarios_bp.route("/usuarios", methods=["POST"])
def insertar_usuario():
    datos = request.get_json()

    UsuarioModel.insertar(datos)

    return jsonify({
        "mensaje": "Usuario agregado correctamente"
    }), 201

@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def actualizar_usuario(id):

    datos = request.get_json()

    actualizado = UsuarioModel.actualizar(id, datos)

    if actualizado:
        return jsonify({
            "mensaje": "Usuario actualizado correctamente"
        }), 200

    return jsonify({
        "mensaje": "Usuario no encontrado o sin cambios"
    }), 404

@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):

    eliminado = UsuarioModel.eliminar(id)

    if eliminado:
        return jsonify({
            "mensaje": "Usuario eliminado correctamente"
        }), 200

    return jsonify({
        "mensaje": "Usuario no encontrado"
    }), 404