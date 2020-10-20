class User_string_to_caps:
    def __init__(self):
        self.string1 = ""

    def user_given(self):
        self.string1 = input()

    def display_string1(self):
        print(self.string1.upper())

    def display_string2(self):
        print(self.string1.lower())

string1 = User_string_to_caps()
string1.user_given()
string1.display_string1()
string1.display_string2()
