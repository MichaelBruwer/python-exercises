class Parenthesis_validation:

    def validation_check(self,string1):
        parent,parentletter = [], {"(": ")", "{":"}","[":"]"}
        for brackit in string1:
            if brackit in parentletter:
                parent.append(brackit)
            elif len(parent) == 0 or parentletter[parent.pop()] != brackit:
                return False
        return len(parent) == 0


print(Parenthesis_validation().validation_check("((("))

