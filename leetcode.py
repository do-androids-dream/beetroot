# def rotate(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: None Do not return anything, modify nums in-place instead.
#     """
#     r_list = nums[-k:] + nums[:k+1]
#     return r_list
#
#
# print(rotate([1, 2, 3, 4, 5, 6, 7], 3))


# def removeDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     i = 1
#     count = 1
#     while i <= len(nums) - 1:
#         print(nums, "i=", i, nums[i], "count=", count)
#         if nums[i - 1] == nums[i]:
#             count += 1
#         else:
#             count = 1
#         if count > 2:
#             nums.remove(nums[i])
#             i -= 1
#             count -= 1
#
#         i += 1
#     return len(nums)
#
#
# def removeDuplicates(nums):
#     if len(nums) <= 2:
#         return len(nums)
#     slow = 0
#     k = 1
#     for fast in range(1, len(nums)):
#         if nums[fast] == nums[slow]:
#             k += 1
#             if k == 2:  # its a duplicate but its still a safe number so we can increase slow
#                 slow += 1
#                 nums[slow] = nums[fast]
#         else:
#             slow += 1
#             nums[slow] = nums[fast]
#             k = 1
#     return slow + 1
#
#
# removeDuplicates([1, 1, 1, 2, 2, 3, 3, 3])


# def canJump(nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     if nums[0] == 0 and len(nums) > 1:
#         return False
#     i = 0
#     result = True
#     if 0 in nums:
#         i_null = nums.index(0)
#         for j in nums[:i_null]:
#             if j <= i_null - i:
#                 result = False
#             else:
#                 result = True
#             i += 1
#     return result


# def canJump(nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     result = True
#     if 0 in nums:
#         nums = "".join([str(n) for n in nums]).split("0")
#
#         print(nums)
#         for i in nums[:-1]:
#             for j in range(len(i)):
#                 if int(i[j]) > len(i) - int(j):
#                     result = True
#                     break
#                 result = False
#             if result is False:
#                 return result
#         return result

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if nums[0] == 0 and len(nums) > 1:
        return False
    # if nums[-1] == 0:
    #     nums = nums[:-1]
    i = 0
    result = True
    while i < len(nums):

        for j in range(1, nums[i]+1):
            if nums[i + nums[j]] or i == len(nums) - 1:
                result = True
                break
            result = False
        if result is False:
            return result
        i += 1
    return result



print(canJump([1,3,7,0,2,0,0,0,0]))
