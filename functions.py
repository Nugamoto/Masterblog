import json

BLOG_POSTS = [
    {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
    {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'},
    {'id': 3, 'author': 'Alice Smith', 'title': 'Tech Trends 2025',
     'content': 'Exploring the upcoming trends in AI and machine learning for 2025.'},
    {'id': 4, 'author': 'Bob Johnson', 'title': 'Travel Diary: Japan',
     'content': 'Highlights from my trip to Kyoto and Tokyo, including local food and temples.'},
    {'id': 5, 'author': 'Clara Rose', 'title': 'Healthy Living Tips',
     'content': '5 simple habits that helped me improve my physical and mental health.'},
    {'id': 6, 'author': 'Dave Lee', 'title': 'Book Review: The Silent Patient',
     'content': 'A deep dive into one of the most gripping psychological thrillers I\'ve read.'},
    {'id': 7, 'author': 'Ella Martinez', 'title': 'Photography 101',
     'content': 'A beginner\'s guide to mastering the art of photography with any camera.'},
    {'id': 8, 'author': 'Frank Yang', 'title': 'Why I Switched to Linux',
     'content': 'My journey from Windows to Linux and the pros and cons I discovered.'},
    {'id': 9, 'author': 'Grace Kim', 'title': 'Morning Routines That Work',
     'content': 'Structuring your mornings for better productivity and peace of mind.'},
    {'id': 10, 'author': 'Henry Clark', 'title': 'The Rise of Indie Games',
     'content': 'How small studios are revolutionizing the gaming industry with passion projects.'}
]


def load_json(filepath="storage.json"):
    try:
        with open(filepath, "r") as fileobject:
            return json.load(fileobject)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json(content, filepath="storage.json"):
    with open(filepath, "w") as fileobject:
        fileobject.write(json.dumps(content))


def get_new_id(blog_posts):
    if not blog_posts:
        return 1
    max_id = max(blog_post["id"] for blog_post in blog_posts)
    return max_id + 1
