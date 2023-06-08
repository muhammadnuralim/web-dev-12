from flask import Blueprint

bp = Blueprint('posts', __name__)

from app.user import routes