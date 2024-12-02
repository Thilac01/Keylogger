import socket
import time
import keyboard

def get_local_ip():
    """Get the local IP address of the machine running the script."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))  # No real connection, just to get the local IP
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'  # Fallback if unable to get the IP
    finally:
        s.close()
    return ip

def send_data():
    server_ip = '192.168.1.6'  # IP of Machine A (Server)
    server_port = 12345        # Same port as the server

    print(f"Attempting to connect to {server_ip}:{server_port}...")

    # Create a socket and connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    print(f"Press any key to send data. Press ESC to stop.")

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            timestamp = time.time()
            message = f"Key: {event.name}, Time: {timestamp}\n"
            sock.send(message.encode('utf-8'))  # Send data via TCP
            print(f"Sent: {message}")

        if event.name == 'esc':
            print("Stopping...")
            break

    sock.close()

if __name__ == "__main__":
    send_data()
