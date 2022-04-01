function isPrime(n) {
  if (n === 2) return true;
  if (n < 2 || n % 2 === 0) return false;
  for (let i = 3; i * i <= n; i++) if (n % i === 0) return false;
  return true;
}

console.log(isPrime(1));
console.log(isPrime(2));
console.log(isPrime(3));
console.log(isPrime(4));
console.log(isPrime(5));
console.log(isPrime(6));
