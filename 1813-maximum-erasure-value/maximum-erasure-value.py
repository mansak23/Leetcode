class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
    
        seen = set()          # To store unique elements in current window
        left = 0              # Left pointer of sliding window
        curr_sum = 0          # Current sum of unique elements in window
        max_sum = 0           # Store max sum
        best_subarray = []    # To store the optimal subarray
        current_subarray = [] # To track current subarray

        for right in range(len(nums)):
            while nums[right] in seen:
            # Remove elements from the left until duplicate is gone
                seen.remove(nums[left])
                curr_sum -= nums[left]
                current_subarray.pop(0)
                left += 1

            # Add new unique element
            seen.add(nums[right])
            curr_sum += nums[right]
            current_subarray.append(nums[right])

        # Update max sum and subarray if this is the best so far
            if curr_sum > max_sum:
                max_sum = curr_sum
                best_subarray = current_subarray[:]

        return max_sum
