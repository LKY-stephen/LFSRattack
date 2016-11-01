#pragma once

#include <string>

using namespace std;

class LFSR
{
private:
	int n;
	int* reg;
	int* usedpara;
	int parasize;
	int (*filter)(int *x);
	void filterinit();
public:
	LFSR(int x);
	void getreg(string & output);
	int getnext();
};