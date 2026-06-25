import os
import platform

def show_system_info():
    print("\n=== System Information ===")
    print("OS:", platform.system())
    print("Release:", platform.release())
    print("Machine:", platform.machine())
    print("Current Directory:", os.getcwd())
