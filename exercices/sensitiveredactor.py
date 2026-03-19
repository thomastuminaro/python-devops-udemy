import re

def redact_sensitive_data(content: str) -> str:
    if not isinstance(content, str):
        raise TypeError("content must be a string.")
    
    redacted_list = []
    for line in content.split("\n"): 
        if re.match(r"(?i)(?:api_key|password|secret)\s*[=:]\s*", line):
            pattern = r'([=:]\s*)"?(.+)"?\s*'
            replacement = r'\1[REDACTED]'
            redacted_list.append(re.sub(pattern, replacement, line))
        else:
            redacted_list.append(line)

    return ("\n").join(redacted_list)

if __name__ == "__main__":
    file_content = 'host = web.service;local\napi_Key = "abc-123"\nretries = 3\n\nPassword:secret\nuser = admin'
    redacted_content = redact_sensitive_data(file_content)
    print(redacted_content)