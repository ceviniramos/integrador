from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def obtener_datos():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
 
    cursor.execute("""
        SELECT vehiculos.patente,
               vehiculos.marca,
               vehiculos.modelo,
               vehiculos.anio,
               servicios.descripcion,
               servicios.fecha,
               servicios.costo,
               servicios.imagen
        FROM vehiculos
        INNER JOIN servicios
        ON vehiculos.id = servicios.id_vehiculo
    """)
    datos = cursor.fetchall()
    conn.close()
    return datos

@app.route("/")
def index():
    datos = obtener_datos()
    return render_template("index.html", datos=datos)

if __name__ == "__main__":
    app.run(debug=True)
