import re

def unix_match(filename: str, pattern: str) -> bool:
    pattern = pattern.replace("[!", "[^")
    return bool(re.match(pattern, filename))

