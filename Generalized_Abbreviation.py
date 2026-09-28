class Solution:
    def generateAbbreviations(self, word):
        result = []

        def backtrack(index, current, count):
            if index == len(word):
                if count > 0:
                    current += str(count)
                result.append(current)
                return

            backtrack(index + 1, current, count + 1)

            if count > 0:
                current += str(count)

            backtrack(index + 1, current + word[index], 0)

        backtrack(0, "", 0)

        return result
