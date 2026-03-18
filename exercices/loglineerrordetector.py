import re

def has_critical_error(log_line: str) -> bool:
    pattern = r"\bERROR:|\bFAIL:"
    if re.search(pattern, log_line.upper()):
        return True
    return False

if __name__ == "__main__":
    line1 = "2023-10-27 INFO: System started successfully."
    line2 = "2023-10-27 ERROR: Database connection lost."
    line3 = "2023-10-27 WARN: Disk usage high, but operation will not fail all clear."
    line4 = "2023-10-27 DEBUG: User 'test' initiated a fail: sequence."

    print(has_critical_error(line3))