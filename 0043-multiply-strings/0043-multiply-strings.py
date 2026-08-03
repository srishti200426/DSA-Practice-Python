class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (num1 == "0" or num2 == "0"):
            return "0"
        n = len(num1)
        m = len(num2)
        result = [0]*(m+n)

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                mul = int(num1[i]) * int(num2[j])

                p1 = i+ j
                p2 = i + j + 1

                total = mul + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        answer = []

        for digit in result:
            if not(digit == 0 and len(answer) == 0):
                answer.append(str(digit))

        return "".join(answer)

         
        