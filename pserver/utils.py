import re

def sanitize_filename(title):
    """Remove unsafe characters from video title."""
    return re.sub(r'[<>:"/\\|?*]', "", title).replace(" ", "_")
