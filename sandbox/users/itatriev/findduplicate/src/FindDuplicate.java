public class FindDuplicate {
    public static void main(String[] args) {
        System.out.println(findDuplicate(new int[] {4, 5, 3, 1, 2, 6, 5}));
    }

    public static int findDuplicate(int[] nums) {
        int slow = nums[0];
        int fast = nums[0];
        for (int i = 0; i < nums.length; i++) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) {
                break;
            }
        }

        int p1 = nums[0];
        int p2 = fast;
        while (p1 != p2) {
            p1 = nums[p1];
            p2 = nums[p2];
        }

        return p1;
    }
}
