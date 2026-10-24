import socket


class PortScanner:
    def scan(self, target, start_port, end_port):
        open_ports = []

        print(f"Escaneando {target}...")

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Porta aberta: {port}")
                open_ports.append(port)

            sock.close()

        return open_ports


if __name__ == "__main__":
    scanner = PortScanner()
    scanner.scan("127.0.0.1", 1, 100)python src\scanner.py