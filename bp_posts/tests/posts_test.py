from bp_posts.dao.posts_dao import PostsDAO

path = '../../data/data.json'
bookmrk_path = '../../data/bookmarks.json'

post = PostsDAO(path)


class TestPosts:

    def test_get_all(self):
        """ Проверяем, верный ли список кандидатов возвращается """

        posts_result = post.get_all()
        assert type(posts_result) == list, "возвращается не список"
        assert len(posts_result) > 0, "возвращается пустой список"

    def test_get_post_by_user_name(self):
        """Тест для отображения поста по имени"""

        result_posts = post.get_post_by_user_name('larry')
        assert len(result_posts) == 2, "Неверное количество постов пользователя"

    def test_get_post_by_id(self):
        """Тест для отображения поста по ид"""

        result_posts = post.get_post_by_id(1)
        assert (result_posts["pk"] == 1), "возвращается неправильный пост"
        assert len(result_posts) == 1, "Несоответствие поста индексу"

    def test_search_for_posts(self):
        """Тест для поиска по постам"""

        result_posts = post.search_for_posts('бабушка')
        assert len(result_posts) == 1, "Неверно найденное количество постов"

    def test_search_tags(self):
        """Тест для поиска по тегам"""

        result_posts = post.search_tags('food')
        assert len(result_posts) == 1, "Неверно найденное количество постов по тегу"

    def test_add_bookmark(self):
        """Тест для добавления закладок в список"""

        result_posts = post.add_bookmark(bookmrk_path, 1)
        assert len(result_posts) == 1, "Пост добавлен"
