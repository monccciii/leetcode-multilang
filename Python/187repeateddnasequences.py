# How it works:
# initialize candidates and output as sets (for optimization)
# run a for statement with is 9 characters shorter than the length
# of the sequence to avoid index errors
# create ten which is the current index + index + 10
# add it to candidates if it isn't there, if it is
# add it to output. once complete return output

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        candidates = set()
        output = set()
        for i in range(len(s) - 9):
            ten = s[i:i+10]
            if ten in candidates:
                if ten not in output:
                    output.add(ten)
            else:
                candidates.add(ten)
        return output