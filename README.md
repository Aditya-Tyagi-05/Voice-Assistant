# Voice-Assistant

This is a Python-based voice assistant that listens to your voice commands and performs tasks like searching Wikipedia, opening websites, and telling the current time.

## Features

- Greets the user based on the time of day.
- Recognizes voice commands using `speech_recognition`.
- Provides spoken responses using `pyttsx3`.
- Performs actions such as:
  - Searching Wikipedia.
  - Opening websites (YouTube, Google, Gmail, Facebook, etc.).
  - Telling the current time.
  - Opening Visual Studio Code.
  - Exiting gracefully when thanked.

## Installation

1. **Install Python**: Ensure Python 3.7 or higher is installed. Download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Run the following command to install the required libraries:
   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia pyaudio
