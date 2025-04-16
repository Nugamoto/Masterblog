import json

DEFAULT_FILEPATH = "blog_posts.json"


def load_json(filepath=DEFAULT_FILEPATH):
    """
    Load blog posts from a JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        list: List of blog post dictionaries.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as fileobject:
            return json.load(fileobject)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json(content, filepath=DEFAULT_FILEPATH):
    """
    Save blog posts to a JSON file.

    Args:
        content (list): List of blog post dictionaries to save.
        filepath (str): Path to the JSON file.

    Raises:
        IOError: If writing to file fails.
        TypeError: If content is not serializable to JSON.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as fileobject:
            json.dump(content, fileobject, indent=4)
    except (IOError, OSError) as e:
        raise IOError(f"Failed to write to file {filepath}") from e
    except TypeError as e:
        raise TypeError("Provided content could not be serialized to JSON") from e


def get_new_id(blog_posts):
    """
    Generate a new unique ID for a blog post.

    Args:
        blog_posts (list): List of existing blog posts.

    Returns:
        int: A new ID one higher than the current maximum.
    """
    if not blog_posts:
        return 1
    max_id = max(blog_post["id"] for blog_post in blog_posts)
    return max_id + 1


def fetch_post_by_id(post_id, posts):
    """
    Retrieve a blog post by its ID.

    Args:
        post_id (int or str): The ID of the post to find.
        posts (list): List of blog post dictionaries.

    Returns:
        dict: The found post, or None if not found.
    """
    for post in posts:
        if str(post["id"]) == str(post_id):
            return post
    return None


def update_blog_post(post_id, author, title, content, posts):
    """
    Update the content of a blog post.

    Args:
        post_id (int or str): ID of the post to update.
        author (str): New author name.
        title (str): New title.
        content (str): New content.
        posts (list): List of blog posts.

    Side effect:
        Saves the updated list to JSON.
    """
    for post in posts:
        if str(post["id"]) == str(post_id):
            post["author"] = author
            post["title"] = title
            post["content"] = content
            break
    save_json(posts)


def add_blog_post(post_id, author, title, content, posts):
    """
    Add a new blog post to the list.

    Args:
        post_id (int): Unique ID for the new post.
        author (str): Author name.
        title (str): Blog post title.
        content (str): Blog post content.
        posts (list): Existing blog posts.

    Side effect:
        Appends new post and saves to JSON.
    """
    posts.append(
        {
            "id": post_id,
            "author": author,
            "title": title,
            "content": content,
            "likes": 0
        }
    )
    save_json(posts)


if __name__ == "__main__":
    pass
