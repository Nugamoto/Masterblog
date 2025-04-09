import json

BITCOIN_BLOG_POSTS = [
    {
        "id": 1,
        "author": "Max Huber",
        "title": "Bitcoin Explained Like You're 5",
        "content": "A simple explanation of how Bitcoin works, from blocks to wallets."
    },
    {
        "id": 2,
        "author": "Laura Neumann",
        "title": "Why Bitcoin Is Not Just Digital Money",
        "content": "A look into Bitcoin as a protocol for decentralized trust, not just currency."
    },
    {
        "id": 3,
        "author": "Felix Braun",
        "title": "Understanding the Bitcoin Halving",
        "content": "What is the halving event and why does it matter for Bitcoin's monetary policy?"
    },
    {
        "id": 4,
        "author": "Nora Vogel",
        "title": "What Makes Bitcoin Truly Decentralized?",
        "content": "Exploring node culture, governance, and how consensus actually works."
    },
    {
        "id": 5,
        "author": "Samuel Becker",
        "title": "The Lightning Network: Scaling Bitcoin",
        "content": "How Lightning enables fast, cheap transactions on top of Bitcoin."
    },
    {
        "id": 6,
        "author": "Anna Roth",
        "title": "Running a Bitcoin Full Node at Home",
        "content": "Why and how you should run your own node to support the network."
    },
    {
        "id": 7,
        "author": "Tobias Zimmer",
        "title": "Bitcoin Mining: Beyond the Buzzwords",
        "content": "What miners actually do, how blocks are built, and why proof-of-work matters."
    },
    {
        "id": 8,
        "author": "Helena Schröder",
        "title": "Privacy in Bitcoin: What You Need to Know",
        "content": "Bitcoin isn't anonymous. Learn how to protect your privacy as a user."
    },
    {
        "id": 9,
        "author": "Lars König",
        "title": "Bitcoin vs Central Banks",
        "content": "A deep dive into how Bitcoin contrasts with traditional monetary systems."
    },
    {
        "id": 10,
        "author": "Mira Weber",
        "title": "Bitcoin in 2025: Where Are We Headed?",
        "content": "Predictions, developments, and open questions about the future of Bitcoin."
    }
]
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
        # save_json(BITCOIN_BLOG_POSTS, "blog_posts.json")
        pass
