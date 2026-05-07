import RPi.GPIO as GPIO
import time

# --- Pin Configuration (BCM numbering) ---
IN1 = 17  # Left motor forward
IN2 = 27  # Left motor backward
IN3 = 22  # Right motor forward
IN4 = 23  # Right motor backward

# --- Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in (IN1, IN2, IN3, IN4):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


# --- Motor Control Functions ---

def drive_forward():
    """Power both motors to drive the rover forward."""
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def drive_backward():
    """Reverse both motors to drive the rover backward."""
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop():
    """Stop all motors."""
    for pin in (IN1, IN2, IN3, IN4):
        GPIO.output(pin, GPIO.LOW)


# --- Main Loop ---

if __name__ == "__main__":
    try:
        print("Rover starting...")

        print("Driving forward for 3 seconds...")
        drive_forward()
        time.sleep(3)

        print("Stopping for 1 second...")
        stop()
        time.sleep(1)

        print("Driving backward for 3 seconds...")
        drive_backward()
        time.sleep(3)

        print("Stopping.")
        stop()

    except KeyboardInterrupt:
        print("\nInterrupted by user.")

    finally:
        stop()
        GPIO.cleanup()
        print("GPIO cleaned up. Goodbye!")
