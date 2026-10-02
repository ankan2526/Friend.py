import subprocess
import tempfile
import os

BLOCKED_WORDS = ['import os', 'import sys', 'import subprocess', 'eval', 'exec']

def check_blocked_words(code: str) -> bool:
    for word in BLOCKED_WORDS:
        if word in code:
            return False
    return True

def run_code(code: str) -> str:
    if not check_blocked_words(code):
        return "Error: Code contains blocked words or unsafe operations."
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(code)
        temp_file_path = temp_file.name

    try:
        result = subprocess.run(
            ['python3', temp_file_path],
            capture_output=True,
            text=True,
            timeout=3
        )
        output = result.stdout + result.stderr
        return output
    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out (3 seconds limit)."
    except Exception as e:
        return f"Error executing code: {e}"
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
