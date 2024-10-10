class FileManager:
    @staticmethod
    def save_to_file(content, filename):
        try:
            with open(filename, 'w') as file:
                file.write(content)
        except Exception as e:
            raise IOError(f"Помилка збереження файлу: {filename}. Причина: {str(e)}")
