# Decode XORed Array:
class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        decode = [first]
        for i in range(len(encoded)):
            a=(encoded[i]^decode[-1])
            decode.append(a)
        return decode