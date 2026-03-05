import datetime
from typing import Dict

class Clock:
    """Clock module for time and date operations"""
    
    @staticmethod
    def get_current_time(format_12hr: bool = True) -> str:
        """Get current time as string"""
        now = datetime.datetime.now()
        if format_12hr:
            return now.strftime("%I:%M:%S %p")
        return now.strftime("%H:%M:%S")
    
    @staticmethod
    def get_current_date(full_format: bool = True) -> str:
        """Get current date as string"""
        now = datetime.datetime.now()
        if full_format:
            return now.strftime("%A, %B %d, %Y")
        return now.strftime("%Y-%m-%d")
    
    @staticmethod
    def get_timestamp() -> str:
        """Get timestamp for logging"""
        return datetime.datetime.now().strftime("%H:%M:%S")
    
    @staticmethod
    def get_time_components() -> Dict[str, int]:
        """Get time as components"""
        now = datetime.datetime.now()
        return {
            'hour': now.hour,
            'minute': now.minute,
            'second': now.second,
            'day': now.day,
            'month': now.month,
            'year': now.year
        }