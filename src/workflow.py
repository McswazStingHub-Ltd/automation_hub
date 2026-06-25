from src.network_info import show_network_info
from src.password_generator import generate_password
from src.logger import log_action


def run_workflow():
    print("\n=== Automation Workflow ===")

    log_action("Workflow started")

    print("\nStep 1: Network Information")
    show_network_info()

    print("\nStep 2: Password Generator")
    generate_password()

    log_action("Workflow completed")

    print("\nWorkflow completed.")
