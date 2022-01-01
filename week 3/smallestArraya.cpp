class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int>numberStore (nums.size(), 0);
        for(int j = 0; j < nums.size(); j++) {
            for(int i = 0; i < nums.size(); i++) {
            if ((nums[i] < nums[j]) && (nums[j] != nums[i])) {
                numberStore[j] = numberStore[j] + 1;
            }
        }
        }
        return numberStore;
    }
};
