import json


class Comments:
    """Класс Comments содержит:
       Поля:
        - path                                          - путь к загружаемому файлу

       Методы:
        - get_all_comments                              - возвращает весь список словарей
        - get_comments_by_post_id                       - возвращает комментарии определенного поста
    """

    def __init__(self, path):
        """Конструктор"""

        self.path = path

    def load_data(self):
        """Загрузка данных из файла"""

        with open(self.path, 'r', encoding='utf-8') as file:        # открытие json - файла
            data = json.load(file)                                  # загрузка списка словарей из json - файла

        return data

    def get_all_comments(self):
        """Возвращает весь список словарей"""

        data = self.load_data()  # получение списка словарей
        return data

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста"""

        comments = self.get_all_comments()
        comments_by_post_id = []
        comment_count = 0

        for comment in comments:
            if post_id == comment['post_id']:
                comment_count += 1
                comments_by_post_id.append(comment)

        return comments_by_post_id, comment_count

