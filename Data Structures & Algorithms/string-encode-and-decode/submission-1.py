class Solution:

    def encode(self, strs: List[str]) -> str:
        #encoding algo should perform an operation where it transforms the given 
        #list of strs into one string while maintaing the individual 
        #position information so that it can be used by the decoder to decode the encoded str back to the same list of strs.
        #to get separate words, use a delimiter. But it can be in the original string as well.
        #to verify encode the len of the str along with the delimiter to know while decoding
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string
    def decode(self, s: str) -> List[str]:
        #
        decoded_string, i  = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_string.append(s[j+1: j+1 + length])
            i = j+1 +length
        return decoded_string