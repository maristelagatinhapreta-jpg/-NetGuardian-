from flask import Flask, jsonify, render_template
import socket
import platform
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dados")
def dados():
    net = psutil.net_io_counters()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    sistema = platform.system()
    versao = platform.release()

    return jsonify({
        "hostname": hostname,
        "ip": ip,
        "sistema_operacional": sistema,
        "versao": versao,
        "enviados": round(net.bytes_sent / (1024 * 1024), 2),
        "recebidos": round(net.bytes_recv / (1024 * 1024), 2),
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
