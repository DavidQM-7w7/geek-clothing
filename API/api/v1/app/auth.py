import os

from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("API_TOKEN")


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        auth = request.headers.get("Authorization")

        if auth is None:
            return jsonify({"mensaje": "Token requerido"}), 401

        if not auth.startswith("Bearer "):
            return jsonify({"mensaje": "Formato de token inválido"}), 401

        token = auth.split(" ")[1]

        if token != TOKEN:
            return jsonify({"mensaje": "Token inválido"}), 401

        return f(*args, **kwargs)

    return decorated