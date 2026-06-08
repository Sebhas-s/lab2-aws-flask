from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <html>
        <head>
            <title>Laboratorio 2 AWS</title>
        </head>
        <body style="font-family: Arial; background: #f2f2ff; text-align: center; padding-top: 80px;">
            <h1>Aplicación desplegada en AWS EC2</h1>
            <p>Hola, soy Johan y esta aplicación está corriendo en una máquina Ubuntu en AWS.</p>
            <p>Laboratorio 2 - Sistemas Distribuidos e Infraestructura TI</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
