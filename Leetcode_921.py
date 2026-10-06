class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        m_list = list()
        for char in s:
            if char == ')' and len(m_list) != 0 and m_list[-1] == '(':
                m_list.pop()
            else:
                m_list.append(char)
        
        return len(m_list)


test = Solution()
test_str = "()))(("
print(test.minAddToMakeValid(test_str))