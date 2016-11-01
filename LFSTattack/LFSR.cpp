#pragma once

#include "LFSR.h"

int para30[] = { 29,5,3,0 };
int para50[] = { 49,48,23,22 };
int para100[] = { 99,62 };
int initvalue[] = { 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1 };


int filter30(int *reg)
{
	return (reg[1]*reg[13]*reg[27])^(reg[13] * reg[27])^(reg[1] * reg[27])^reg[13];
}

int filter50(int *reg)
{
	return 0;
}

int filter100(int *reg)
{
	return 0;
}

void LFSR::filterinit()
{
	switch (n)
	{
	case 30:
		filter = filter30;
		break;
	case 50:
		filter = filter50;
		break;
	case 100:
		filter = filter100;
		break;
	default:
		break;
	}
}

LFSR::LFSR(int x)
{
	n = x;
	reg = new int[n];
	memcpy(reg, initvalue, n * sizeof(int));
	switch (n)
	{
	case 30:
		usedpara = para30;
		parasize = 4;
		break;
	case 50:
		usedpara = para50;
		parasize = 4;
		break;
	case 100:
		usedpara = para100;
		parasize = 2;
		break;
	default:
		usedpara = NULL;
		parasize = 0;
		break;
	}
	filterinit();
}
void LFSR::getreg(string & output)
{
	output = "";
	for (int i = 0; i < n; i++)
	{
		output += reg[i] ? '1' : '0';
	}
}


int LFSR::getnext()
{
	int temp = 0,i=0;
	for (i = 0; i < parasize; i++)
	{
		temp ^= reg[usedpara[i]];
	}
	for ( i = 0; i < n-1; i++)
	{
		reg[i] = reg[i + 1];
	}
	reg[i] = temp;
	return filter();
}

