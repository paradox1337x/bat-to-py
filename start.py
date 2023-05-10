import os
import subprocess
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select batch file",
    filetypes=[("Batch files", "*.bat"), ("All files", "*.*")]
)

if not file_path:
    exit()

with open(file_path, 'r') as batch_file:
    batch_contents = batch_file.read()

python_code = """import os
import subprocess

{}

""".format('\n'.join(f"subprocess.call('{command}', shell=True)" for command in batch_contents.splitlines()))

script_path = os.path.splitext(file_path)[0] + ".py"
with open(script_path, 'w') as python_file:
    python_file.write(python_code)

subprocess.call(['python', script_path])
