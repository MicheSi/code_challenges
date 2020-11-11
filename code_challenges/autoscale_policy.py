class Solution: 
    
    def finalInstances(self, instances, averageUtil):
        
        ptr = 0
        
        while (ptr < len(averageUtil)):

            if (averageUtil[ptr] > 60):
                doubled = instances * 2
                if (doubled <= 2 * pow(10, 8)):
                    instances = doubled
                    ptr += 11
                    continue
                else:
                    ptr += 1
                    continue 
            elif (averageUtil[ptr] < 25):
                if (instances > 1):
                    instances = math.ceil(instances / 2)
                    ptr += 11
                    continue
                else:
                    ptr += 1
                    continue
            ptr += 1
                    
        return instances
    
    
s = Solution()
averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
print(s.finalInstances(2, averageUtil))