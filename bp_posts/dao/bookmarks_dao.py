from bp_posts.dao.posts_dao import *


class Bookmarks:
    """Класс Posts содержит:

       Поля:
        - path

       Методы:
        - load_data
        - get_all
        - dump_to_json
        - add_or_del_bookmark

    """

    def __init__(self, path):
        """Конструктор"""

        self.path = path

    def load_data(self):
        """Загрузка данных из файла"""

        try:
            with open(self.path, 'r', encoding='utf-8') as file:        # открытие json - файла
                data = json.load(file)                                  # загрузка списка словарей из json - файла
        except (FileNotFoundError, json.JSONDecodeError):
            return "Файл поврежден!"
        else:
            return data

    def get_all(self):
        """Возвращает весь список словарей"""
        data = self.load_data()                                     # получение списка словарей
        return data

    def dump_to_json(self, file_path, result_list):
        """Запись в json файл"""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(result_list, f, ensure_ascii=False, indent=4)  # перезапись файла

    def add_or_del_bookmark(self, post_path, pk):
        """Добавление и удаление закладок"""

        all_posts = PostsDAO(post_path)
        posts = all_posts.get_all()

        bookmarks = self.get_all()

        is_post_exist = False                                       # заглушка для проверки

        for el in range(len(bookmarks) - 1, -1, -1):
            if bookmarks[el]['pk'] == pk:
                bookmarks.pop(el)
                is_post_exist = True

        if not is_post_exist:
            for post in posts:
                if pk == post['pk']:
                    bookmarks.append(post)

        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(bookmarks, f, ensure_ascii=False, indent=4)  # перезапись файла

        return bookmarks





