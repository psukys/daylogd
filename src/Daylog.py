class Daylog:

    def __init__(self):
        self.date = ''
        self.posts = []  # should consist of Post objects


class Post:

    def __init__(self):
        self.title = ''  # name of the post
        self.mark = ''  # marking of the post, how good/bad was it
        self.content = ''  # short description of it went
