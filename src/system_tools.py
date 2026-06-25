import os
import platform
import shutil


def show_system_info():
    print("\n=== System Information ===")
    print(f"OS: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Current Directory: {os.getcwd()}")

    total, used, free = shutil.disk_usage("/")

    print("\n=== Disk Usage ===")
    print(f"Total: {total // (1024**3)} GB")
    print(f"Used: {used // (1024**3)} GB")
    print(f"Free: {free // (1024**3)} GB")
