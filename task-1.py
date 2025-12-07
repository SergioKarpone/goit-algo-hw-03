import argparse
import shutil
from pathlib import Path
import sys

# Парсинг командного рядку
def parse_args():
    
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів та сортування за розширенням.")
    
    # Перший аргумент (обов'язковий)
    parser.add_argument("source", type=str, help="Шлях до вихідної папки")
    
    # Другий аргумент (default -> 'dist')
    parser.add_argument("output", nargs="?", default="dist", help="Шлях до папки призначення (default -> dist)")
    
    return parser.parse_args()


# Копіювання файлу у підпапку за розширенням
def copy_file(file_path: Path, output_folder: Path):
    
    try:
        # Зчитування розширення файлу (без розширення -> 'others')
        extension = file_path.suffix[1:] if file_path.suffix else 'others'
        
        # Шлях до цільової папки за розщиренням
        target_dir = output_folder / extension
        
        # Створення папки, якщо не існує
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Формування кінцевого шляху файлу
        destination_file = target_dir / file_path.name
        
        # Копіювання файлу (copy2 зберігає метадані файлу)
        shutil.copy2(file_path, destination_file)
        print(f"OK! Скопійовано: {file_path} -> {destination_file}")
        
    except PermissionError:
        print(f"Warning - Немає прав доступу до файлу: {file_path}")
    except OSError as e:
        print(f"ERROR - Помилка ОС при копіюванні {file_path}: {e}")


# Рекурсивне читання папки та виклик функції копіювання файлів
def read_folder(path: Path, output_folder: Path):

    try:
        for item in path.iterdir():
            if item.is_dir():
                # Рекурсивний виклик для підпапки
                read_folder(item, output_folder)
            elif item.is_file():
                # Обробка файлу
                copy_file(item, output_folder)
                
    except PermissionError:
        print(f"Warning - Немає прав доступу до директорії: {path}")
    except FileNotFoundError:
        print(f"Warning - Директорію не знайдено: {path}")
    except OSError as e:
        print(f"ERROR! Помилка при читанні директорії {path}: {e}")


# Рекурсивнt зчитування папки та виклик функції копіювання файлів
def read_folder(path: Path, output_folder: Path):
    try:
        for item in path.iterdir():
            if item.is_dir():
                # Рекурсивний виклик для підпапки
                read_folder(item, output_folder)
            elif item.is_file():
                # Обробка файлу
                copy_file(item, output_folder)
                
    except PermissionError:
        print(f"[ERROR] Немає прав доступу до директорії: {path}")
    except FileNotFoundError:
        print(f"[ERROR] Директорію не знайдено: {path}")
    except OSError as e:
        print(f"[ERROR] Помилка при читанні директорії {path}: {e}")

if __name__ == "__main__":
    
    # Парсинг аргументів
    args = parse_args()
    
    source_path = Path(args.source)
    output_path = Path(args.output)

    # Перевірка на існування вихідної папки
    if not source_path.exists() or not source_path.is_dir():
        print(f"[CRITICAL] Вихідна директорія '{source_path}' не існує або це не папка.")
        sys.exit(1)

    print(f"Починаємо сортування з '{source_path}' у '{output_path}'...")
    
    # Запуск рекурсивної обробки
    read_folder(source_path, output_path)
    