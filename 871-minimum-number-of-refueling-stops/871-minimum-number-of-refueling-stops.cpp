// typedef unsigned long long ;
class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        vector<unsigned long long>dp(stations.size() + 1, 0);
        dp[0] = startFuel;
        
        for(int i = 0; i < stations.size(); i ++) {
            // const auto [cur_distance, fuel] = stations[i];
            for (int j = i; j >-1; j--) {
                if (dp[j] >= stations[i][0]) {
                    dp[j + 1] = max(dp[j + 1], dp[j] + stations[i][1]);
                }
            }
        }
        
        for (int i = 0; i < dp.size(); i ++) {
            if (dp[i] >= target) return i;
        }
        return -1;
    }
};