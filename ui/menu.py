from controllers.data_controller import DataController
from views.subplots import plot_multiple_subplots

def display_menu():
    print("1. Display extreme values")
    print("2. Show Temperature Line Chart")
    print("3. Show Temperature vs Humidity Scatter Plot")
    print("4. Show Humidity Histogram")
    print("5. Show Multiple Subplots")

# ui/menu.py
def handle_choice(choice, controller):
    if choice == '1':
        controller.display_extremes()
    elif choice == '2':
        controller.plot_chart("line")  # Замість plot_line_chart
    elif choice == '3':
        controller.plot_chart("scatter")  # Замість plot_scatter_chart
    elif choice == '4':
        controller.plot_chart("histogram")  # Замість plot_histogram
    elif choice == '5':
        plot_multiple_subplots(controller.data)
    else:
        print("Invalid choice")


# ui.py

def export_visualization(controller, plot_type):
    filename = input("Enter filename (without extension): ")
    format = input("Choose format - PNG, SVG, or HTML: ").lower()

    if format == "html":
        controller.export_as_html(plot_type, filename)
    else:
        controller.export_as_image(plot_type, filename, format)
