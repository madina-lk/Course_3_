import logging

from flask import Blueprint, current_app, jsonify  # импорт класса блюпринт

from bp_posts.dao.posts_dao import *

posts_blueprint = Blueprint('posts_blueprint', __name__)
logging.basicConfig(filename='./logs/api.log', level=logging.INFO, format=" %(asctime)s - %(levelname)s - %(message)s")                # добавление файла, в который пишутся логи


@posts_blueprint.route('/api/posts')
def page_posts():
    """Вьюшка для представления просмотра постов в формате json"""
    try:
        path = current_app.config.get('POST_PATH')
        posts = PostsDAO(path)
        all_posts = posts.get_all()
        return jsonify(all_posts)
    except FileNotFoundError:                                       # обработка ошибки
        logging.error("Нет доступа к данным")                       # запись в лог
        return "Нет доступа к данным"


@posts_blueprint.route('/api/posts/<int:pk>')
def page_posts_by_pk(pk):
    """Вьюшка для представления просмотра поста по ид"""
    try:
        path = current_app.config.get('POST_PATH')
        posts_list = PostsDAO(path)
        result_posts_list = posts_list.get_post_by_id(pk)
        return jsonify(result_posts_list)
    except FileNotFoundError:                                       # обработка ошибки
        logging.error("Нет доступа к данным")                       # запись в лог
        return "Нет доступа к данным"
