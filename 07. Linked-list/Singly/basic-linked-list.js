class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const list = new Node(1);
list.next = new Node(2);
list.next.next = new Node(3);
list.next.next.next = new Node(4);

console.log(list);
