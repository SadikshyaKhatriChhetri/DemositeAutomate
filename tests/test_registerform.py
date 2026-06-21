from pages.registerform_page import RegisterPage

def test_valid_registration(page):

    # Arrange
    page.goto("https://demo.automationtesting.in/Register.html")
    register_page = RegisterPage(page)

    # Act
    register_page.register_user(
        first_name="John",
        last_name="Doe",
        address="Kathmandu, Nepal",
        email="john123@example.com",
        phone="9876543210",
        password="Test@123"
    )

    # Assert
    assert not page.locator("text=Success").is_visible()