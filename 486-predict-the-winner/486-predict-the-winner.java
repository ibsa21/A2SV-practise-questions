class Solution {
    public boolean PredictTheWinner(int[] nums) {
        
        int result = recursive(nums, 0, nums.length-1);
        int sumValue = 0;
        
        for  (int i = 0; i < nums.length; i++) {
            sumValue += nums[i];
        }
        return result >= (double) sumValue/2;
        
    }
    
    static int recursive(int[] nums, int left, int right) {
        
        if (left > right || left > nums.length-1 || right < 0) {
            return 0;
        }
        
        int leftValue = nums[left] + Math.min(recursive(nums, left + 2, right), recursive(nums, left+1, right-1));
        int rightValue = nums[right] + Math.min(recursive(nums, left, right-2), recursive(nums, left+1, right-1));
        
        return Math.max(leftValue, rightValue);
    }
}