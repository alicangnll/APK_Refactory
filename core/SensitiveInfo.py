import os
from core.Config import SENSITIVE_KEYWORDS

class SensitiveInfo:
    def check_text_for_sensitive_keywords(file_path):
        matches = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    line = line.strip()
                    for keyword in SENSITIVE_KEYWORDS:
                        if keyword in line.lower():
                            matches.append((file_path, line_number, line))
                            break
        except UnicodeDecodeError:
            print(f"Failed to decode file: {file_path}")
        return matches
    
    def check_file_for_sensitive_keywords(file_path):
        matches = []
        try:
            for root, dirs, files in os.walk(file_path):
                 for file in files:
                     if file.endswith(".xml"):
                         print(file)
                         with open(file_path + "/" + file, 'r', encoding='utf-8') as file_open:
                             for line_number, line in enumerate(file_open, start=1):
                                line = line.strip()
                                for keyword in SENSITIVE_KEYWORDS:
                                    if keyword in line.lower():
                                        matches.append((file_open, line_number, line))
                                        break
        except UnicodeDecodeError:
            print(f"Failed to decode file: {file_path}")
            pass
        return matches