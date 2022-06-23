function sieve(n) {
  const primes = Array.from({ length: n + 1 }, () => true);

  for (let i = 2; i * i <= primes.length; i++) {
    if (primes[i]) {
      for (let j = i * i; j <= primes.length; j += i) {
        primes[j] = false;
      }
    }
  }

  for (let j = 2; j < primes.length; j++) {
    if (primes[j]) {
      console.log(j);
    }
  }
}

sieve(10);
