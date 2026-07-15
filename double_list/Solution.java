package double_list;

public class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] new_array = new int[n * 2];
        for (int i = 0; i < n * 2; i++) {
            if (i < n) {
                new_array[i] = nums[i];
            } else {
                new_array[i] = nums[i - n];
            }
        }
        return new_array;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1, 2, 1};
        int[] result = solution.getConcatenation(nums);
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
