import os


class FileComparator:
    def read_file_lines(self, filepath):
        """Зчитує рядки з файлу та повертає множину."""
        if not os.path.exists(filepath):
            return set()
        with open(filepath, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())

    def find_intersection(self, set1, set2):
        """Знаходить спільні рядки."""
        return set1.intersection(set2)

    def find_difference(self, set1, set2):
        """Знаходить рядки, що є лише в одному з файлів."""
        return set1.symmetric_difference(set2)

    def write_to_file(self, filepath, data):
        """Записує дані у файл."""
        with open(filepath, 'w', encoding='utf-8') as f:
            for line in sorted(data):
                f.write(f"{line}\n")


def main():
    comparator = FileComparator()
    lines1 = comparator.read_file_lines('file1.txt')
    lines2 = comparator.read_file_lines('file2.txt')

    comparator.write_to_file('same.txt', comparator.find_intersection(lines1, lines2))
    comparator.write_to_file('diff.txt', comparator.find_difference(lines1, lines2))


if __name__ == "__main__":
    main()
