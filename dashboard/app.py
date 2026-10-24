from flask import Flask
import socket
import platform

app = Flask(__name__)


@app.route("/")
def home():

    hostname = socket.gethostname()

    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Não encontrado"

    sistema = platform.system()
    versao = platform.release()

    return f"""
    <html>
    <head>
        <title>NetGuardian</title>

        <style>

            body {{
                background-color: #0f172a;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 80px;
            }}

            .card {{
                background-color: #1e293b;
                width: 600px;
                margin: auto;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
            }}

            h1 {{
                color: #38bdf8;
            }}

            hr {{
                border: 1px solid #475569;
            }}

        </style>

    </head>

    <body>

        <div class="card">

            <h1>🛡️ NetGuardian</h1>

            <h2>Sistema de Monitoramento de Rede</h2>

            <p>Status: Online ✅</p>

            <hr>

            <p><b>Computador:</b> {hostname}</p>

            <p><b>IP:</b> {ip}</p>

            <p><b>Sistema:</b> {sistema}</p>

            <p><b>Versão:</b> {versao}</p>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)