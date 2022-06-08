import json

from exception.data_exception import DataSourceError


class PostsDAO:
    """Класс Posts содержит:
       Поля:
        - path                                                      - путь к загружаемому файлу

       Методы:
        - get_post_by_user_name                                     - возвращает посты определенного пользователя
        - get_post_by_id                                            - возвращает пост по pk
        - search_for_posts                                          - возвращает список постов по ключевому слову
        - get_all                                                   - возвращает весь список словарей
    """

    def __init__(self, path):
        """Конструктор"""

        self.path = path

    def load_data(self):
        """Загрузка данных из файла"""

        try:
            with open(self.path, 'r', encoding='utf-8') as file:  # открытие json - файла
                data = json.load(file)  # загрузка списка словарей из json - файла
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataSourceError('Не удалось получить данные из файла')
        else:
            return data

    def get_all(self):
        """Возвращает весь список словарей"""
        data = self.load_data()                                     # получение списка словарей
        return data

    def get_post_by_user_name(self, username):
        """Возвращает посты определенного пользователя"""

        if type(username) != str:
            raise TypeError("Неверный тип")

        posts = self.get_all()
        posts_by_name = []                                          # список для хранения найденных постов

        for post in posts:                                          # перебор элементов списка словаря
            if username in post['poster_name']:                     # условие вхождения а poster_name
                posts_by_name.append(post)                          # добавление найденного поста в список posts_by_name

        return posts_by_name

    def get_post_by_id(self, pk):
        """Возвращает пост по pk"""

        if type(pk) != int:
            raise TypeError("Неверный тип")

        posts = self.get_all()
        post_by_pk = []                                             # список для хранения словаря

        for post in posts:                                          # перебор элементов списка словаря
            if pk == post['pk']:                                    # условие проверки id
                post_by_pk.append(post)

        return post_by_pk

    def search_for_posts(self, query):
        """Возвращает список постов по ключевому слову"""

        if type(query) != str:
            raise TypeError("Неверный тип")

        posts = self.get_all()
        result_search = []                                          # список для хранения постов

        for post in posts:                                          # перебор элементов списка словаря
            if query in post['content']:                            # условие проверки id
                result_search.append(post)                          # добавление найденного поста в список result_search

        return result_search

    def add_bookmark(self, bookmrk_path, pk):
        """Добавление закладок"""
        posts = self.get_all()
        bookmarks = []

        for post in posts:
            if pk == post['pk']:
                bookmarks.append(post)

        with open(bookmrk_path, 'w', encoding='utf-8') as f:
            json.dump(bookmarks, f, ensure_ascii=False, indent=4)  # перезапись файла

        return bookmarks

    def get_content(self, pk):
        """Получение содержимого поля 'content'"""
        posts = self.get_all()
        content = ''

        for post in posts:  # перебор элементов списка словаря
            if pk == post['pk']:
                content = post['content']

        return content.split()

    def get_content_by_tags(self, pk):
        """замена тегов ссылками"""
        post = self.get_all()
        word_without_tag = ""

        content_list = self.get_content(pk)
        # re_content = (regex.sub(r'[^\P{P}#]+', '', content_list)).split()

        for index in range(len(content_list)):
            word = content_list[index]
            if word.startswith('#'):
                word_without_tag = word.replace('#', '')
                content_list[index] = f'<a href="/tag/{word_without_tag}">{word}</a>'

        return ' '.join(content_list)

    def search_tags(self, tag):
        """поиск по тегам"""
        posts = self.get_all()
        content_by_tag = []
        search_tag = f'#{tag}'

        for post in posts:  # перебор элементов списка словаря
            if search_tag in post['content']:
                content_by_tag.append(post)

        return content_by_tag

