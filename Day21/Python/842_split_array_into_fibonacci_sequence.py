class Solution(object):
    def splitIntoFibonacci(self, num):
        result = []

        def backtrack(index):
            if index == len(num) and len(result) >= 3:
                return True

            curr = 0
            for i in range(index, len(num)):
                # no leading zero
                if num[index] == '0' and i > index:
                    break

                curr = curr * 10 + int(num[i])
                if curr > 2**31 - 1:
                    break

                if len(result) >= 2:
                    expected = result[-1] + result[-2]
                    if curr < expected:
                        continue
                    if curr > expected:
                        break

                result.append(curr)
                if backtrack(i + 1):
                    return True
                result.pop()

            return False

        backtrack(0)
        return result

        
