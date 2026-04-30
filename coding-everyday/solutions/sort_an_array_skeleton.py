"""
Sort an Array — Skeleton
배열 정렬하기 — 스켈레톤

LeetCode 912: https://leetcode.com/problems/sort-an-array/

Mission / 미션:
    Sort a list of integers in ascending order WITHOUT using built-in
    sort functions, min(), or max().
    내장 정렬 함수, min(), max()를 사용하지 않고
    정수 리스트를 오름차순으로 정렬하세요.
"""


def sort_array(nums: list[int]) -> list[int]:
    """
    Sort the list in ascending order using selection sort.
    선택 정렬을 사용하여 리스트를 오름차순으로 정렬합니다.
    """
    # KO: 1. 리스트의 길이를 변수 n에 저장하세요.
    # EN: 1. Store the length of the list in a variable called n.
    n = len(nums)

    # KO: 2. 바깥쪽 반복문: 정렬된 부분을 한 칸씩 늘려갑니다.
    #        i는 "지금부터 채울 위치"입니다.
    # EN: 2. Outer loop: grow the sorted prefix by one element at a time.
    #        i is "the position we are about to fill".
    for i in range(n):

        # KO: 3. nums[i:] 중에서 가장 작은 값의 인덱스를 추적할 변수를 초기화하세요.
        #        처음에는 i 자신이 가장 작다고 가정합니다.
        # EN: 3. Initialize a variable to track the index of the smallest value
        #        in nums[i:]. Start by assuming i itself is the smallest.
        min_index = i

        # KO: 4. 안쪽 반복문: i+1부터 끝까지 돌면서, 더 작은 값을 찾으면
        #        min_index를 갱신하세요.
        # EN: 4. Inner loop: iterate from i+1 to the end. If you find a smaller
        #        value, update min_index.
        for j in range(i + 1, n):

            # KO: 5. nums[j]가 nums[min_index]보다 작으면 min_index를 j로 바꾸세요.
            # EN: 5. If nums[j] is smaller than nums[min_index], set min_index to j.
            if nums[j] < nums[min_index]:
                min_index = j

        # KO: 6. nums[i]와 nums[min_index]의 위치를 교환하세요.
        #        Python에서는 a, b = b, a로 한 줄에 가능합니다!
        # EN: 6. Swap nums[i] and nums[min_index].
        #        In Python, you can do this in one line: a, b = b, a!
        nums[i], nums[min_index] = nums[min_index], nums[i]

    # KO: 7. 정렬된 리스트를 반환하세요.
    # EN: 7. Return the sorted list.
    return nums


if __name__ == "__main__":
    # 테스트 케이스 / Test cases
    print("Test 1:", sort_array([5, 2, 3, 1]))
    # 예상 / Expected: [1, 2, 3, 5]

    print("Test 2:", sort_array([5, 1, 1, 2, 0, 0]))
    # 예상 / Expected: [0, 0, 1, 1, 2, 5]

    print("Test 3:", sort_array([1]))
    # 예상 / Expected: [1]

    print("Test 4:", sort_array([1, 2, 3, 4, 5]))
    # 예상 / Expected: [1, 2, 3, 4, 5]

    print("Test 5:", sort_array([5, 4, 3, 2, 1]))
    # 예상 / Expected: [1, 2, 3, 4, 5]

    print("Test 6:", sort_array([-5, 3, -1, 0, 2]))
    # 예상 / Expected: [-5, -1, 0, 2, 3]
