from flask import Flask, render_template, request, redirect, url_for

from functions import load_json, save_json, get_new_id

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = load_json("blog_posts.json")
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        blog_posts = load_json("blog_posts.json")
        new_id = get_new_id(blog_posts)
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        print("DEBUG", new_id, author, title, content)
        blog_posts.append(
            {
                "id": new_id,
                "author": author,
                "title": title,
                "content": content
            }
        )
        save_json(blog_posts, "blog_posts.json")
        return redirect(url_for('index'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
