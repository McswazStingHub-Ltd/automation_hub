import socket

def show_network_info():
    hostname = socket.gethostname()

    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Unavailable"

    print("\n=== Network Information ===")
    print("Hostname:", hostname)
    print("IP Address:", ip)
