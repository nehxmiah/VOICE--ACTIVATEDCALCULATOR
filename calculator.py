import math
from typing import Union

class Calculator:
    """Calculator module for mathematical operations"""
    
    def __init__(self):
        self.safe_functions = {
            'sqrt': math.sqrt,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'log10': math.log10,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e,
            'abs': abs,
            'pow': pow
        }
    
    def evaluate(self, expression: str) -> Union[float, int]:
        """Safely evaluate a mathematical expression"""
        expr = expression.replace('^', '**').replace(' ', '')
        
        try:
            result = eval(expr, {"__builtins__": {}}, self.safe_functions)
            if isinstance(result, float):
                return round(result, 6)
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")
    
    def parse_spoken_expression(self, text: str) -> str:
        """Convert spoken words to mathematical expression"""
        import re
        
        # Remove common command prefixes
        text = re.sub(r'^(calculate|compute|what is)\s+', '', text, flags=re.IGNORECASE)
        text_lower = text.lower().strip()
        
        # Word-to-symbol replacements (order matters - longer phrases first)
        replacements = [
            ("multiplied by", "*"),
            ("divided by", "/"),
            ("to the power of", "**"),
            ("square root of", "sqrt("),
            ("sine of", "sin("),
            ("cosine of", "cos("),
            ("tangent of", "tan("),
            ("plus", "+"),
            ("minus", "-"),
            ("times", "*"),
            ("squared", "**2"),
            ("cubed", "**3"),
        ]
        
        for word, symbol in replacements:
            text_lower = text_lower.replace(word, symbol)
        
        # Keep only valid expression characters
        text_lower = re.sub(r'[^0-9+\-*/.()^]', '', text_lower)
        
        if not text_lower or text_lower.isspace():
            return ""
        
        # Replace ^ with ** for power operations
        text_lower = text_lower.replace("^", "**")
        
        # Balance parentheses
        open_count = text_lower.count('(')
        close_count = text_lower.count(')')
        text_lower += ')' * (open_count - close_count)
        
        return text_lower.strip()