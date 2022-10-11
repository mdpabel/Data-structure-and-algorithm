class Node {
  constructor() {
    this.children = {};
    this.isLastNode = false;
  }
}

class Trie {
  constructor() {
    this.root = new Node();
  }

  insert(str) {
    let root = this.root;
    for (const char of str) {
      if (!(char in root.children)) {
        root.children[char] = new Node();
      }
      root = root.children[char];
    }
    root.isLastNode = true;
  }

  search(str) {
    let root = this.root;
    for (const char of str) {
      if (!(char in root.children)) {
        return false;
      }
      root = root.children[char];
    }
    return root.isLastNode;
  }
}

const trie = new Trie();
trie.insert('abc');
trie.insert('hello');
const res = trie.search('hello');
console.log(res);
