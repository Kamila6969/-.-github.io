class JournalEntry:
    def __init__(self, text, date, category, tags=None):
        self.text = text
        self.date = date
        self.category = category
        self.tags = tags if tags else []


class Journal:
    def __init__(self):
        self.entries = []

    def create_entry(self, text, date, category, tags=None):
        if not text:
            print("Текст не може бути порожнім.")
            return
        if tags is None:
            tags = []
        entry = JournalEntry(text, date, category, tags)
        self.entries.append(entry)
        print("Запис успішно створено.")

    def edit_entry(self, index, text, date, category, tags=None):
        if 0 <= index < len(self.entries):
            entry = self.entries[index]
            entry.text = text
            entry.date = date
            entry.category = category
            entry.tags = tags if tags else []
            print("Запис успішно відредаговано.")
        else:
            print("Невірний індекс.")

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
            print("Запис успішно видалено.")
        else:
            print("Невірний індекс.")

    def organize_entries_by_category(self):
        organized_entries = {}
        for entry in self.entries:
            category = entry.category
            if category not in organized_entries:
                organized_entries[category] = []
            organized_entries[category].append(entry)
        return organized_entries

    def search_entries_by_tag(self, tag):
        matching_entries = []
        for entry in self.entries:
            if tag in entry.tags:
                matching_entries.append(entry)
        return matching_entries


def main(journal):
    while True:
        print("\n1. Створити новий запис")
        print("2. Редагувати запис")
        print("3. Видалити запис")
        print("4. Організувати записи за категоріями")
        print("5. Пошук записів за тегами")
        print("6. Вийти")
        choice = input("Виберіть дію: ")
        if choice == "1":
            text = input("Введіть текст запису: ")
            date = input("Введіть дату запису (формат: YYYY-MM-DD): ")
            category = input("Введіть категорію: ")
            tags = input("Введіть теги (розділені комами): ").split(",")
            journal.create_entry(text, date, category, tags)
        elif choice == "2":
            index = int(input("Введіть індекс запису для редагування: "))
            text = input("Введіть новий текст запису: ")
            date = input("Введіть нову дату запису (формат: YYYY-MM-DD): ")
            category = input("Введіть нову категорію: ")
            tags = input("Введіть нові теги (розділені комами): ").split(",")
            journal.edit_entry(index, text, date, category, tags)
        elif choice == "3":
            index = int(input("Введіть індекс запису для видалення: "))
            journal.delete_entry(index)
        elif choice == "4":
            organized_entries = journal.organize_entries_by_category()
            for category, entries in organized_entries.items():
                print(f"\nКатегорія: {category}")
                for entry in entries:
                    print(f"Текст: {entry.text}, Дата: {entry.date}, Теги: {', '.join(entry.tags)}")
        elif choice == "5":
            tag = input("Введіть тег для пошуку: ")
            matching_entries = journal.search_entries_by_tag(tag)
            for entry in matching_entries:
                print(f"Текст: {entry.text}, Дата: {entry.date}, Категорія: {entry.category}, Теги: {', '.join(entry.tags)}")
        elif choice == "6":
            break
        else:
            print("Невірний вибір. Спробуйте знову.")


if __name__ == "__main__":
    journal = Journal()
    main(journal)
