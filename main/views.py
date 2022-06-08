from flask import Blueprint, render_template, current_app, request, redirect

from bp_posts.dao.comment_dao import *
from bp_posts.dao.bookmarks_dao import *
from bp_posts.dao.posts_dao import *


main_blueprint = Blueprint('main_blueprint', __name__)              # создание нового блюпринта с заданным именм


@main_blueprint.route('/')                                          # создание вьюшки для главной страницы
def main_page():
    """Вьюшка для главной страницы"""

    try:
        path = current_app.config.get('POST_PATH')                      # путь к файлу
        posts_list = PostsDAO(path)                                     # создание экземпляра класса
        all_posts = posts_list.get_all()                                # получение списка всех постов
        return render_template('index.html', posts=all_posts)           # обращение к шаблону
    except FileNotFoundError:
        return "Нет доступа к данным"


@main_blueprint.route('/search', methods=['GET'])                   # создание вьюшки для страницы поиска
def search_page():
    """Поиск поста"""

    s = request.args.get('s', "")                                   # получение доступа к параметрам адресной строки

    try:
        path = current_app.config.get('POST_PATH')
        posts_list = PostsDAO(path)
        result_posts = posts_list.search_for_posts(s)
        return render_template('search.html', s=s, posts=result_posts)
    except FileNotFoundError:
        return "Нет доступа к данным"


@main_blueprint.route('/user-feed/<username>')
def get_posts_by_user(username):
    """Получение поста по имени"""

    path = current_app.config.get('POST_PATH')
    posts_list = PostsDAO(path)
    result_list = posts_list.get_post_by_user_name(username)

    return render_template('user-feed.html', posts=result_list)


@main_blueprint.route('/post/<int:pk>')
def get_post_by_id(pk):
    """Получение поста по ид"""

    path = current_app.config.get('POST_PATH')
    path_to_comments = current_app.config.get('COMMENTS_PATH')

    posts_list = PostsDAO(path)
    comments_list = Comments(path_to_comments)

    result_posts_list = posts_list.get_post_by_id(pk)
    result_comments_list, comment_count = comments_list.get_comments_by_post_id(pk)
    tags = posts_list.get_content_by_tags(pk)

    return render_template('posts.html', comment_count=comment_count, posts=result_posts_list, comments=result_comments_list, tags=tags)


@main_blueprint.route('/bookmarks/add/<int:pk>')
def add_bookmarks(pk):
    """Добавление и удаление закладок"""

    path = current_app.config.get('POST_PATH')
    bkmrk_path = current_app.config.get('BOOKMARKS_PATH')

    bkmrk_list = Bookmarks(bkmrk_path)
    bkmrk_list.add_or_del_bookmark(path, pk)

    return redirect("/", code=302)                                      # возврат к исходной странице после добавления/удаления


@main_blueprint.route('/bookmarks')
def get_bookmarks():
    """Получение списка закладок"""

    bkmrk_path = current_app.config.get('BOOKMARKS_PATH')
    bkmrk_list = Bookmarks(bkmrk_path)
    result_list = bkmrk_list.get_all()

    return render_template("bookmarks.html", bookmarks=result_list)


@main_blueprint.route('/tag/<tagname>')
def get_post_by_tag(tagname):
    """Вьюшка для перехода по тегам"""

    path = current_app.config.get('POST_PATH')
    post = PostsDAO(path)
    content_by_tag = post.search_tags(tagname)

    return render_template('tag.html', posts=content_by_tag, tagname=tagname)




