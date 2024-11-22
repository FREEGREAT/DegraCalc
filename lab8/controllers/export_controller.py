"""
Клас для керування експортом графіків у різні формати (зображення, HTML).

"""
class ExportController:
    """
    Клас для керування експортом графіків у різні формати (зображення, HTML).
    Методи:
    --------
    export_plot(plot_instance, filename, format="png") :
        Експортує графік у зазначений файл та формат (за замовчуванням PNG).
        Параметри:
        -----------
        plot_instance : object
            Екземпляр графіка (наприклад, інстанс класу для побудови графіків), 
            який має метод `save`.
        filename : str
            Ім'я файлу для збереження графіка.
        format : str, optional
            Формат файлу для збереження (за замовчуванням "png").
    
    export_as_html(plot_instance, filename) :
        Експортує графік у HTML формат з використанням методу `save_as_html` класу графіка.
        Параметри:
        -----------
        plot_instance : object
            Екземпляр графіка, який має метод `save_as_html` для експорту в HTML.        
        filename : str
            Ім'я файлу для збереження HTML.

    prompt_and_export(plot_instance, filename_base, format="png") :
        Запитує користувача, чи хоче він зберегти графік. Якщо так, зберігає графік у файл.
        Параметри:
        -----------
        plot_instance : object
            Екземпляр графіка, який має методи для збереження графіка.
        filename_base : str
            Базове ім'я файлу для збереження (без розширення).        
        format : str, optional
            Формат файлу для збереження (за замовчуванням "png").
        """    
    def export_plot(self, plot_instance, filename, img_format="png"):
        """
        Експортує графік у вказаний файл і формат.
        Параметри:
        -----------
        plot_instance : object
            Екземпляр графіка, що має метод `save` для збереження.
        filename : str
            Ім'я файлу для збереження графіка.
        format : str, optional
            Формат файлу (за замовчуванням "png").
        """
        plot_instance.save(filename, img_format)    
    def export_as_html(self, plot_instance, filename):
        """
        Експортує графік у формат HTML.
        Параметри:
        -----------
        plot_instance : object
            Екземпляр графіка, що має метод `save_as_html` для експорту в HTML.        
        filename : str
            Ім'я файлу для збереження HTML.
        """
        plot_instance.save_as_html(filename)
    
    def prompt_and_export(self, plot_instance, filename_base, img_format="png"):
        """
        Запитує користувача, чи хоче він зберегти графік, і якщо так — експортує його у файл.

        Параметри:
        -----------
        plot_instance : object
            Екземпляр графіка, що має методи для збереження графіків.
        
        filename_base : str
            Базове ім'я файлу (без розширення), яке буде використано при експорті.
        
        format : str, optional
            Формат файлу для збереження (за замовчуванням "png").
        """
        save_choice = input("Do you want to save this chart? (y/n): ")
        if save_choice.lower() == 'y':
            filename = f"{filename_base}.{img_format}"
            self.export_plot(plot_instance, filename, img_format)
            print(f"Chart saved as {filename}.")
