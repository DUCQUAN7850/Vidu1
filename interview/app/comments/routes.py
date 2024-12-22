from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Comment
from app.schemas import CommentSchema

comments_bp = Blueprint("comments", __name__)
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


@comments_bp.route("/", methods=["POST"])
def add_comment():
    data = request.get_json()
    errors = comment_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    new_comment = Comment(**data)
    db.session.add(new_comment)
    db.session.commit()

    return comment_schema.dump(new_comment), 201


@comments_bp.route("/", methods=["GET"])
def get_comments():
    root_comments = Comment.query.filter_by(parent_id=None).all()
    return comments_schema.dump(root_comments), 200
