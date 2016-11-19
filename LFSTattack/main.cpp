#pragma once
#include <iostream>
#include "LFSR.h"

#define SCAL 30
using namespace std;
int main()
{
	LFSR myLFSR=LFSR(SCAL);
	string reg;
	myLFSR.getreg(reg);
	cout << reg<<endl;
	int outputscal = 1000;
	int output = 0;
	for (int j = 0; j < outputscal;)
	{
		output=myLFSR.getnext();
		j = output ? j + 1: j;
		cout << output;
	}
	return 0;
}