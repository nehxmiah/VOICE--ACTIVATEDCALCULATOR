import speech_recognition as sr
import pyttsx3
import threading
from typing import Callable, Optional

class SpeechHandler:
    """Handle speech recognition and text-to-speech"""
    
    def __init__(self, speech_rate: int = 150):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', speech_rate)
        self.is_listening = False
        self.listen_callback: Optional[Callable] = None
        
    def set_speech_rate(self, rate: int):
        """Set speaking rate"""
        self.engine.setProperty('rate', rate)
    
    def speak(self, text: str, blocking: bool = False):
        """Convert text to speech"""
        if blocking:
            self.engine.say(text)
            self.engine.runAndWait()
        else:
            threading.Thread(
                target=self._speak_thread, 
                args=(text,), 
                daemon=True
            ).start()
    
    def _speak_thread(self, text: str):
        """Thread for non-blocking speech"""
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen_once(self, timeout: int = 5) -> Optional[str]:
        """Listen for a single command"""
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
                text = self.recognizer.recognize_google(audio)
                return text
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return "UNKNOWN"
        except Exception as e:
            return f"ERROR: {str(e)}"
    
    def start_listening(self, callback: Callable):
        """Start continuous listening"""
        self.is_listening = True
        self.listen_callback = callback
        threading.Thread(target=self._listen_loop, daemon=True).start()
    
    def stop_listening(self):
        """Stop continuous listening"""
        self.is_listening = False
    
    def _listen_loop(self):
        """Continuous listening loop"""
        while self.is_listening:
            result = self.listen_once()
            if result and self.listen_callback:
                self.listen_callback(result)