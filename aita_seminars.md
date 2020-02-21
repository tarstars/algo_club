# 2020-01-07
## Easy

* swap values of the two variables a and b
  * with a third variable t
  * with + and - operations
  * with xor operation

hometasks for Imran:
  * read about xor
  * find non-paired element of an array: in [7, 1, 5, 7, 5] it is 1
  * cipher/decipher text with xor

## Medium
* The principle of mathematical induction
* Proof that the following program calculates the sum of all elements in the array:
```python
def proof_sum(a):
  s = 0
  for v in a:
    s += v
  return s
```
 * invariant and execution points
 * Array: definition, operations, O-estimations
 * Kinds of O-estimations for cases: the best, the worst, mean, amortized
 * Build over array:
   * A Stack
   * A Queue
 * Follow-up:
   * A Stack with max_peek function
Hometask:
 * Write your own array-based Queue. Cover your class with testcases.
 
 ## Hard
  * Started to speak about https://leetcode.com/problems/cat-and-mouse/
  * first-player-win and second-player-win
  * take-away pencils game with 1-2-3 pencils to take
  
# 2020-01-14
## Medium

Four ways to determine the binomial coefficients
* Algebraic: n! / (k! * (n - k)!)
* Recurrent: c(n, 0) = c(n, n) = 1; c(n, k) = c(n - 1, k - 1) + c(n - 1, k) {Pascal's triangle}
* Combinatoric: number of ways to peek k elements from n objects
* Expansion of (1 + x) ^ n expression as sum(k, 0, n, x^k * c(n, k))


There are 12 corollaries between these 4 points.

Problems: 
* print out one line of Pascal's triangle
* whether it is possible to construct queue using stacks objects ?
* construct stack with quick access to the maximal element in stack
* construct queue with quick access to the maximal element in queue


Cat and mouse.
