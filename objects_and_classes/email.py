class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send_email(self):
        self.is_sent = True

    def sent_email(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()
emails_list = []

while command != "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails_list.append(email)
    command = input()

indices = [int(x) for x in input().split(", ")]

for index in indices:
    email = emails_list[index]
    email.send_email()

for email in emails_list:
    print(email.sent_email())
