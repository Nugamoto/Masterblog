import json

DEFAULT_FILEPATH = "blog_posts.json"


def load_json(filepath=DEFAULT_FILEPATH):
    try:
        with open(filepath, "r") as fileobject:
            return json.load(fileobject)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json(content, filepath=DEFAULT_FILEPATH):
    with open(filepath, "w") as fileobject:
        fileobject.write(json.dumps(content, indent=4))


def get_new_id(blog_posts):
    if not blog_posts:
        return 1
    max_id = max(blog_post["id"] for blog_post in blog_posts)
    return max_id + 1


def fetch_post_by_id(post_id, posts):
    for post in posts:
        if str(post["id"]) == str(post_id):
            return post
    return {}


def update_blog_post(post_id, author, title, content, posts):
    for post in posts:
        if str(post["id"]) == str(post_id):
            post["author"] = author
            post["title"] = title
            post["content"] = content
            break
    save_json(posts, "blog_posts.json")


def add_blog_post(post_id, author, title, content, posts):
    posts.append(
        {
            "id": post_id,
            "author": author,
            "title": title,
            "content": content
        })
    save_json(posts, "blog_posts.json")


if __name__ == "__main__":
    pass
