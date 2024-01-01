class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, remaining, path):
            # If the combination is done
            if len(path) == k and remaining == 0:
                result.append(path[:])
                return
            # Explore further
            for i in range(start, 10):
                # Skip if remaining sum would be negative
                if remaining - i < 0:
                    break
                # Include the current number and explore further
                path.append(i)
                backtrack(i + 1, remaining - i, path)
                # Backtrack
                path.pop()

        result = []
        backtrack(1, n, [])
        return result

