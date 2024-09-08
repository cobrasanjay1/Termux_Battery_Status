import subprocess
import json
import time

def get_battery_status():
    # Get battery status from Termux
    result = subprocess.run(['termux-battery-status'], capture_output=True, text=True)
    
    # Parse the JSON output
    battery_status = json.loads(result.stdout)
    
    return battery_status

def speak_battery_percentage(percentage):
    # Command to speak the battery percentage using Termux TTS
    speak_command = f"Battery percentage is {percentage} percent"
    subprocess.run(['termux-tts-speak', speak_command])

def main():
    while True:
        # Get the current battery status
        battery_status = get_battery_status()
        battery_percentage = battery_status['percentage']
        is_charging = battery_status['status'] == "CHARGING"

        # Check if the battery percentage is greater than or equal to 80%
        if battery_percentage >= 80:
            speak_battery_percentage(battery_percentage)

        # Break the loop if the charger is unplugged
        if not is_charging:
            print("Charger unplugged. Exiting.")
            break

        # Sleep for a short period before checking again
        time.sleep(5)

if __name__ == "__main__":
    main()

