class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        
        long total_sum = 0;
        for(int i = 0; i < nums.size(); i++) {
            
            int max_arr = nums[i];
            int min_arr = nums[i];
            
            for (int j = i; j < nums.size(); j++) {
                
                if (nums[j] < min_arr)
                    min_arr = nums[j];
                    
                if (nums[j] > max_arr)
                    max_arr = nums[j];
                
                total_sum  += max_arr - min_arr;
            }
        }
        
        return total_sum;
    }
};