# RC-2021-11-19
A solution to the Riddler Classic of November 19, 2021

🟥-1, 🟨0, 🟦+1
```
sgn(L-R) 🙂  🙂 -sgn(L+R)
           ⚫
sgn(L-R) 🙂  🙂 sgn(L+R)
```
Found by brute force search of the 2\*3^27 different ways players could share 3 distinct strategies. Only using 1-2 strategies didn't work.

I found the first version of the answer 2.2% of the way through.

# Files
## [submission.md](./submission.md)
My submission for the puzzle, lightly edited and with a postscript added

## [attempts.py](./attempts.py)
My initial attempts at the problem and the code that double-checked my initial answer. Requires Python 3.10 because I used match/case clauses; they should be easy to rewrite if desired.

## [rc2021-11-19.cpp](./rc2021-11-19.cpp)
The code that solved the problem. Originally compiled with Visual Studio 2019. I think the only non-C code I used was the `inline` compiler hint and `std::cout`.

## [test-sgn.py](./test-sgn.py)
The code that tested my final version of the answer, with the colors encoded as -1, 0, and +1 instead of 0, 1, and 2.
