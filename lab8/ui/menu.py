"""
    Виводить головне меню з варіантами для користувача.
    Користувач може вибрати, що саме відобразити 
    чи експортувати з доступних графіків.
    
    Виводить список варіантів:
    1. Виведення екстремальних значень
    2. Побудова лінійного графіка температури
    3. Побудова графіка температури та вологості
    4. Побудова гістограми вологості
    5. Побудова кількох підграфіків
    6. Експорт графіка у форматі PNG
"""
import os
from views.subplots import plot_multiple_subplots

def display_menu():
    print("1. Display extreme values")
    print("2. Show Temperature Line Chart")
    print("3. Show Temperature vs Humidity Scatter Plot")
    print("4. Show Humidity Histogram")
    print("5. Show Multiple Subplots")
    print("6. Export Chart as PNG")

def handle_choice(choice, controller):
    """
    Обробляє вибір користувача та викликає відповідні методи з DataController для побудови графіків.
    
    Параметри:
    -----------
    choice : str
        Вибір користувача для виконання певної операції.
    
    controller : DataController
        Екземпляр класу DataController, який управляє даними та побудовою графіків.

    Якщо вибір не відповідає жодному з варіантів, виводиться повідомлення про помилку.
    
    Викликає відповідні методи з DataController:
    - display_extremes() для екстремальних значень
    - plot_chart() для побудови графіків
    - plot_multiple_subplots() для побудови кількох підграфіків
    - export_chart_as_png() для експорту графіка у формат PNG
    """
    if choice == '1':
        controller.display_extremes()
    elif choice == '2':
        controller.plot_chart("line") 
    elif choice == '3':
        controller.plot_chart("scatter")  
    elif choice == '4':
        controller.plot_chart("histogram")  
    elif choice == '5':
        plot_multiple_subplots(controller.data)
    elif choice == '6':
        export_chart_as_png(controller) 
    else:
        print("Invalid choice")

def export_chart_as_png(controller):
    """
    Експортує графік у формат PNG на основі вибору користувача.
    Параметри:
    -----------
    controller : DataController
        Екземпляр класу DataController, який містить 
        дані та методи для побудови графіків.
    
    Виводить запит на вибір типу графіка 
    (лінійний, розсіяння, гістограма) та назви файлу для експорту.
    Якщо введено некоректний тип графіка, 
    виводиться повідомлення про помилку.
    """
    plot_type = input("Enter the type of chart to export (line, scatter, histogram): ").lower()
    plot_instance = controller.get_plot_instance(plot_type)
    if plot_instance:
        filename = input("Enter the filename (without extension): ")
        # Формуємо шлях до файлу
        directory = "results/lab8"
        os.makedirs(directory, exist_ok=True)  # Створюємо каталог, якщо його немає
        full_path = os.path.join(directory, f"{filename}")
        
        print("Exporting chart as PNG...")
        plot_instance.plot(controller.data)  
        plot_instance.save(full_path)
        print(f"Chart exported as {full_path}")
    else:
        print("Invalid chart type. Please try again.")
