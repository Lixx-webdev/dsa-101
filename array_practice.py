# Array DSA Practice File
# Run: python array_practice.py
# Each function has a problem statement, solution, and test cases.
# Try solving it yourself first (delete the body and rewrite it) before checking the solution.


# ---------- 1. Two Sum ----------
def two_sum(arr, target):
    """Return indices [i, j] such that arr[i] + arr[j] == target."""
    seen = {}
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return [-1, -1]


# ---------- 2. Maximum Subarray (Kadane's) ----------
def max_subarray(arr):
    """Return the largest sum of any contiguous subarray."""
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


# ---------- 3. Best Time to Buy and Sell Stock ----------
def max_profit(prices):
    """Return max profit from one buy + one later sell."""
    min_price = float('inf')
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best


# ---------- 4. Product of Array Except Self ----------
def product_except_self(nums):
    """Return array where res[i] = product of all nums except nums[i]. No division."""
    n = len(nums)
    res = [1] * n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res


# ---------- 5. Move Zeroes ----------
def move_zeroes(nums):
    """Move all zeros to the end in place, keep relative order of non-zeros."""
    insert_pos = 0
    for x in nums:
        if x != 0:
            nums[insert_pos] = x
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
    return nums


# ---------- 6. Merge Intervals ----------
def merge_intervals(intervals):
    """Merge all overlapping intervals."""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result


# ---------- 7. Container With Most Water ----------
def max_area(height):
    """Two vertical lines form a container; return max water it can hold."""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


# ---------- 8. Rotate Array ----------
def rotate(nums, k):
    """Rotate array right by k steps, in place."""
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = list(reversed(nums[:k]))
    nums[k:] = list(reversed(nums[k:]))
    return nums


# ---------- 9. Find Duplicate Number (Floyd's cycle detection) ----------
def find_duplicate(nums):
    """nums has n+1 ints in range [1,n]; find the one duplicate. O(1) space."""
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow


# ---------- 10. Trapping Rain Water ----------
def trap(height):
    """Return total water trapped between bars after raining."""
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water


# ---------- 11. Subarray Sum Equals K ----------
def subarray_sum(nums, k):
    """Count number of contiguous subarrays that sum to k."""
    count = 0
    curr_sum = 0
    prefix_counts = {0: 1}
    for x in nums:
        curr_sum += x
        count += prefix_counts.get(curr_sum - k, 0)
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
    return count


# ---------- 12. Sort Colors (Dutch National Flag) ----------
def sort_colors(nums):
    """Sort array of 0s, 1s, 2s in place, one pass."""
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


# ------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------
def run_tests():
    tests = [
        ("two_sum", two_sum([2, 7, 11, 15], 9), [0, 1]),
        ("max_subarray", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6),
        ("max_profit", max_profit([7, 1, 5, 3, 6, 4]), 5),
        ("product_except_self", product_except_self([1, 2, 3, 4]), [24, 12, 8, 6]),
        ("move_zeroes", move_zeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0]),
        ("merge_intervals", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]]),
        ("max_area", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49),
        ("rotate", rotate([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
        ("find_duplicate", find_duplicate([1, 3, 4, 2, 2]), 2),
        ("trap", trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6),
        ("subarray_sum", subarray_sum([1, 1, 1], 2), 2),
        ("sort_colors", sort_colors([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2]),
    ]

    passed = 0
    for name, actual, expected in tests:
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got {actual}, expected {expected}")
        passed += ok

    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
