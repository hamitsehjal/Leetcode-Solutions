class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1,count2 = {},{}
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
            count2[s2[i]] = 1 + count2.get(s2[i], 0)

        l = 0
        # if count1 == count2:
        #     return True

        for r in range(len(s1),len(s2)+1):
            if count1 == count2:
                return True
            
            if r < len(s2):

                count2[s2[r]] = 1 + count2.get(s2[r],0)
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                
                l += 1
    
            

        return False



