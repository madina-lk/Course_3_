from bp_posts.dao.comment_dao import Comments

comments_path = '../../data/comments.json'


class TestComment:

    def test_get_comments_by_post_id(self):
        """Тест для отображения комментариев к посту по ид поста"""
        comments = Comments(comments_path)
        result, com_count = comments.get_comments_by_post_id(1)
        assert com_count == 4, "Неверное количество комментариев"

