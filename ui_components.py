import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import Callable, Optional

class ClockDisplay:
    """Clock display UI component"""
    
    def __init__(self, parent, update_callback: Optional[Callable] = None):
        self.frame = ttk.LabelFrame(parent, text="Clock", padding="10")

        self.time_label = ttk.Label(self.frame, font=('Arial', 24, 'bold'))
        self.time_label.pack()

        self.date_label = ttk.Label(self.frame, font=('Arial', 12))
        self.date_label.pack()

        if update_callback:
            self.update_callback = update_callback
            # Defer the first update to avoid calling callback before object is fully initialized
            self.frame.after(100, self._schedule_update)
    
    def update_display(self, time_str: str, date_str: str):
        """Update clock display"""
        self.time_label.config(text=time_str)
        self.date_label.config(text=date_str)
    
    def _schedule_update(self):
        """Schedule periodic updates"""
        self.update_callback()
        self.time_label.after(1000, self._schedule_update)


class CalculatorPanel:
    """Calculator UI component"""
    
    def __init__(self, parent, calculate_callback: Callable):
        self.frame = ttk.LabelFrame(parent, text="Calculator", padding="10")
        self.calculate_callback = calculate_callback
        
        self.entry = ttk.Entry(self.frame, font=('Arial', 14))
        self.entry.pack(fill=tk.X, pady=5)
        self.entry.bind('<Return>', lambda e: self.calculate_callback())
        
        ttk.Button(
            self.frame, 
            text="Calculate", 
            command=self.calculate_callback
        ).pack(side=tk.LEFT, padx=5)
        
        self.result_label = ttk.Label(
            self.frame, 
            text="Result: ", 
            font=('Arial', 12, 'bold')
        )
        self.result_label.pack(side=tk.LEFT, padx=5)
    
    def get_expression(self) -> str:
        """Get expression from entry"""
        return self.entry.get()
    
    def set_expression(self, expr: str):
        """Set expression in entry"""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, expr)
    
    def set_result(self, result: str):
        """Display result"""
        self.result_label.config(text=f"Result: {result}")
    
    def set_error(self, error: str):
        """Display error"""
        self.result_label.config(text=f"Error: {error}")


class VoiceControlPanel:
    """Voice control UI component"""
    
    def __init__(self, parent, toggle_callback: Callable):
        self.frame = ttk.LabelFrame(parent, text="Voice Control", padding="10")
        self.toggle_callback = toggle_callback
        
        self.listen_btn = ttk.Button(
            self.frame, 
            text="Start Listening", 
            command=self.toggle_callback
        )
        self.listen_btn.pack(side=tk.LEFT, padx=5)
        
        self.status_label = ttk.Label(
            self.frame, 
            text="Status: Ready", 
            foreground="green"
        )
        self.status_label.pack(side=tk.LEFT, padx=5)
    
    def set_listening(self, is_listening: bool):
        """Update listening state"""
        if is_listening:
            self.listen_btn.config(text="Stop Listening")
            self.status_label.config(text="Status: Listening...", foreground="red")
        else:
            self.listen_btn.config(text="Start Listening")
            self.status_label.config(text="Status: Ready", foreground="green")


class ConversationLog:
    """Conversation log UI component"""
    
    def __init__(self, parent):
        self.frame = ttk.LabelFrame(parent, text="Conversation Log", padding="10")
        
        self.text_widget = scrolledtext.ScrolledText(
            self.frame, 
            height=15, 
            wrap=tk.WORD, 
            font=('Arial', 10)
        )
        self.text_widget.pack(fill=tk.BOTH, expand=True)
    
    def add_message(self, message: str, timestamp: str = ""):
        """Add message to log"""
        if timestamp:
            self.text_widget.insert(tk.END, f"[{timestamp}] {message}\n")
        else:
            self.text_widget.insert(tk.END, f"{message}\n")
        self.text_widget.see(tk.END)
    
    def clear(self):
        """Clear log"""
        self.text_widget.delete(1.0, tk.END)