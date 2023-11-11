title = input()
content = input()
comment = input()


def formatting(tag, text):
    print(f"<{tag}>\n"
          f"    {text}\n"
          f"</{tag}>")


formatting("h1", title)
formatting("article", content)

while comment != "end of comments":
    formatting("div", comment)
    comment = input()
