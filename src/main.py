import os

def show_system_info():
    print("\n=== System Information ===")
    print(f"Current directory: {os.getcwd()}")
    print(f"Operating System: {os.name}")

def notes_manager():
    note = input("Enter a note: ")

    with open("notes.txt", "a") as f:
        f.write(note + "\n")

    print("Note saved.")

def main():
    while True:
        print("\n=== Automation Hub ===")
        print("1. Say Hello")
        print("2. Show Version")
        print("3. System Information")
        print("4. Notes Manager")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print("Hello, McswazStingHub-Ltd!")

        elif choice == "2":
            print("Automation Hub v3.0")

        elif choice == "3":
            show_system_info()

        elif choice == "4":
            notes_manager()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
