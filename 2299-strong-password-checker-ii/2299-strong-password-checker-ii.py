class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        lower_case = False
        upper_case = False
        one_digit = False
        special_char = False

        i = 0
        prev = None
        while i < len(password):
            if prev == password[i]:
                return False
            if password[i].isalpha():
                if password[i] == password[i].lower():
                    lower_case = True
                else:
                    upper_case = True
            if password[i].isdigit():
                one_digit = True
            else:
                if not special_char:
                    if password[i] in '!@#$%^&*()-+':
                        special_char = True
            prev = password[i]
            i += 1

        return special_char and one_digit and lower_case and upper_case