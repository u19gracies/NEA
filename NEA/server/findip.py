import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))  # This is a random public IP address
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'  # Default to localhost
    finally:
        s.close()
    return ip_address

print("Local IP address:", get_local_ip())