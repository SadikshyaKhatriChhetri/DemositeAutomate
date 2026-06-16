class RegisterPage:
    def __init__(self, page):
        self.page = page
    def open(self):
        self.page.goto("https://demo.automationtesting.in/Register.html")