// rc2021-11-19.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>


// The Python version of the code looked something like this:
// for raw_strat in itertools.product(range(3), repeat=27):
//      strat_0 = chunks(raw_strat[0:9], 3)
//      strat_1 = chunks(raw_strat[9:18], 3)
//      strat_2 = chunks(raw_strat[18:27], 3)
// where chunks(lst, n) reshapes lst into a 3-column 2D nested list.
// Each strat is a 3x3 nested list where, e.g., strat_0[l][r] is what that strategy
// says you should guess when the color of the left hat is l and the color of the
// right hat is r.
//
// This version uses r[27] instead of raw_strat and uses this formula to determine
// which cell of the array to check:

inline int to_index(int strategy, int left, int right) {
    return (9 * strategy + 3 * left + right);
}

// This is where all the work happens.
// s0, s1, s2, and s3 are the numbers (from 0 to 2) of the strategy that player
// will use.
void iterate(int s0, int s1, int s2, int s3) {
	int r[27];
	int most_successes = -1;
	// From the symmetry of the problem, r[0] must be 0 and the first nonzero
	// digit must be 1. If I hadn't found an answer, I would've tried to skip
	// some of these cases.
	for (r[0] = 0; r[0] < 1; r[0]++) {
	for (r[1] = 0; r[1] < 2; r[1]++) {
	for (r[2] = 0; r[2] < 3; r[2]++) {
	for (r[3] = 0; r[3] < 3; r[3]++) {
	for (r[4] = 0; r[4] < 3; r[4]++) {
	for (r[5] = 0; r[5] < 3; r[5]++) {
	for (r[6] = 0; r[6] < 3; r[6]++) {
	for (r[7] = 0; r[7] < 3; r[7]++) {
	for (r[8] = 0; r[8] < 3; r[8]++) {
		// This prints every 12 or so seconds on my iMac in Windows 10.
		std::cout << "Checking ";
		for (int i = 0; i < 9; i++) std::cout << r[i];
		std::cout << "...\n";
		for (r[9] = 0; r[9] < 3; r[9]++) {
		for (r[10] = 0; r[10] < 3; r[10]++) {
		for (r[11] = 0; r[11] < 3; r[11]++) {
		for (r[12] = 0; r[12] < 3; r[12]++) {
		for (r[13] = 0; r[13] < 3; r[13]++) {
		for (r[14] = 0; r[14] < 3; r[14]++) {
		for (r[15] = 0; r[15] < 3; r[15]++) {
		for (r[16] = 0; r[16] < 3; r[16]++) {
		for (r[17] = 0; r[17] < 3; r[17]++) {
		for (r[18] = 0; r[18] < 3; r[18]++) {
		for (r[19] = 0; r[19] < 3; r[19]++) {
		for (r[20] = 0; r[20] < 3; r[20]++) {
		for (r[21] = 0; r[21] < 3; r[21]++) {
		for (r[22] = 0; r[22] < 3; r[22]++) {
		for (r[23] = 0; r[23] < 3; r[23]++) {
		for (r[24] = 0; r[24] < 3; r[24]++) {
		for (r[25] = 0; r[25] < 3; r[25]++) {
		for (r[26] = 0; r[26] < 3; r[26]++) {
			// Here's our array of hats. I internally matched RYB -> 012,
			// but that's completely arbitrary. Also, I put the players in
			// counterclockwise order, so their left is the same as the left
			// in a list written left to right.
			int h[4];
			for (h[0] = 0; h[0] < 3; h[0]++) {
			for (h[1] = 0; h[1] < 3; h[1]++) {
			for (h[2] = 0; h[2] < 3; h[2]++) {
			for (h[3] = 0; h[3] < 3; h[3]++) {
				// If nobody guessed right, get out of the hat loops and continue.
				if (h[0] != r[to_index(s0, h[3], h[1])] &&
						h[1] != r[to_index(s1, h[0], h[2])] &&
						h[2] != r[to_index(s2, h[1], h[3])] &&
						h[3] != r[to_index(s3, h[2], h[0])]) {
					goto SKIP; // My first goto in a C/C++ program in 30 years!
				} // end if
			}}}} // end h-loops
			// If we've made it here, we've checked every combination of hats
			// and someone's answered properly in each one.
			// Each section of code checks who ran each strategy,
			// then prints out that strategy.
			if (s0 == 0) std::cout << "0";
			if (s1 == 0) std::cout << "1";
			if (s2 == 0) std::cout << "2";
			if (s3 == 0) std::cout << "3";
			std::cout << ": ";
			for (int i = 0; i < 9; i++) std::cout << r[i];
			std::cout << "; ";
			if (s0 == 1) std::cout << "0";
			if (s1 == 1) std::cout << "1";
			if (s2 == 1) std::cout << "2";
			if (s3 == 1) std::cout << "3";
			std::cout << ": ";
			for (int i = 9; i < 18; i++) std::cout << r[i];
			std::cout << "; ";
			if (s0 == 2) std::cout << "0";
			if (s1 == 2) std::cout << "1";
			if (s2 == 2) std::cout << "2";
			if (s3 == 2) std::cout << "3";
			std::cout << ": ";
			for (int i = 18; i < 27; i++) std::cout << r[i];
			std::cout << " = 81\n";
			SKIP: ; // Is the null operation necessary? Beats me.
		} // end innermost r-loop
		}}}}}}}}}}}}}}}}} // end r-loops until we get to the progress indicator
	}}}}}}}}} // end rest of r-loops
} // end iterate()

int main()
{
	// Like I said, all the work is in the iterate() function. I thought it would
	// be better to have the repeated strategy change the most quickly, so I used
	// those arguments instead of iterate(0, 0, 1, 2).
	iterate(0, 1, 2, 2);
}