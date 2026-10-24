import psutil


stats = psutil.net_io_counters()

print("\n=== NETGUARDIAN ===\n")

print(f"Bytes enviados  : {stats.bytes_sent}")
print(f"Bytes recebidos : {stats.bytes_recv}")

print("\nMonitor concluído.")