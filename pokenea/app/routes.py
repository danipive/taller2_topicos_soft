import random
from flask import Blueprint, jsonify, render_template
import socket

bp = Blueprint('main', __name__)

# Datos de los Pokeneas
pokeneas = [
    {"id": 1, "nombre": "Pokenea1", "altura": "1.2m", "habilidad": "Llamarada", "imagen": "https://storage.googleapis.com/bucket-pokeneas/poke1.jpg", "frase_filosofica": "Conócete a ti mismo"},
    {"id": 2, "nombre": "Pokenea2", "altura": "1.5m", "habilidad": "Terremoto", "imagen": "https://storage.googleapis.com/bucket-pokeneas/poke2.png", "frase_filosofica": "La vida sin examen no merece la pena vivirse"},
    {"id": 3, "nombre": "Pokenea3", "altura": "1.8m", "habilidad": "Hipnosis", "imagen": "https://storage.googleapis.com/bucket-pokeneas/poke3.PNG", "frase_filosofica": "La verdadera sabiduría está en reconocer la propia ignorancia"},
    {"id": 4, "nombre": "Pokenea4", "altura": "2m", "habilidad": "Hidrobomba", "imagen": "https://storage.googleapis.com/bucket-pokeneas/poKE4.png", "frase_filosofica": "La felicidad es la realización del ser"},
    {"id": 5, "nombre": "Pokenea5", "altura": "2.5m", "habilidad": "Pararrayos", "imagen": "https://storage.googleapis.com/bucket-pokeneas/Poke5.jpeg", "frase_filosofica": "El hombre es libre en el momento en que desea serlo"},
    {"id": 6, "nombre": "Pokenea6", "altura": "1m", "habilidad": "Migraña", "imagen": "https://storage.googleapis.com/bucket-pokeneas/poke6.jpg", "frase_filosofica": "La verdadera sabiduría está en saber que no se sabe nada"},
    {"id": 7, "nombre": "Pokenea7", "altura": "1.7m", "habilidad": "Tumba rocas", "imagen": "https://storage.googleapis.com/bucket-pokeneas/poke7.jpeg", "frase_filosofica": "Frase1"},

    # Añade más Pokeneas según sea necesario
]

@bp.route('/api/pokenea', methods=['GET'])
def get_pokenea():
    pokenea = random.choice(pokeneas)
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": socket.gethostname()
    })

@bp.route('/pokenea', methods=['GET'])
def show_pokenea():
    pokenea = random.choice(pokeneas)
    try:
        return render_template('index.html', pokenea=pokenea, contenedor_id=socket.gethostname())
    except Exception as e:
        return str(e)
