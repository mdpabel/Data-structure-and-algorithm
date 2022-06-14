class Node {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class BinaryTree {
  constructor(val) {
    this.root = new Node(val);
  }

  printTree(order) {
    if (order === 'inOrder') {
      this.inOrder(this.root);
      return;
    }
    if (order === 'preOrder') {
      this.preOrder(this.root);
      return;
    }
    if (order === 'postOrder') {
      this.postOrder(this.root);
      return;
    }
    if (order === 'levelOrder') {
      this.levelOrder(this.root);
    }

    if (order === 'reverseLevelOrder') {
      this.reverseLevelOrder(this.root);
    }

    throw new Error(
      'Please check the order type, It should be (inOrder | preOrder | postOrder)'
    );
  }
  inOrder(root) {
    if (root) {
      this.inOrder(root.left);
      console.log(root.val);
      this.inOrder(root.right);
    }
  }

  preOrder(root) {
    if (root) {
      console.log(root.val);
      this.preOrder(root.left);
      this.preOrder(root.right);
    }
  }

  postOrder(root) {
    if (root) {
      this.preOrder(root.left);
      this.preOrder(root.right);
      console.log(root.val);
    }
  }

  levelOrder(root) {
    if (!root) return;

    const queue = [root];

    while (queue.length > 0) {
      const node = queue.shift();

      console.log(node.val);

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
  }

  reverseLevelOrder(root) {
    if (!root) return;

    const queue = [root];
    const stack = [];

    while (queue.length > 0) {
      const node = queue.shift();

      stack.push(node);

      if (node.right) queue.push(node.right);
      if (node.left) queue.push(node.left);
    }

    while (stack.length > 0) {
      console.log(stack.pop().val);
    }
  }

  rootToLeaf(root) {
    if (!root) return;
  }
}

const tree = new BinaryTree(1);
tree.root.left = new Node(2);
tree.root.right = new Node(3);
tree.root.left.left = new Node(4);
tree.root.left.right = new Node(5);

// tree.inOrder(tree.root);
// console.log('');
// tree.preOrder(tree.root);
// tree.printTree('preOrder');
// tree.levelOrder(tree.root);
tree.reverseLevelOrder(tree.root);
