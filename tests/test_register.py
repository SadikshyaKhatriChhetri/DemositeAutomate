from pages.register_page import RegisterPage
def test_registerpageload(page):
    register = RegisterPage(page)
    register.open()
    assert "Register" in page.title()