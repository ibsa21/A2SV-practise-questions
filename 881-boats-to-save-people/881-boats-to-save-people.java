class Solution {
    public int numRescueBoats(int[] people, int limit) {
        //3,3,4,5
        // min_number of boot = 1
        // max_number of boot = people.length
        // 1, 2, 2,  3
        //
        Arrays.sort(people);
        
        int left = 0;
        int right = people.length - 1;
        
        int number_boot = 0;
        
        while (left <= right) {
            
            if (people[left] + people[right] > limit) {
                right -= 1;
            }
            else {
                left += 1;
                right -=1;
            }
            number_boot += 1;

        }
        
        return number_boot;
    }
}