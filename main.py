from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000

# Usuarios registrados previamente: nombre -> (contraseña, mensaje de bienvenida)
USUARIOS = {
    "juan": ("admin", "Bienvenido Administrador juan"),
    "pepe": ("user", "Bienvenido Usuario pepe"),
}


def calcular_descuento(edad, total):
    """Devuelve el monto de descuento según la edad."""
    if edad >= 18 and edad <= 30:
        return total * 0.15
    elif edad > 30:
        return total * 0.25
    return 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        total_sin_descuento = cantidad * PRECIO_TARRO
        descuento = calcular_descuento(edad, total_sin_descuento)
        total_a_pagar = total_sin_descuento - descuento

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "descuento": descuento,
            "total_a_pagar": total_a_pagar,
        }
    return render_template("ejercicio1.html", resultado=resultado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        clave = request.form["clave"]

        if usuario in USUARIOS and USUARIOS[usuario][0] == clave:
            mensaje = USUARIOS[usuario][1]
        else:
            mensaje = "Usuario o contraseña incorrectos"
    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
