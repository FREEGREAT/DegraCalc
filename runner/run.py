
import sys
import os

# Додає головну директорію проекту до шляхів Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user_interface.user_interface import UserInterface
def run_ascii_art_generator():
    try:
        ui = UserInterface()
        color = ui.get_user_input()
        
        if color:
            ui.preview_ascii_art(color)
            
            save = input("Бажаєте зберегти ASCII-арт? (y/n): ").lower()
            if save == 'y':
                ui.save_ascii_art()
    except Exception as e:
        print(f"Сталася помилка під час виконання генератора ASCII-арту: {str(e)}")

def main():
    labs = [
        {"name": "Генератор ASCII-арту", "function": run_ascii_art_generator},
        # Додавайте нові лабораторні роботи тут у форматі:
        # {"name": "Назва лабораторної", "function": ваша_функція}
    ]
    
    while True:
        print("\nВиберіть лабораторну роботу для запуску:")
        for i, lab in enumerate(labs, start=1):
            print(f"{i}. {lab['name']}")
        print(f"{len(labs) + 1}. Вихід")

        try:
            choice = int(input("Ваш вибір: "))

            if 1 <= choice <= len(labs):
                labs[choice - 1]["function"]()
            elif choice == len(labs) + 1:
                print("Вихід з програми.")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, введіть номер лабораторної роботи.")
        except Exception as e:
            print(f"Сталася помилка: {str(e)}")

if __name__ == "__main__":
    main()
