"""
Модуль для роботи з файлами, що забезпечує збереження вказаного контенту до файлу у заданій директорії.

Клас:
    FileManager: Клас для управління файлами, включає метод для збереження контенту у файл.

Methods:
    save_to_file(content, filename):
        Зберігає текстовий контент у файл у визначеній директорії. Автоматично створює потрібні директорії, якщо вони не існують.
"""

import os

class FileManager:
    """
    Клас для управління файлами, який дозволяє зберігати дані у файли у визначеній структурі директорій.
    """

    @staticmethod
    def save_to_file(content, filename):
        """
        Зберігає текстовий контент у файл у підпапці `results/lab3`.

        Метод створює необхідні директорії, якщо вони відсутні, і зберігає контент у файл.

        Args:
            content (str): Текстовий контент, який потрібно записати у файл.
            filename (str): Ім'я файлу, в який буде збережено контент.

        Raises:
            IOError: Якщо виникла помилка під час збереження файлу.

        Example:
            >>> FileManager.save_to_file("Hello, world!", "example.txt")
            Файл успішно збережено: /path/to/results/lab3/example.txt
        """
        try:
            # Визначаємо шлях до директорії для збереження
            directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "results", "lab3")
            
            # Якщо директорія не існує, створюємо її
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Повний шлях до файлу
            file_path = os.path.join(directory, filename)
            
            # Зберігаємо контент у файл
            with open(file_path, 'w') as file:
                file.write(content)
            
            print(f"Файл успішно збережено: {file_path}")
        except Exception as e:
            raise IOError(f"Помилка збереження файлу: {filename}. Причина: {str(e)}")
