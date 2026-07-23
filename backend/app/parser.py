import re


def parse_command(text):
    if not text or not text.strip():
        return (None, None, None)

    match = re.search(r"[A-Z]+\d+", text, re.IGNORECASE)
    if not match:
        return (None, None, None)

    command_text = text.lower()

    if "write" in command_text:
        remaining = text.split("write", 1)[1].strip()
        if " to " not in remaining:
            return (None, None, None)

        parts = remaining.split(" to ", 1)
        value = parts[0].strip()
        return ("write", match.group(), value)

    if "read" in command_text:
        return ("read", match.group(), None)

    return (None, None, None)


def parse_text(text):
    return parse_command(text)
