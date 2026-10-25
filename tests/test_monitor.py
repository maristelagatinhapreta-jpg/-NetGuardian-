from src.monitor import get_network_stats


def test_get_network_stats():
    data = get_network_stats()
    assert "bytes_sent" in data
    assert "bytes_recv" in data
    assert data["bytes_sent"] >= 0
    assert data["bytes_recv"] >= 0
