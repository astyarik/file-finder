import os
import sys

def find_files_by_name(search_term, start_path='.', output_file='check.txt'):
    """
    Рекурсивно ищет файлы, содержащие заданное слово в названии, 
    начиная с указанного пути, и записывает их полные пути в текстовый файл.

    :param search_term: Слово или часть слова для поиска в названиях файлов.
    :param start_path: Путь, с которого начать поиск (по умолчанию - текущая директория).
    :param output_file: Имя файла, в который будут записаны результаты.
    """
    
    # Преобразуем поисковый запрос в нижний регистр для регистронезависимого поиска
    search_term = search_term.lower()
    found_files = []
    
    # 1. Обход директорий с помощью os.walk()
    print(f"Начало поиска '{search_term}' в директории: {os.path.abspath(start_path)}...")
    
    try:
        # os.walk() генерирует кортежи (root, dirs, files) для каждого каталога в дереве
        for root, dirs, files in os.walk(start_path):
            for file_name in files:
                # 2. Проверка, содержит ли имя файла искомое слово
                if search_term in file_name.lower():
                    # 3. Формирование полного пути
                    full_path = os.path.join(root, file_name)
                    found_files.append(full_path)
                    print(f"Найдено: {full_path}")
    
    except Exception as e:
        print(f"Произошла ошибка при обходе файловой системы: {e}")
        return

    # 4. Запись результатов в файл check.txt
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            if found_files:
                f.write('\n'.join(found_files))
                print(f"\n---")
                print(f"✅ Готово! Найдено файлов: {len(found_files)}")
                print(f"Все пути сохранены в файле: **{os.path.abspath(output_file)}**")
            else:
                f.write(f"Файлы, содержащие '{search_term}', не найдены.")
                print(f"\n---")
                print(f"⚠️ Файлы, содержащие '{search_term}', не найдены.")
                
    except Exception as e:
        print(f"Ошибка при записи в файл {output_file}: {e}")
        
# ----------------------------------------------------

if __name__ == "__main__":
    
    # Запрос слова для поиска у пользователя
    search_word = input("Введите слово (или часть слова) для поиска в названиях файлов (например, mine): ").strip()

    if not search_word:
        print("Поисковое слово не может быть пустым. Завершение работы.")
        sys.exit(1)
        
    # Вызов основной функции
    # Вы можете изменить '.' на конкретный путь, например 'C:\\' или '/home/user'
    find_files_by_name(search_word, start_path='C:\\')
