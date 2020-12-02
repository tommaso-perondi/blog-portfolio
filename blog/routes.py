from flask import Blueprint, render_template, redirect, url_for, Response
from flask_login import current_user, login_required, logout_user
from .models import Post
from .forms import PostCreate
from . import db
main_bp = Blueprint(
    "main_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@main_bp.route("/admin", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""

    return render_template(
        "dashboard.html",
        title="Admin Dashboard",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
        posts = Post.query.order_by(Post.time_created.desc()).all()
    )

@main_bp.route("/posts/create", methods=["GET", "POST"])
@login_required
def create_post():

    form = PostCreate()

    if form.validate_on_submit():
        db.session.add(Post(title=form.title.data, content=form.content.data))
        db.session.commit()
        
    return render_template(
        "post_create.html",
        form=form,
        title="Create post.",
    )


@main_bp.route("/posts/<post_id>/delete")
@login_required
def delete_post(post_id):
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return Response(status=200)


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))


@main_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@main_bp.route("/blog", methods=["GET"])
def blog():
    return render_template("blog.html", posts=Post.query.order_by(Post.time_created.desc()).all())


@main_bp.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
