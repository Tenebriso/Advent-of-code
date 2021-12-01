class Node {
    int data;
    Node left;
    Node right;

    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

public class BinaryTree {
    Node head;
    public BinaryTree(Node head) {
        this.head = head;
    }
     public boolean isBST() {
        return isBST(this.head, Integer.MAX_VALUE, Integer.MIN_VALUE);
    }

    private boolean isBST(Node head, int min, int max) {
        if (head == null)
            return true;
        if (head.data < min || head.data > max)
            return false;
        return isBST(head.left, min, head.data - 1) ||
                isBST(head.right, head.data + 1, max);
    }
}
