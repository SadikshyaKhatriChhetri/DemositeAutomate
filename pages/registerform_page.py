from playwright.sync_api import Page
class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

        # Text fields
        self.firstname = page.get_by_placeholder("First Name")
        self.lastname = page.get_by_placeholder("Last Name")
        self.address = page.locator("textarea")
        self.email = page.locator("input[type='email']")
        self.phone = page.locator("input[type='tel']")

        # Gender
        self.maleradio = page.locator("input[value='Male']")
        self.femaleradio = page.locator("input[value='FeMale']")

        # Hobbies
        self.cricket = page.locator("#checkbox1")

        # Languages
        self.languages = page.locator("#msdd")

        # Skills
        self.skills = page.locator("#Skills")

     # Country
        #self.country_dropdown = page.locator("#select2-country-container")
        #self.country_search = page.locator(".select2-search__field")

        # DOB
        self.year = page.locator("#yearbox")
        self.month = page.locator("select[ng-model='monthbox']")
        self.day = page.locator("select[ng-model='daybox']")

        # Password
        self.password = page.locator("#firstpassword")
        self.confirm_password = page.locator("#secondpassword")

        # Submit
        self.submit = page.locator("#submitbtn")

    def register_user(self, first_name, last_name, address, email, phone, password):
        # Personal Information
        self.firstname.fill(first_name)
        self.lastname.fill(last_name)
        self.address.fill(address)
        self.email.fill(email)
        self.phone.fill(phone)

        # Gender
        self.maleradio.check()

        # Hobbies
        self.cricket.check()

        # Languages
        self.languages.click()
        self.page.locator("//a[text()='English']").click()

        # Skills
        self.skills.select_option(label="Python")
        
         # Country
       #self.country_dropdown.click()
        #self.country_search.fill("India")
        #self.page.locator("//li[text()='India']").click()

        # DOB
        self.year.select_option("1998")
        print(self.month.count())
        self.month.select_option(label="May")
        self.day.select_option("15")

        # Password
        self.password.fill(password)
        self.confirm_password.fill(password)
        
        self.page.wait_for_timeout(5000)

        # Submit
        self.submit.click()
        self.page.wait_for_timeout(5000)
        