giclass User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class JournalEntry:
    def __init__(self, text, date, category, tags=None):
        self.text = text
        self.date = date
        self.category = category
        self.tags = tags if tags else []


class Tag:
    def __init__(self, name):
        self.name = name


class Journal:
    def __init__(self):
        self.entries = []

    def create_entry(self, text, date, category, tags=None):
        entry = JournalEntry(text, date, category, tags)
        self.entries.append(entry)

    def edit_entry(self, index, text, date, category, tags=None):
        if 0 <= index < len(self.entries):
            entry = self.entries[index]
            entry.text = text
            entry.date = date
            entry.category = category
            entry.tags = tags if tags else []
        else:
            print("Невірний запис.")

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
        else:
            print("Невірний запис.")

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

    def validate_entry(self, text):
        if not text:
            print("Текст не може бути порожнім.")
            return False
        return True

    def validate_unique_categories(self):
        categories = set()
        for entry in self.entries:
            category = entry.category
            if category in categories:
                print("Категорія '{}' не унікальна.".format(category))
                return False
            categories.add(category)
        return True
