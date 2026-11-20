
from flask import Flask, render_template, request
import os

app = Flask(__name__)

PRODUCTOS = {
    "cafe": {"nombre": "Café", "precio": 5.00},
    "sandwich": {"nombre": "Sándwich", "precio": 8.00},
    "jugo": {"nombre": "Jugo", "precio": 6.00}
}

@app.route("/", methods=["GET", "POST"])
def inicio():
    mensaje = None
    total = None
    detalle = []

    if request.method == "POST":
        producto = request.form.get("producto", "")
        cantidad_texto = request.form.get("cantidad", "1")

        try:
            cantidad = int(cantidad_texto)
        except ValueError:
            cantidad = 0

        # Defectos intencionales para las pruebas
        if producto not in PRODUCTOS:
            mensaje = "Pedido registrado."
            total = 0
        elif cantidad_texto == "":
            mensaje = "Pedido registrado."
            total = 0
        else:
            precio = PRODUCTOS[producto]["precio"]
            total = precio * cantidad

            detalle.append({
                "nombre": PRODUCTOS[producto]["nombre"],
                "cantidad": cantidad,
                "subtotal": total
            })

            mensaje = "Pedido registrado correctamente."

    return render_template(
        "index.html",
        productos=PRODUCTOS,
        mensaje=mensaje,
        total=total,
        detalle=detalle
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
