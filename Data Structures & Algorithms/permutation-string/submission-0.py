class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}
        l = 0

        # Count characters in s1
        for c in range(len(s1)):
            count1[s1[c]] = 1 + count1.get(s1[c], 0)

        # Sliding window over s2
        for r in range(len(s2)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)

            if r - l + 1 == len(s1):

                # Check current window
                if count1 == count2:
                    return True

                # Remove left character
                count2[s2[l]] -= 1

                if count2[s2[l]] == 0:
                    del count2[s2[l]]

                l += 1

        return False