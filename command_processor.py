from calculator import Calculator
from clock import Clock
from typing import Dict, Callable

class CommandProcessor:
    """Process voice commands and route to appropriate modules"""
    
    def __init__(self, calculator: Calculator, clock: Clock):
        self.calculator = calculator
        self.clock = clock
        self.commands: Dict[str, Callable] = {
            'time': self._handle_time,
            'clock': self._handle_time,
            'date': self._handle_date,
            'calculate': self._handle_calculation,
            'what is': self._handle_calculation,
            'compute': self._handle_calculation
        }
    
    def process(self, text: str) -> str:
        """Process command and return response"""
        text_lower = text.lower()
        
        for keyword, handler in self.commands.items():
            if keyword in text_lower:
                return handler(text_lower)
        
        return self._handle_unknown()
    
    def _handle_time(self, text: str) -> str:
        """Handle time queries"""
        time_str = self.clock.get_current_time(format_12hr=True)
        return f"The time is {time_str}"
    
    def _handle_date(self, text: str) -> str:
        """Handle date queries"""
        date_str = self.clock.get_current_date(full_format=True)
        return f"Today is {date_str}"
    
    def _handle_calculation(self, text: str) -> str:
        """Handle calculation requests"""
        expr = self.calculator.parse_spoken_expression(text)
        if expr:
            try:
                result = self.calculator.evaluate(expr)
                return f"The answer is {result}"
            except Exception as e:
                return f"I couldn't calculate that: {str(e)}"
        return "I couldn't find a calculation in your request"
    
    def _handle_unknown(self) -> str:
        """Handle unknown commands"""
        return ("I can help with time, date, and calculations. "
                "Try asking 'what time is it?' or 'calculate 5 plus 3'")