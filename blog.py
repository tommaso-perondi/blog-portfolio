from flask import Flask, render_template, request
blog = Flask(__name__)

@blog.route('/')
def home():
    return render_template('index.html')