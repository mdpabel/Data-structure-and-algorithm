/**
 1. HashTable
 2. hash_function
 3. set
 4. get
 5. values
 6. keys
 7. delete
 */

class HashTable {
  constructor(size = 5) {
    this.table = new Array(size);
  }

  // HASH_FUNCTION
  _hash(key) {
    let total = 0;
    const PRIME_NUMBER = 17;
    for (let i = 0; i < Math.min(key.length, 30); i++) {
      total += key.charCodeAt(i) - 96;
    }
    const id = (total * PRIME_NUMBER) % this.table.length;
    return id;
  }

  // SET
  set(key, value) {
    const index = this._hash(key);
    if (!this.table[index]) {
      this.table[index] = [];
    }
    this.table[index].push([key, value]);
  }

  // GET
  get(key) {
    const index = this._hash(key);
    if (this.table[index]) {
      for (let i = 0; i < this.table[index].length; i++) {
        if (this.table[index][i][0] === key) {
          return this.table[index][i][1];
        }
      }
      return undefined;
    }
  }

  // KEYS
  keys() {
    const keysArr = [];
    for (let i = 0; i < this.table.length; i++) {
      for (let j = 0; j < this.table[i].length; j++) {
        keysArr.push(this.table[i][j][0]);
      }
    }
    console.log(keysArr);
  }

  // VALUES

  // DELETE
}

const hash = new HashTable();
hash.set("a", 1);
hash.set("b", 2);
hash.set("c", 3);
hash.set("d", 4);
hash.set("e", 5);
hash.set("f", 6);
hash.set("g", 7);

const res = hash.get("e");

hash.keys();

console.log(res);
