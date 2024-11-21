from controllers.data_controller import DataController
from ui.menu import display_menu, handle_choice

def main():
    file_path = 'data/weather_data.csv'
    controller = DataController(file_path)

    while True: 
        display_menu()
        choice = input("Select an option (or 'q' to quit): ")
        
        if choice.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        handle_choice(choice, controller) 

if __name__ == "__main__":
    main()
