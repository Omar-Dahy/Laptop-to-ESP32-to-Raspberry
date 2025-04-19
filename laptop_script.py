import socket

# Specify the Raspberry Pi IP and port
host = '192.168.1.2'  # Raspberry Pi IP
port = 12345  # Port for communication

# Create the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    while True:
        data = input("Input command (AA for 5 blinks, BB for 10): ")

        s.sendall(data.encode())  # Send data to Raspberry Pi
        print(f"Sent data: {data}")
