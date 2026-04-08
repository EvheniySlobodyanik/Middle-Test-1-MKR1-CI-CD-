import os

class FileComparator:
    def read_file_lines(self, filepath):
        """Зчитує рядки з файлу та повертає множину."""
        if not os.path.exists(filepath):
            return set()
        with open(filepath, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
        
    def find_intersection(self, set1, set2):
        """Знаходить персонажів, які є в обох списках."""
        return set1.intersection(set2)
    
    def find_difference(self, set1, set2):
        """Знаходить унікальних персонажів (симетрична різниця)."""
        return set1.symmetric_difference(set2)