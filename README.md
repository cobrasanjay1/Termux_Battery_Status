
# Battery Monitor Script for Termux

## Overview

This Python script, `bat.py`, monitors the battery status on a Termux environment. When the battery level reaches 80% or higher, the script uses Termux's text-to-speech (TTS) functionality to announce the battery percentage. The script also stops running when the charger is unplugged.

## Features

- Monitors battery status in real-time using the Termux API.
- Announces the battery percentage when it reaches 80% or higher using Termux TTS.
- Exits when the charger is unplugged.

## Requirements

- **Termux** installed on an Android device.
- Termux API packages installed:
  - `termux-battery-status`
  - `termux-tts-speak`
- Python 3.x installed in Termux.

### Installing Termux API

To use this script, you need to install Termux API:

```bash
pkg install termux-api
```

## Usage

1. Clone this repository or download `bat.py` to your Termux environment.
2. Run the script using Python:

```bash
python bat.py
```

The script will continuously monitor the battery status and speak the percentage when it reaches 80%. It will automatically stop if the charger is unplugged.

## How It Works

- **Battery Status**: The script retrieves battery information using `termux-battery-status`, which provides data in JSON format.
- **Voice Feedback**: When the battery percentage is 80% or higher, the script uses `termux-tts-speak` to announce the current battery percentage.
- **Charger Monitoring**: The script stops execution when it detects that the charger is unplugged.

## Example Output

- Spoken message when the battery is at 80%:
  ```
  Battery percentage is 80 percent
  ```

- Console message when the charger is unplugged:
  ```
  Charger unplugged. Exiting.
  ```

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to this project.

## License

This project is licensed under the MIT License.
