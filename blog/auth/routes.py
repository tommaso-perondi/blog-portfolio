from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from .forms import LoginForm
from .models import User
from auth import login_manager, main
import sys

auth = Blueprint(
    "auth", __name__, template_folder="templates", static_folder="static"
)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password_hash(form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("auth.dashboard"))
        flash("Invalid username/password combination")
        return redirect(url_for("auth.login"))
    return render_template(
        "login.html",
        form=form,
        title="Log in.",
        template="login-page",
        body="Log in with your User account.",
    )


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth.login"))
