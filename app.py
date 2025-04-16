from flask import Flask, render_template, request, redirect, url_for

from functions import load_json, save_json, get_new_id, fetch_post_by_id, add_blog_post, update_blog_post

app = Flask(__name__)


@app.route('/')
def index():
    """
    Display the homepage with all blog posts.

    Returns:
        Rendered index.html template with blog post data.
    """
    blog_posts = load_json("blog_posts.json")
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handle creation of a new blog post.

    Returns:
        On GET: Rendered add.html template.
        On POST: Redirect to homepage after saving new post.
    """
    if request.method == 'POST':
        author = request.form.get("author", "").strip()
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if not author or not title or not content:
            error = "All fields must be filled."
            return render_template('add.html', error=error)

        blog_posts = load_json("blog_posts.json")
        new_id = get_new_id(blog_posts)
        add_blog_post(new_id, author, title, content, blog_posts)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<post_id>', methods=['POST'])
def delete(post_id):
    """
    Delete a blog post by ID.

    Args:
        post_id (str): ID of the post to delete.

    Returns:
        Redirect to homepage after deletion.
    """
    blog_posts = load_json("blog_posts.json")
    post = fetch_post_by_id(post_id, blog_posts)
    if post:
        blog_posts.remove(post)
        save_json(blog_posts, "blog_posts.json")
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Update an existing blog post.

    Args:
        post_id (int): ID of the post to update.

    Returns:
        On GET: Rendered update.html template with pre-filled post.
        On POST: Redirect to homepage after saving updated post.
    """
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


@app.route('/like/<int:post_id>')
def like(post_id):
    """
    Increment the like counter for a blog post.

    Args:
        post_id (int): ID of the post to like.

    Returns:
        Redirect to homepage after updating likes.
    """
    blog_posts = load_json("blog_posts.json")

    for post in blog_posts:
        if str(post["id"]) == str(post_id):
            post["likes"] = post.get("likes", 0) + 1
            break

    save_json(blog_posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
