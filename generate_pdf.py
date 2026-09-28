from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Preformatted, ListFlowable, ListItem, HRFlowable
)
from reportlab.pdfbase.pdfmetrics import stringWidth

styles = getSampleStyleSheet()

title_style = ParagraphStyle('TitleBig', parent=styles['Title'], fontSize=26, spaceAfter=6)
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=13, textColor=colors.HexColor('#555555'), spaceAfter=30)
h1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, spaceBefore=18, spaceAfter=10, textColor=colors.HexColor('#1a1a1a'))
h2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, spaceBefore=14, spaceAfter=8, textColor=colors.HexColor('#2c3e50'))
h3 = ParagraphStyle('H3', parent=styles['Heading3'], fontSize=12, spaceBefore=10, spaceAfter=6, textColor=colors.HexColor('#34495e'))
body = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10.5, leading=15, spaceAfter=8, alignment=TA_LEFT)
bullet = ParagraphStyle('Bullet', parent=body, leftIndent=14, spaceAfter=4)
code_style = ParagraphStyle(
    'Code', parent=styles['Normal'], fontName='Courier', fontSize=9, leading=12,
    backColor=colors.HexColor('#f5f5f5'), borderPadding=8, spaceAfter=12, spaceBefore=4,
    leftIndent=4,
)

def code(text):
    return Preformatted(text, code_style)

def para(text):
    return Paragraph(text, body)

def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, bullet), bulletColor=colors.HexColor('#2c3e50')) for i in items],
        bulletType='bullet', start='•', leftIndent=18,
    )

def divider():
    return HRFlowable(width="100%", thickness=0.6, color=colors.HexColor('#cccccc'), spaceBefore=6, spaceAfter=14)

story = []

# ---------------- Title Page ----------------
story.append(Spacer(1, 1.8*inch))
story.append(Paragraph("Arrays Data Structure", title_style))
story.append(Paragraph("From Scratch to Advanced — Concepts, Patterns, Classic Interview Problems, and Tips", subtitle_style))
story.append(Spacer(1, 0.3*inch))
story.append(divider())
story.append(Paragraph("A complete reference covering array fundamentals, core problem-solving patterns, "
                        "12 classic interview problems with solutions, and a general framework for building "
                        "coding logic.", body))
story.append(PageBreak())

# ---------------- Section 1: What is an array ----------------
story.append(Paragraph("1. What is an Array?", h1))
story.append(para("A contiguous block of memory storing elements of the same type, accessed by index in "
                   "O(1) time because the address is computed directly:"))
story.append(code("address = base_address + index * element_size"))

story.append(Table(
    [["Index", "0", "1", "2", "3", "4"],
     ["Value", "10", "20", "30", "40", "50"]],
    colWidths=[70]+[60]*5,
    style=TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0,0), (0,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('BACKGROUND', (1,0), (-1,0), colors.HexColor('#ecf0f1')),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
    ])
))
story.append(Spacer(1, 12))

story.append(Paragraph("Static vs Dynamic Arrays", h2))
story.append(bullets([
    "<b>Static arrays</b> (C, Java arrays): fixed size, set at creation time.",
    "<b>Dynamic arrays</b> (Python <font face='Courier'>list</font>, Java <font face='Courier'>ArrayList</font>, "
    "C++ <font face='Courier'>vector</font>, JS <font face='Courier'>Array</font>): resize automatically by "
    "allocating a new, larger block (usually 2x) and copying elements over when full.",
]))

# ---------------- Section 2: Complexity table ----------------
story.append(Paragraph("2. Time Complexity Cheat Sheet", h1))
story.append(Table(
    [["Operation", "Static Array", "Dynamic Array"],
     ["Access by index", "O(1)", "O(1)"],
     ["Search (unsorted)", "O(n)", "O(n)"],
     ["Search (sorted, binary search)", "O(log n)", "O(log n)"],
     ["Insert/delete at end", "N/A (fixed)", "O(1) amortized"],
     ["Insert/delete at start/middle", "O(n)", "O(n)"]],
    colWidths=[220, 130, 130],
    style=TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONTSIZE', (0,0), (-1,-1), 9.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7f7f7')]),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
    ])
))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Why \"amortized\" O(1) for dynamic array append?</b> Most appends are O(1), but "
                       "occasionally the array is full and must resize (O(n) copy). Averaged over many "
                       "operations, it still comes out to O(1) per append.", body))

# ---------------- Section 3: Basic operations ----------------
story.append(Paragraph("3. Basic Operations (Python)", h1))
story.append(code(
"""arr = [10, 20, 30, 40, 50]

arr[2]                  # access -> 30
arr.append(60)          # insert at end -> O(1) amortized
arr.insert(1, 15)       # insert at index -> O(n), shifts elements right
arr.pop()               # remove last -> O(1)
arr.pop(1)              # remove at index -> O(n), shifts elements left
30 in arr               # search -> O(n)
arr[1:3]                # slicing -> O(k)"""
))
story.append(Paragraph("Traversal", h3))
story.append(code(
"""for x in arr:
    print(x)"""
))
story.append(Paragraph("2D Arrays / Matrices", h3))
story.append(code(
"""matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[1][2]   # -> 6, row 1 col 2"""
))

story.append(PageBreak())

# ---------------- Section 4: Core Techniques ----------------
story.append(Paragraph("4. Core Techniques (The Toolbox)", h1))
story.append(para("These four patterns solve roughly 80% of array interview questions."))

story.append(Paragraph("A. Two Pointers", h2))
story.append(para("Use when the array is sorted, or you're comparing elements from both ends, or partitioning in place."))
story.append(code(
"""def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]"""
))

story.append(Paragraph("B. Sliding Window", h2))
story.append(para("Use for subarray/substring problems with a contiguous window — max/min sum, longest/shortest "
                   "subarray meeting a condition."))
story.append(code(
"""def max_sum_subarray_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]   # slide: add new, drop old
        max_sum = max(max_sum, window_sum)
    return max_sum"""
))

story.append(Paragraph("C. Prefix Sum", h2))
story.append(para("Use for range-sum queries or subarray-sum problems — precompute cumulative sums so any range "
                   "query is O(1)."))
story.append(code(
"""def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i+1] = prefix[i] + x
    return prefix

# sum of arr[l..r] inclusive:
# prefix[r+1] - prefix[l]"""
))

story.append(Paragraph("D. Hashing (dict/set) for O(1) lookup", h2))
story.append(para("Use to trade space for time — turn an O(n²) brute force into O(n)."))
story.append(code(
"""def two_sum(arr, target):
    seen = {}  # value -> index
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return [-1, -1]"""
))

story.append(PageBreak())

# ---------------- Section 5: Classic Problems ----------------
story.append(Paragraph("5. Classic Interview Problems", h1))

def problem(num, title, statement, sol, note=None):
    story.append(Paragraph(f"{num}. {title}", h2))
    story.append(Paragraph(f"<i>{statement}</i>", body))
    story.append(code(sol))
    if note:
        story.append(Paragraph(f"<b>Key insight:</b> {note}", body))

problem(1, "Two Sum",
        "Given array + target, return indices of two numbers that add to target.",
"""def two_sum(arr, target):
    seen = {}
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return [-1, -1]""",
        "Hashmap trades O(n) space for O(n) time instead of O(n^2) brute force.")

problem(2, "Maximum Subarray (Kadane's Algorithm)",
        "Find the contiguous subarray with the largest sum.",
"""def max_subarray(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far""",
        "If the running sum goes negative, drop it and restart from the current element. O(n) time, O(1) space.")

problem(3, "Best Time to Buy and Sell Stock",
        "Find max profit from one buy + one sell.",
"""def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit""",
        "Track the minimum price seen so far; profit is always current price minus that minimum.")

problem(4, "Product of Array Except Self",
        "Return an array where each element is the product of all others, without division, in O(n).",
"""def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res""",
        "Compute prefix products left-to-right, then multiply in suffix products right-to-left.")

problem(5, "Move Zeroes",
        "Move all zeros to the end, keep relative order of non-zeros, in place.",
"""def move_zeroes(nums):
    insert_pos = 0
    for x in nums:
        if x != 0:
            nums[insert_pos] = x
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0""",
        "Two-pass in-place write pointer — overwrite non-zeros forward, then fill the rest with zeros.")

story.append(PageBreak())

problem(6, "Merge Intervals",
        "Merge all overlapping intervals.",
"""def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result""",
        "Sorting by start time turns an O(n^2) overlap check into a single linear sweep.")

problem(7, "Container With Most Water",
        "Two vertical lines form a container; find the pair with max area.",
"""def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best""",
        "Always move the pointer at the shorter line — moving the taller one can never increase the area.")

problem(8, "Rotate Array",
        "Rotate an array right by k steps, in place.",
"""def rotate(nums, k):
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])""",
        "Reverse the whole array, then reverse each of the two resulting segments.")

problem(9, "Find Duplicate Number",
        "Array of n+1 ints in range [1,n]; find the duplicate without modifying the array or using extra space.",
"""def find_duplicate(nums):
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
    return slow""",
        "Floyd's cycle detection — treat the array as an implicit linked list via indices. O(n) time, O(1) space.")

problem(10, "Trapping Rain Water",
        "Compute how much water is trapped between bars after raining.",
"""def trap(height):
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
    return water""",
        "Two pointers track the tallest bar seen so far from each side; the shorter side bounds trapped water.")

story.append(PageBreak())

problem(11, "Subarray Sum Equals K",
        "Count the number of contiguous subarrays that sum to k.",
"""def subarray_sum(nums, k):
    count = 0
    curr_sum = 0
    prefix_counts = {0: 1}
    for x in nums:
        curr_sum += x
        count += prefix_counts.get(curr_sum - k, 0)
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
    return count""",
        "Combines prefix sum with a hashmap of prefix-sum frequencies.")

problem(12, "Sort Colors (Dutch National Flag)",
        "Sort an array of 0s, 1s, 2s in place, in one pass.",
"""def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1""",
        "Three pointers partition the array into 0s, 1s, and 2s regions in a single pass.")

story.append(PageBreak())

# ---------------- Section 6: Tips and Tricks ----------------
story.append(Paragraph("6. Tips & Tricks for Solving Array Problems", h1))
story.append(bullets([
    "<b>Always check: is it sorted?</b> Sorted → binary search or two pointers unlocks O(log n) or O(n) solutions.",
    "<b>Brute force first, then optimize.</b> State the O(n²) solution out loud, then ask \"what am I recomputing?\" — "
    "that recomputation is usually solved by a hashmap or prefix sum.",
    "<b>Two pointers from opposite ends</b> when comparing/combining the smallest and largest remaining elements "
    "(sorted arrays, palindrome checks, container problems).",
    "<b>Sliding window</b> whenever the problem says \"contiguous subarray/substring\" and asks for max/min/count "
    "satisfying some condition — grow the window, shrink it when a constraint is violated.",
    "<b>Prefix sums</b> turn any \"sum of range\" query into O(1) after O(n) preprocessing.",
    "<b>HashMap/Set trades space for time.</b> Nested loop searching for a value? Ask \"can I remember what I've seen?\"",
    "<b>In-place tricks:</b> use the array itself as a marker (negate values, swap to correct position) for O(1) space "
    "— common in \"find missing/duplicate number\" problems.",
    "<b>Sorting first</b> often simplifies a problem (merge intervals, 3Sum) at the cost of O(n log n).",
    "<b>Watch for off-by-one errors</b> at loop boundaries — trace a small 3-4 element example by hand.",
    "<b>Edge cases to always check:</b> empty array, single element, all same elements, sorted, reverse sorted, "
    "negative numbers, duplicates.",
    "<b>For \"in-place\" requirements</b>, think about iteration direction (forward vs backward) to avoid overwriting "
    "data you still need.",
    "<b>Cycle detection (Floyd's)</b> is a hidden gem for \"array as implicit linked list\" problems.",
    "<b>Kadane's pattern</b> (running value that resets when unhelpful) generalizes beyond sums — max product "
    "subarray, longest subarray patterns, etc.",
    "<b>Explain time/space complexity out loud</b> as you code — interviewers weight this as much as correctness.",
]))

story.append(PageBreak())

# ---------------- Section 7: Logic Building Framework ----------------
story.append(Paragraph("7. Building Coding Logic — A General Framework", h1))
story.append(para("This process works for any DSA problem, not just arrays."))

story.append(Paragraph("Step 1 — Understand before solving", h2))
story.append(para("Restate the problem in your own words. Identify: inputs, outputs, constraints (size, value "
                   "range), and edge cases. Manually work a small example by hand — 3-5 elements — before writing "
                   "any code."))

story.append(Paragraph("Step 2 — Brute force first, always", h2))
story.append(para("Ask \"what's the dumbest solution that obviously works?\" State its time complexity out loud. "
                   "This gives you a correctness baseline and reveals where the waste is."))

story.append(Paragraph("Step 3 — Find what's being recomputed", h2))
story.append(bullets([
    "Recomputing a sum repeatedly → <b>prefix sum</b>",
    "Recomputing \"have I seen this value\" → <b>hashmap/set</b>",
    "Recomputing a min/max over a shrinking window → <b>sliding window / monotonic deque</b>",
    "Re-scanning from the start each time → <b>two pointers</b>",
]))

story.append(Paragraph("Step 4 — Match the problem shape to a known pattern", h2))
story.append(Table(
    [["Signal in problem", "Likely pattern"],
     ["\"sorted array\"", "binary search, two pointers"],
     ["\"contiguous subarray/substring\"", "sliding window"],
     ["\"count subarrays/pairs with sum/property\"", "prefix sum + hashmap"],
     ["\"find pair/triplet\"", "two pointers (after sorting) or hashmap"],
     ["\"next greater/smaller element\"", "monotonic stack"],
     ["\"kth largest/smallest\", \"top k\"", "heap"],
     ["\"overlapping ranges\"", "sort by start, sweep"],
     ["\"graph of choices, all paths\"", "backtracking/DFS"],
     ["\"optimal value, choices build on subproblems\"", "dynamic programming"],
     ["\"linked list/array cycle\"", "fast & slow pointers"]],
    colWidths=[260, 220],
    style=TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONTSIZE', (0,0), (-1,-1), 9.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7f7f7')]),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ])
))
story.append(Spacer(1, 10))

story.append(Paragraph("Step 5 & 6 — Code, trace, and analyze", h2))
story.append(para("Code the optimized version, then trace it by hand on your small example before running it. "
                   "Analyze complexity explicitly — say it out loud, even alone. This trains the habit interviewers "
                   "want to see."))

story.append(Paragraph("How to Actually Build This Skill", h2))
story.append(bullets([
    "<b>Volume with spaced repetition beats one-shot difficulty.</b> Solve ~150-200 problems across patterns "
    "(NeetCode 150 / Blind 75 are well-curated) rather than 500 random ones.",
    "<b>Study by pattern, not by random difficulty.</b> Do 8-10 sliding window problems in a row, then 8-10 "
    "two-pointer problems, etc.",
    "<b>After solving, ask \"could I have recognized this pattern faster?\"</b> Write one sentence: \"sorted + "
    "pair search → two pointers.\"",
    "<b>Re-solve problems after a gap</b> (1-2 weeks later) without looking at your old solution.",
    "<b>Explain your approach out loud before coding</b>, even alone.",
    "<b>When stuck for more than ~10-15 min</b>, look at just the name of the technique (not the solution) and try again.",
]))

story.append(PageBreak())

# ---------------- Section 8: 3-Week Practice Plan ----------------
story.append(Paragraph("8. 3-Week Practice Plan", h1))

def week_table(title, rows):
    story.append(Paragraph(title, h2))
    data = [["Day", "Pattern", "Problems"]] + rows
    t = Table(data, colWidths=[35, 130, 315])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONTSIZE', (0,0), (-1,-1), 8.7),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7f7f7')]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

week_table("Week 1 — Two Pointers, Sliding Window, Prefix Sum", [
    ["1", "Two Pointers (basics)", "Two Sum II (sorted), Valid Palindrome, Reverse Array"],
    ["2", "Two Pointers (advanced)", "Container With Most Water, 3Sum, Sort Colors"],
    ["3", "Sliding Window (fixed size)", "Max Sum Subarray of Size K, Average of Subarrays"],
    ["4", "Sliding Window (variable size)", "Longest Substring Without Repeating Chars, Minimum Size Subarray Sum"],
    ["5", "Prefix Sum", "Range Sum Query, Subarray Sum Equals K"],
    ["6", "Mixed review", "Redo 2 hardest from days 1-5 without looking"],
    ["7", "Rest / catch up", "Re-attempt anything you got wrong"],
])

week_table("Week 2 — Hashing, Sorting Tricks, Stacks", [
    ["8", "Hashmap/Set", "Two Sum, Group Anagrams, Contains Duplicate"],
    ["9", "Hashmap (frequency)", "Top K Frequent Elements, Longest Consecutive Sequence"],
    ["10", "Sort-first tricks", "Merge Intervals, Non-overlapping Intervals"],
    ["11", "Cyclic sort / in-place index tricks", "Find Missing Number, Find Duplicate Number, First Missing Positive"],
    ["12", "Monotonic Stack", "Next Greater Element, Daily Temperatures"],
    ["13", "Monotonic Stack (harder)", "Trapping Rain Water, Largest Rectangle in Histogram"],
    ["14", "Rest / mixed review", "Redo 2 hardest from week 2"],
])

week_table("Week 3 — Kadane's Variants, Binary Search, Combine Patterns", [
    ["15", "Kadane's family", "Maximum Subarray, Maximum Product Subarray"],
    ["16", "Binary Search on answer", "Search in Rotated Sorted Array, Find Min in Rotated Array"],
    ["17", "Matrix/2D arrays", "Rotate Image, Spiral Matrix, Set Matrix Zeroes"],
    ["18", "Greedy + arrays", "Jump Game, Gas Station"],
    ["19", "Combine 2+ patterns", "Product of Array Except Self, 3Sum Closest"],
    ["20", "Mock interview", "3 random problems from days 1-19, cold, 25 min each, explain out loud"],
    ["21", "Review & reflect", "Note which pattern took longest to recognize; redo those 3"],
])

story.append(Paragraph("Rules to Actually Make This Work", h2))
story.append(bullets([
    "<b>Timebox each problem to 20-25 min</b> before peeking at a hint.",
    "<b>After solving, write one line:</b> \"signal → pattern\" in a running notes file.",
    "<b>Days 6, 14, 21 are non-negotiable</b> — spaced repetition converts memorization into recognition.",
    "<b>Say your approach out loud before coding</b>, every time, even alone.",
]))

doc = SimpleDocTemplate(
    "Arrays_Complete_Guide.pdf",
    pagesize=letter,
    topMargin=0.75*inch, bottomMargin=0.75*inch,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    title="Arrays: From Scratch to Advanced",
    author="Claude Code",
)
doc.build(story)
print("PDF generated: Arrays_Complete_Guide.pdf")
