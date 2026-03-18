class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Length of array
        n = len(nums)

        # Handle cases where k > n
        # Example: rotate by 10 on size 7 → same as rotate by 3
        k %= n

        # Repeat rotation k times
        for _ in range(k):

            # Step 1: remove last element
            last = nums.pop()

            # Step 2: insert it at the beginning
            nums.insert(0, last)