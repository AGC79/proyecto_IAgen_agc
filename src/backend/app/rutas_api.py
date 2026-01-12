from flask import Blueprint, request, jsonify
from llm import get_answer
from db import SesionLocal, Interaccion
from datetime import datetime

# Organización de las rutas con blueprint
api = Blueprint("api", __name__)

# Ruta inicial
@api.route("/raiz_api", methods=["GET"])
def health():
    return "Agente LLM de Ciberseguridad"

# Ruta del chatbot
@api.route("/chat", methods=["POST"])

def chat():
    """
    {
    "pregunta": "¿Qué es un firewall?"
    }
    """
    data = request.get_json()
    pregunta = data.get("pregunta")

    if not pregunta:
        return jsonify({"error": "Es necesario introducir una pregunta"}), 400

    respuesta = get_answer(pregunta)

    sesion = SesionLocal()
    interaction = Interaccion(pregunta=pregunta, respuesta=respuesta)
    sesion.add(interaction)
    sesion.commit()
    sesion.close()

    return jsonify({"respuesta": respuesta})

    
