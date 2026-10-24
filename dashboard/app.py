from flask import Flask, render_template, jsonify
import socket
import platform
import psutil

app = Flask(__name__)

@app.route("/")
def home():

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return render_template(
        "index.html",
        hostname=hostname,
        ip=ip,
        sistema=platform.system(),
        versao=platform.release()
    )

@app.route("/dados")
def dados():

    rede = psutil.net_io_counters()

    return jsonify({
        "enviados": round(rede.bytes_sent / 1024 / 1024, 2),
        "recebidos": round(rede.bytes_recv / 1024 / 1024, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)