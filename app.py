from flask import Flask, render_template, request, redirect, url_for

from functions import load_json, save_json, get_new_id, fetch_post_by_id, add_blog_post, update_blog_post

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

        add_blog_post(new_id, author, title, content, blog_posts)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<post_id>')
def delete(post_id):
    blog_posts = load_json("blog_posts.json")

    post = fetch_post_by_id(post_id, blog_posts)

    blog_posts.remove(post)

    save_json(blog_posts, "blog_posts.json")

    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    posts = load_json("blog_posts.json")
    post = fetch_post_by_id(post_id, posts)

    if not post:
        return "Post not found", 404

    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        update_blog_post(post_id, author, title, content, posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
