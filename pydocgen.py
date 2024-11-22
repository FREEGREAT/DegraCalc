import os
import pydoc

def remove_empty_files(root_dir):
    """Видаляє порожні файли у вказаній директорії."""
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == 0:  # Перевіряє, чи файл порожній
                print(f"Видаляється порожній файл: {file_path}")
                os.remove(file_path)

def generate_docs(root_dir, output_dir="docs"):
    """Генерує HTML-документацію для всіх .py файлів у проєкті."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Створює директорію для документації

    # Групує файли за лабораторіями (наприклад, lab1, lab2, ...)
    for lab_dir in os.listdir(root_dir):
        lab_path = os.path.join(root_dir, lab_dir)
        if os.path.isdir(lab_path) and lab_dir.startswith("lab"):
            print(f"Обробка директорії лабораторної роботи: {lab_dir}")
            for root, _, files in os.walk(lab_path):
                for file in files:
                    if file.endswith(".py"):
                        module_path = os.path.splitext(os.path.relpath(
                            os.path.join(root, file), lab_path))[0]
                        module_name = module_path.replace(os.sep, ".")
                        print(f"Генерація документації для модуля: {module_name}")
                        try:
                            # Генерує HTML-документ для модуля
                            output_file = os.path.join(output_dir, 
                                                       f"{lab_dir}_{module_name.replace('.', '_')}.html")
                            with open(output_file, "w", encoding="utf-8") as f:
                                f.write(pydoc.html.document(pydoc.importfile(os.path.join(root, file))))
                        except Exception as e:
                            print(f"Помилка для модуля {module_name}: {e}")

if __name__ == "__main__":
    root_directory = "."  
    remove_empty_files(root_directory)  
    generate_docs(root_directory) 
