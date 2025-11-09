from flask import Flask, render_template, g, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"   # Asegurate que este archivo exista en la carpeta del proyecto

def get_db():
    db = getattr(g, "_db", None)
    if db is None:
        db = g._db = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.route("/")
def index():
    db = get_db()
    query = '''
        SELECT vehiculos.patente,
               vehiculos.marca,
               vehiculos.modelo,
               vehiculos.anio,
               vehiculos.imagen,
               servicios.servicio,
               servicios.costo
        FROM vehiculos
        INNER JOIN servicios
            ON vehiculos.id = servicios.id_vehiculo
    '''
    datos = db.execute(query).fetchall()
    return render_template("index.html", datos=datos)

@app.teardown_appcontext
def close(err):
    db = getattr(g, "_db", None)
    if db:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)


