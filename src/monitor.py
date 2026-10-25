import psutil


def get_network_stats():
    stats = psutil.net_io_counters()
    return {
        "bytes_sent": stats.bytes_sent,
        "bytes_recv": stats.bytes_recv,
    }
