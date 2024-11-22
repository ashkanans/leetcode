class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        substr = ""
        longset_substr = ""
        for c in s:
            if c in substr:
                temp_substr = substr + c
                actual_substr = temp_substr.split(c)[-2]
                actual_substr += c
                substr = actual_substr
                if len(substr) > len(longset_substr):
                    longset_substr = substr
            else:
                substr += c
                if len(substr) > len(longset_substr):
                    longset_substr = substr

        return len(longset_substr)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Simple cases
        {"input": "nfpdmpi", "expected_output": 5},
        {"input": "abcabcbb", "expected_output": 3},
        {"input": "bbbbb", "expected_output": 1},
        {"input": "pwwkew", "expected_output": 3},

        # Edge cases
        {"input": "", "expected_output": 0},  # Empty string
        {"input": " ", "expected_output": 1},  # Single character (space)
        {"input": "au", "expected_output": 2},  # Two unique characters
        {"input": "dvdf", "expected_output": 3},  # Overlapping substrings
        {"input": "abcdefg", "expected_output": 7},  # All unique characters
        {"input": "aabbcc", "expected_output": 2},  # Repeated pairs of characters
        {"input": "a", "expected_output": 1},  # Single character
        {"input": "aa", "expected_output": 1},  # Two identical characters
        {"input": "tmmzuxt", "expected_output": 5},  # Complex substring handling

        # Longer strings
        {"input": "abcabcabcdabcde", "expected_output": 5},  # Long repeating pattern
        {"input": "abcdefghijklmnopqrstuvwxyz", "expected_output": 26},  # All unique lowercase letters
        {"input": "abac", "expected_output": 3},  # Early termination of unique substring

        # Strings with symbols and spaces
        {"input": "abc!@#abc!@#", "expected_output": 6},  # With symbols
        {"input": "123 456 789", "expected_output": 7},  # Digits and spaces
        {"input": "!@#$%^&*()_+", "expected_output": 12},  # Only symbols
        {"input": "  ", "expected_output": 1},  # Multiple spaces

        # Stress cases
        {"input": "a" * 10000, "expected_output": 1},  # Large string with same character
        {"input": "abcdefg" * 1000, "expected_output": 7},  # Large string with all unique substrings
        {"input": "".join(chr(i % 128) for i in range(1000)), "expected_output": 128},  # ASCII characters repeating
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases):
        result = solution.lengthOfLongestSubstring(test_case["input"])
        assert result == test_case["expected_output"], (
            f"Test case {i + 1} failed: "
            f"input={test_case['input']}, expected={test_case['expected_output']}, got={result}"
        )

    print("All test cases passed!")
