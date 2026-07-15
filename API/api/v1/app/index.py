from flask import Flask
from app.controllers.usuarios import usuarios_bp
from app.controllers.marcas import marcas_bp
from app.controllers.prendas import prendas_bp
from app.controllers.ventas import ventas_bp
from app.controllers.reportes import reportes_bp

app = Flask(__name__)

app.register_blueprint(usuarios_bp, url_prefix="/api/v1")
app.register_blueprint(marcas_bp, url_prefix="/api/v1")
app.register_blueprint(prendas_bp, url_prefix="/api/v1")
app.register_blueprint(ventas_bp, url_prefix="/api/v1")
app.register_blueprint(reportes_bp, url_prefix="/api/v1")