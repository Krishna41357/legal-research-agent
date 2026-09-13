
import re

def clean_text(text:str)->str:
    #Remove leading/trailing whitespaces from each line

    lines = [line.strip() for line in text.splitlines()]
    # Remove completely empty lines
    lines = [line for line in lines if line]

    # Normalize multiple spaces inside a line
    lines = [re.sub(r"\s+"," ",line) for line in lines]

    # Join paragraphs with a blank line
    return "\n\n".join(lines)

