from flask import Blueprint, render_template, redirect, url_for, Response, request, session
from flask_login import current_user, login_required, logout_user
import json
from blog.models import Post
from blog.forms import PostCreate, PostEdit
from blog import db

main = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@main.route("/posts/create", methods=["GET", "POST"])
@login_required
def create_post():

    form = PostCreate()
    user = current_user
    if form.validate_on_submit():
        db.session.add(
            Post(
                title=form.title.data,
                content=form.content.data,
                author_id=user.id))
        db.session.commit()
        return redirect(url_for('main.blog'))

    return render_template(
        "post_create.html",
        form=form,
        title="Create post.",
    )

@main.route("/posts/<post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id):

    post=Post.query.filter_by(
            id=post_id).first_or_404()
    form = PostEdit(obj=post)
    user = current_user
    if form.validate_on_submit():
        db.session.query(Post).filter_by(id=post_id).update({"title" : form.title.data, "content" : form.content.data, "author_id" : user.id})
        db.session.commit()
        return redirect(url_for('main.blog'))

    return render_template(
        "post_edit.html",
        form=form,
        title="Edit post.",
    )



@main.route("/posts/<post_id>/delete")
@login_required
def delete_post(post_id):
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return Response(status=200)


@main.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@main.route("/blog", methods=["GET"])
def blog():
    return render_template(
        "blog.html", posts=Post.query.order_by(
            Post.time_created.desc()).all())


@main.route("/posts/<post_id>")
def view_post(post_id):
    return render_template(
        "post.html", post=Post.query.filter_by(
            id=post_id).first_or_404())


@main.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


def loggedUser():
    user = None
    cookie = request.cookies.get('user_id')
    if cookie:
        cookie_value = check_secure_val(cookie)
        if cookie_value:
            user = models.User.query.filter_by(id=cookie_value).one()
    return user


@main.route("/admin", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""

    return render_template(
        "dashboard.html",
        title="Admin Dashboard",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
        posts=Post.query.order_by(Post.time_created.desc()).all()
    )
