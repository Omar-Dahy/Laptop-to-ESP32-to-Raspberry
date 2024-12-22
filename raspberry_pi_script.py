import serial
import time

# Set up serial connection to Arduino (adjust port as necessary)
arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Update port if needed
time.sleep(2)  # Allow time for the serial connection to initialize

# Function to send data to Arduino and get response
def send_data_to_arduino(data):
    arduino.write(data.encode())  # Send the data to Arduino
    print(f"Sent data to Arduino: {data}")
    
    # Wait for Arduino's response
    while arduino.in_waiting == 0:
        time.sleep(0.1)  # Wait for response from Arduino
    
    feedback = arduino.readline().decode().strip()  # Read feedback from Arduino
    return feedback

# Main loop to send and receive data
while True:
    data = input("Enter command for Arduino (AA/BB): ")
    if data in ["AA", "BB"]:
        feedback = send_data_to_arduino(data)  # Send data and get feedback
        print(f"Feedback from Arduino: {feedback}")
    else:
        print("Invalid command. Please enter 'AA' or 'BB'.")
