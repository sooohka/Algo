class Program {
    // This is an input class. Do not edit.
    public static class LinkedList {
        public int value;
        public LinkedList next;

        public LinkedList(int value) {
            this.value = value;
            this.next = null;
        }
    }

    public LinkedList removeDuplicatesFromLinkedList(LinkedList linkedList) {
        LinkedList cur = linkedList;
        while (cur != null) {
            LinkedList next = cur.next;
            while (next != null && cur.value == next.value) {
                next = next.next;
            }
            cur.next = next;
            cur = cur.next;
        }
        return linkedList;
    }
}
