//Runtime: 57 ms, faster than 99.40%
// o(nlogn) cuz pop() offer() takes o(n)
class KthLargest {
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    private int size;
    
    public KthLargest(int k, int[] nums) {
        this.size = k;
        for (int n : nums) add (n);
    }
    
    public int add(int val) {
        if (minHeap.size() < size)
            minHeap.offer(val);
        else if (minHeap.peek() < val) {
            minHeap.poll();
            minHeap.offer(val);
        }
        return minHeap.peek();
    }
}
