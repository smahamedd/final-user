from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import UserModel
from schemas import UserSchema, UserUpdateSchema, UserDeleteSchema

blp = Blueprint("Users", "users", url_prefix="/users",
                description="Operations on users")


@blp.route("/")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return users

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        name = user_data["name"]
        email = user_data["email"]
        phone_number = user_data["phone_number"]
        added_date = user_data.get("added_date")

        user = UserModel(name=name, email=email,
                         phone_number=phone_number, added_date=added_date)

        db.session.add(user)
        db.session.commit()

        return user

    @blp.response(204)
    def delete(self):
        UserModel.query.delete()
        db.session.commit()
        return ""


@blp.route("/<int:user_id>")
class UserItem(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    @blp.arguments(UserUpdateSchema)
    @blp.response(200, UserSchema)
    def put(self, user_data, user_id):
        user = UserModel.query.get(user_id)

        if user:
            user.name = user_data["name"]
            user.email = user_data["email"]
            user.phone_number = user_data["phone_number"]
            user.added_date = user_data.get("added_date")
        else:
            user = UserModel(id=user_id, **user_data)

        db.session.add(user)
        db.session.commit()

        return user

    @blp.response(204)
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return ""
