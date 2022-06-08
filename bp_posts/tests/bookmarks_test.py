from bp_posts.dao.bookmarks_dao import Bookmarks

bookmark_path = '../../data/bookmarks.json'
path = '../../data/data.json'


class TestBookmarks:

    def test_add_or_del_bookmark(self):
        """Тест для метода добавления и удаления закладок"""
        bookmark = Bookmarks(bookmark_path)
        result = bookmark.add_or_del_bookmark(path, 2)
        assert len(result) == 1, 'Пост удален из закладок'
        assert len(result) == 0, 'Пост добавлен'

