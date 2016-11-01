#pragma once
#include <iostream>
#include "LFSR.h"
using namespace std;
int main()
{
	LFSR myLFSR=LFSR(30);
	string reg;
	myLFSR.getreg(reg);
	cout << reg<<endl;
	for (int j = 0; j < 10; j++)
	{
		for (int i = 0; i < 30; i++)
		{
			cout<<myLFSR.getnext();
		}
		cout <<endl;
	}
	return 0;
}