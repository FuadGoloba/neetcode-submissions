class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter, s2_counter = {}, {}
        l = 0

        for char in s1:
            s1_counter[char] = s1_counter.get(char, 0) + 1

        for r in range(len(s2)):
            s2_counter[s2[r]] = s2_counter.get(s2[r], 0) + 1

            # Keep the window size within the length of the substring s1
            # Decrement or remove the left most character from s2 counter should the length exceed the window size
            if r - l + 1 > len(s1):
                if s2_counter[s2[l]] == 1:
                    del s2_counter[s2[l]]
                else:
                    s2_counter[s2[l]] -= 1

                l += 1
            
            if s1_counter == s2_counter:
                return True
        return False