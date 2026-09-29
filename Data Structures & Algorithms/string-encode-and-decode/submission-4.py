class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for s in strs:
            enc_str += str(len(s)) + "#" + s
        return enc_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j=i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            startindx = j + 1
            endindx = startindx + length

            res.append(s[startindx:endindx])

            i = endindx

        return res