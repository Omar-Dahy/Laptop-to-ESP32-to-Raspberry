int ledPin = 2;  // LED pin (change if your ESP32 uses a different pin)

void setup() {
  Serial.begin(115200);  // Initialize serial communication at a higher baud rate
  pinMode(ledPin, OUTPUT);  // Set LED pin as an output
}

void loop() {
  if (Serial.available() > 0) {
    String receivedData = Serial.readString();  // Read incoming data
    
    if (receivedData == "AA\n") {  // Include newline character for ESP32 serial
      blinkLed(5);  // Blink LED 5 times for "AA"
      Serial.println("LED blinked 5 times");  // Send feedback to Raspberry Pi
    } else if (receivedData == "BB\n") {  // Include newline character for ESP32 serial
      blinkLed(10);  // Blink LED 10 times for "BB"
      Serial.println("LED blinked 10 times");  // Send feedback to Raspberry Pi
    } else {
      Serial.println("Unknown command");  // Invalid command
    }
  }
}

// Function to blink the LED 'times' number of times
void blinkLed(int times) {
  for (int i = 0; i < times; i++) {
    digitalWrite(ledPin, HIGH);  // Turn the LED on
    delay(500);  // Wait for 500 ms
    digitalWrite(ledPin, LOW);  // Turn the LED off
    delay(500);  // Wait for 500 ms
  }
}
