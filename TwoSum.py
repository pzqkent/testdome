class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        dic1 = {}
        for i in range(len(numbers)):
            value = numbers[i]
            target_left = target_sum - value
            if target_left in dic1:
                return (dic1[target_left],i)
            dic1[value] = i
 
                    
                


                
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """
        return None       

print(TwoSum.find_two_sum([3, 1, 5, 7, 5, 9], 10))