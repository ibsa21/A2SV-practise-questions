class Solution {
public:
    int thirdMax(vector<int>& nums) {
        //int INT_MIN = nums[0];
        int firstMax = INT_MIN;
        
        for(int i = 0; i< nums.size(); i++) {
            if(firstMax < nums[i]) {
                firstMax = nums[i];
            }
        }
        
        int secondMax = INT_MIN ;
        for(int i = 0; i< nums.size(); i++) {
            if(secondMax < nums[i] && nums[i] < firstMax) {
                secondMax = nums[i];
            }
        }
        bool isFound = false;
        int thirdMax = INT_MIN;
        for(int i = 0; i< nums.size(); i++) {
            if(thirdMax <= nums[i] && nums[i] < secondMax) {
                thirdMax = nums[i];
                isFound = true;
            }
        }
        
        if(isFound) {
            return thirdMax;
        }else {
            return firstMax;
        }
        
    }
};
