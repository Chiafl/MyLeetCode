class LRUCache {
    
    private HashMap<Integer, Node> hs;
    private Integer start;
    private Integer end;
    private int cap;

    public LRUCache(int capacity) {
        if (hs==null){
            hs = new HashMap<Integer, Node>();
        }
        cap = capacity;
    }
    
    public int get(int key) {
        if (!hs.containsKey(key)) {
            return -1;
        }
        Node n = hs.get(key);
        update(n);
        return n.val;
    }
    
    public void put(int key, int value) {
        Node ins = hs.getOrDefault(key, new Node(value));
        ins.key = key;
        ins.val = value;
        hs.put(key, ins);

        if (start==null) {
            start = key;
            end = key;
        }
        else {
            update(ins);
        }
    }
    
    private void update(Node n){     
        if (n.left!=null 
            && n.right!=null
            && hs.containsKey(start)){
            n.left.right = n.right;
            n.right.left = n.left;
        }
        updateStart(n);
        updateEnd();
    }
  
    private void updateStart(Node n){
        
        if (n.key.equals(end)){
            if (n.right!=null){
                end = n.right.key;
                n.right.left = null;
            }
        }
        if(!start.equals(n.key) && !n.key.equals(end)){
            Node prev = hs.get(start);
            start = n.key;
            prev.right = n;
            n.left = prev;
            n.right = null;
            
        }
    }
    
    private void updateEnd(){
        if (hs.size()>cap){
            Node prev = hs.get(end);
            Node n = prev.right;
            hs.remove(end);
            end = n.key;
            n.left = null;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

class Node {
    int val = 0;
    Integer key;
    Node left;
    Node right;
    Node(int val){
        this.val = val;
    }
}