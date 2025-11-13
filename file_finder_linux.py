import os
import sys

def find_files_by_name(search_term_string, start_path='.', output_file='check.txt'):

    search_terms = [term.strip().lower() for term in search_term_string.split(';')]
    
    search_terms = [term for term in search_terms if term]

    if not search_terms:
        print("Ошибка: Не удалось распознать поисковые термины после разделения.")
        return

    print(f"Поисковые термины: {', '.join(search_terms)}")
    print(f"Начало поиска в директории: {os.path.abspath(start_path)}...")
    
    found_files = []
    
    try:
        for root, dirs, files in os.walk(start_path):
            for file_name in files:
                file_name_lower = file_name.lower()
                
                if any(term in file_name_lower for term in search_terms):
                    full_path = os.path.join(root, file_name)
                    found_files.append(full_path)
                    print(f"Найдено: {full_path}")
    
    except Exception as e:
        print(f"Произошла ошибка при обходе файловой системы: {e}")
        return

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            if found_files:
                f.write('\n'.join(found_files))
                print(f"\n---")
                print(f"✅ Готово! Найдено файлов: {len(found_files)}")
                print(f"Все пути сохранены в файле: **{os.path.abspath(output_file)}**")
            else:
                f.write(f"Файлы, содержащие ни один из терминов ({', '.join(search_terms)}), не найдены.")
                print(f"\n---")
                print(f"⚠️ Файлы не найдены.")
                
    except Exception as e:
        print(f"Ошибка при записи в файл {output_file}: {e}")
        
# ----------------------------------------------------

if __name__ == "__main__":
    
    search_input = input("Введите слова для поиска через разделитель '; ' (например, mine; craft): ").strip()

    if not search_input:
        print("Поисковое слово не может быть пустым. Завершение работы.")
        sys.exit(1)
        
        find_files_by_name(search_input, start_path='/')
