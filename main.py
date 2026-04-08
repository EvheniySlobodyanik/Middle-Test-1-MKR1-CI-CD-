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
    
    def write_to_file(self, filepath, data):
        """Записує імена персонажів у файл."""
        with open(filepath, 'w', encoding='utf-8') as f:
            for line in sorted(data):
                f.write(f"{line}\n")

def main():
    comparator = FileComparator()

    banner1 = comparator.read_file_lines('file1.txt')
    banner2 = comparator.read_file_lines('file2.txt')
    
    comparator.write_to_file('same.txt', comparator.find_intersection(banner1, banner2))
    comparator.write_to_file('diff.txt', comparator.find_difference(banner1, banner2))

if __name__ == "__main__":
    main()