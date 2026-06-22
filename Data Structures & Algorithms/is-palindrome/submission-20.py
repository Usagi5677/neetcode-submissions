class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s.lower() if c.isalnum())


        k = 0
        l = len(s)-1

        while k<l:
            if s[k] != s[l]:
                return False
            k += 1
            l -=1
        return True

    
    
    
  


    


    
    