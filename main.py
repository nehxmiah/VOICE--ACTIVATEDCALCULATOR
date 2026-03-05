import tkinter as tk
from tkinter import ttk
from calculator import Calculator
from clock import Clock
from speech_handler import SpeechHandler
from command_processor import CommandProcessor
from ui_components import (
    ClockDisplay, 
    CalculatorPanel, 
    VoiceControlPanel, 
    ConversationLog
)

class VoiceAssistantApp:
    """Main application class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Modular Voice Assistant")
        self.root.geometry("800x600")
        
        self.calculator = Calculator()
        self.clock = Clock()
        self.speech_handler = SpeechHandler()
        self.command_processor = CommandProcessor(self.calculator, self.clock)
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup user interface"""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        
        self.clock_display = ClockDisplay(main_frame, self.update_clock)
        self.clock_display.frame.grid(
            row=0, column=0, columnspan=2, 
            sticky=tk.W+tk.E, pady=5
        )
        
        self.calc_panel = CalculatorPanel(main_frame, self.handle_calculation)
        self.calc_panel.frame.grid(
            row=1, column=0, columnspan=2, 
            sticky=tk.W+tk.E, pady=5
        )
        
        self.voice_panel = VoiceControlPanel(main_frame, self.toggle_listening)
        self.voice_panel.frame.grid(
            row=2, column=0, columnspan=2, 
            sticky=tk.W+tk.E, pady=5
        )
        
        self.conv_log = ConversationLog(main_frame)
        self.conv_log.frame.grid(
            row=3, column=0, columnspan=2, 
            sticky=tk.W+tk.E+tk.N+tk.S, pady=5
        )
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
    
    def update_clock(self):
        """Update clock display"""
        time_str = self.clock.get_current_time(format_12hr=False)
        date_str = self.clock.get_current_date(full_format=True)
        self.clock_display.update_display(time_str, date_str)
    
    def handle_calculation(self):
        """Handle calculator button click"""
        expression = self.calc_panel.get_expression()
        try:
            result = self.calculator.evaluate(expression)
            self.calc_panel.set_result(str(result))
            self.log_message(f"Calculated: {expression} = {result}")
        except Exception as e:
            self.calc_panel.set_error(str(e))
            self.log_message(f"Calculation error: {str(e)}")
    
    def toggle_listening(self):
        """Toggle voice listening"""
        if not self.speech_handler.is_listening:
            self.speech_handler.start_listening(self.handle_voice_input)
            self.voice_panel.set_listening(True)
        else:
            self.speech_handler.stop_listening()
            self.voice_panel.set_listening(False)
    
    def handle_voice_input(self, text: str):
        """Handle voice input"""
        if text == "UNKNOWN":
            self.log_message("Could not understand audio")
            return
        
        if text.startswith("ERROR"):
            self.log_message(text)
            return
        
        self.log_message(f"You: {text}")
        
        # Process command through command processor
        response = self.command_processor.process(text)
        
        # Update calculator display if it was a calculation
        if any(keyword in text.lower() for keyword in ["calculate", "what is", "compute"]):
            expr = self.calculator.parse_spoken_expression(text)
            if expr:
                self.calc_panel.set_expression(expr)
                try:
                    result = self.calculator.evaluate(expr)
                    self.calc_panel.set_result(str(result))
                except Exception as e:
                    self.calc_panel.set_error(str(e))
        
        self.log_message(f"Assistant: {response}")
        self.speech_handler.speak(response)
    
    def log_message(self, message: str):
        """Add message to conversation log"""
        timestamp = self.clock.get_timestamp()
        self.conv_log.add_message(message, timestamp)


def main():
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()