from flask import Flask, render_template, request
blog = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates/')

@blog.route('/')
def home():
    return render_template('index.html')

@blog.route('/blog')
def blogpage():
    return render_template('blog.html')

@blog.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    blog.run(debug = True)