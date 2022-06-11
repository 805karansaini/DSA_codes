# 2299. Strong Password Checker II
# https://leetcode.com/problems/strong-password-checker-ii/
# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        spcl = "!@#$%^&*()-+"
        sp, up, low, digit, size = 0, 0, 0, 0, 0

        if len(password) >= 8:
            size = 1

        for c in password:
            if c.isupper():
                up = 1
            if c.islower():
                low = 1
            if c.isnumeric():
                digit = 1

        for c in spcl:
            if c in password:
                sp = 1

        if not sp or not up or not low or not digit or not size:
            return False

        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False

        return True