import socket
import serial

# Set up serial connection to ESP32 (adjust port as necessary)
arduino = serial.Serial('/dev/ttyUSB0', 9600)

# Set up the server
host = '0.0.0.0'
port = 12345

# Create socket and listen for data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    print("Listening for connection...")

    conn, addr = s.accept()
    with conn:  # Only close when you're truly done
        print(f"Connection established with {addr}")

        while True:
            # Receive data from the laptop
            data = conn.recv(1024).decode()
            if data:
                print(f"Received data: {data}")

                # Send data to ESP32
                arduino.write(data.encode())
                print(f"Sent data to ESP32: {data}")

                # Wait for feedback from ESP32
                if arduino.in_waiting > 0:
                    feedback = arduino.readline().decode().strip()
                    print(f"Received feedback from ESP32: {feedback}")

                    # Send feedback back to the laptop
                    conn.sendall(feedback.encode())
                    print(f"Sent feedback to Laptop: {feedback}")
