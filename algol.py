#SEVENTH FILE
#The algorithm to perfom binary search on an unsorted array

Step 1. Find the Minimum and Maximum Values: Iterate through the array to find the minimum and maximum values. This step is necessary to set the range for the binary search.

Step 2. Initialize the Search Range: Set the left pointer to the minimum value and the right pointer to the maximum value found in Step 1.

Step 3. Perform Binary Search: Continue the binary search until the left pointer is less than or equal to the right pointer.

Step 4. Calculate the Mid-point: Calculate the mid-point of the current range using the formula mid = left + (right - left) // 2.

Step 5. Check the Mid-point Value: Compare the value at the mid-point with the target value.

Step 6. Adjust Search Range: If the mid-point value matches the target value, the search is successful, and you can return the index. If the mid-point value is less than the target value, update the left pointer to mid + 1 to search the right half of the current range. If the mid-point value is greater than the target value, update the right pointer to mid - 1 to search the left half of the current range.

Step 7. Repeat Binary Search: Repeat Steps 3 to 6 until the left pointer becomes greater than the right pointer. If the target value is not found, return a failure indicator (e.g., -1).

