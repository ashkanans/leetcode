# two_sum.py

def two_sum(nums, target):
    """
    Function to find two indices in nums such that the numbers add up to the target.

    Parameters:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    List[int]: A list of two indices whose elements sum up to target.
    """
    num_to_index = {}

    # Loop through the list
    for index, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If found, return the indices
            return [num_to_index[complement], index]

        # Store the index of the current number in the dictionary
        num_to_index[num] = index



if __name__ == "__main__":
    # Test cases
    test_cases = [
        {
            "input": {"nums": [2, 7, 11, 15], "target": 9},
            "expected_output": [0, 1]
        },
        {
            "input": {"nums": [3, 2, 4], "target": 6},
            "expected_output": [1, 2]
        },
        {
            "input": {"nums": [3, 3], "target": 6},
            "expected_output": [0, 1]
        },
        {
            "input": {"nums": [2, 5, 5, 11], "target": 10},
            "expected_output": [1, 2]
        }
    ]

    for i, test_case in enumerate(test_cases):
        nums = test_case["input"]["nums"]
        target = test_case["input"]["target"]

        result = two_sum(nums.copy(), target)

        # Check if result contains two valid indices
        assert len(result) == 2, f"Test case {i + 1} failed: result should contain two indices, got {result}"

        # Check if indices are different and within bounds
        assert result[0] != result[1], f"Test case {i + 1} failed: indices should be different, got {result}"
        assert 0 <= result[0] < len(nums) and 0 <= result[1] < len(
            nums), f"Test case {i + 1} failed: indices out of bounds, got {result}"

        # Check if the elements at the returned indices sum up to the target
        assert nums[result[0]] + nums[
            result[1]] == target, f"Test case {i + 1} failed: elements at {result} do not sum to {target}"

    print("All test cases passed!")
