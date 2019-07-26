class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0;
        for (int i=0;i<nums.length;i++){
            sum+=nums[i];
        }
        if (sum%k!=0){
            return false;
        }
        HashMap<Integer, Integer> hs = new HashMap<Integer, Integer>();
        return helper(nums, k, 0, hs, sum);
    }
    
    private boolean helper(int[] nums, int k, int index, HashMap<Integer, Integer> hs, int sum){
        if (index>=nums.length) 
            return true;
        for (int i=0;i<k;i++){
            if (hs.getOrDefault(i,0)+nums[index]<= sum/k){
                hs.put(i, hs.getOrDefault(i, 0)+nums[index]);
                if (helper(nums, k, index+1, hs, sum))
                    return true;           
                hs.put(i, hs.get(i)-nums[index]);
            }
            if (hs.getOrDefault(i,0)==0)
                break;
        }
        return false;
    }
}