class Comment:
    def __init__(self, username: str, content: str, likes: int = 0):
        self.username = username
        self.content = content
        self.likes = likes

    def full_comment(self):
        return f"{self.username} {self.content} {self.likes}"


comment = Comment("Gosho", "Ese", 6)
comment_1 = Comment("Pesho", "Cena")
comment.likes += 1

print(comment.full_comment())
print(comment_1.__dict__)
