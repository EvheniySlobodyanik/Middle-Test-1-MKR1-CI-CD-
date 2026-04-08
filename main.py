import os

class FileComparator:
    def read_file_lines(self, filepath):
        """Зчитує рядки з файлу та повертає множину."""
        if not os.path.exists(filepath):
            return set()
        with open(filepath, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())