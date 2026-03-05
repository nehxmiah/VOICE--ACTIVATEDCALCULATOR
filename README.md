Voice Assistant

A modular Python-based voice assistant with a graphical user interface. This application combines speech recognition, text-to-speech, calculator functionality, and clock display in an easy-to-use interface.

Features

Voice Recognition: Listen to and process voice commands using speech recognition
Text-to-Speech: Audio feedback with customizable speech rate
Calculator: Perform mathematical calculations via voice commands
Clock Display: Real-time time and date display
Conversation Log: Track interaction history
Modular Architecture: Easy to extend with new features and commands

Project Structure


voice assistant/
     main.py                 Main application entry point
    speech_handler.py       Speech recognition and TTS handling
    command_processor.py    Voice command processing and routing
    calculator.py           Calculator module
    clock.py                Clock and date functionality
    ui_components.py        GUI components (Tkinter)
    README.md               This file


 Requirements

- Python 3.6+
- tkinter (usually included with Python)
- speech_recognition
- pyttsx3

 Installation

1. Clone or download the project
2. Install required dependencies:
   bash
   pip install SpeechRecognition pyttsx3
   

Usage

Run the application:
bash
python main.py


The GUI will open with the following components:
- Clock Display: Shows current time and date
- Calculator Panel: Perform calculations
- Voice Control Panel: Start/stop voice listening
- Conversation Log: View command history and responses

Supported Voice Commands

- Time/Clock: "What time is it?" or "Tell me the time"
- Date: "What is the date?" or "Tell me today's date"
- Calculations: "Calculate 5 plus 3" or "What is 10 times 20"



 Main Components

- VoiceAssistantApp: Main application class managing UI and modules
- SpeechHandler: Handles speech recognition and text-to-speech conversion
- CommandProcessor: Routes voice commands to appropriate modules
- Calculator: Performs mathematical operations
- Clock: Provides time and date information
- UI Components: Tkinter-based interface elements

Configuration

In 'speech_handler.py', you can adjust the speech rate:
python
self.engine.setProperty('rate', 150)   Default rate is 150


License

This project is open source and available under the MIT License.

 Author
 NEHXMIAH