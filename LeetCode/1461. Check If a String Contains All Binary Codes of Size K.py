#https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
#1461. Check If a String Contains All Binary Codes of Size K
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11".
# They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
#
# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.

#MAKE A SET TO STORE ALL THE DIFFERENT STRINGS CHECK THE SUM == 2**K (2^K)
def hasAllCodes(self, s: str, k: int) -> bool:
    my_set = set()
    for i in range(len(s) - k + 1):
        w = i + k
        my_set.add(s[i:w])
    num = 2 ** k
    if len(my_set) == num:
        return True
    return False