# real_time_package/runner.py

import subprocess
import os

def run_updater():
    script_path = os.path.join(os.path.dirname(__file__), 'updater.py')
    subprocess.Popen(["python", script_path])
