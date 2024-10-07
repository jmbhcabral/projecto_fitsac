''' Formatters for various data types. '''
from datetime import timedelta, date


def format_duration(duration):
    ''' Format a duration in seconds to a human readable format. '''
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"


def convert_dates_to_str(data):
    """Convert date objects to strings in the data dictionary."""
    for key, value in data.items():
        if isinstance(value, date):
            data[key] = value.isoformat()
    return data
