//Currently now working with established input and output format because I'm a lazy bastard.

#include <iostream>
#include <cstring>
#include <math.h>

using namespace std;

void displayString(char thestring[], int ws, int sz);
char paintRectangle(char thestring[], int ws, int xl, int yl, int wr, int hr, int type);
char paintPixel(char thestring[], int ws, int xp, int yp, int type); // paint just one specific pixel
char paintChunk(char thestring[], int ws, int xst, int yst, int wr, int type); // paint one chunk one given row

int main()
{
	char c[] = "fnasjf0igju93mrfkj=a]klf20"; // string in question
	int sz;
	sz = strlen(c);
	int ws = 7*8; 
	int hs;
	hs = int(ceil(float(sz) / float(ws/8)));

	int xl = 0;
	int yl = 0;
	int wr = 30;
	int hr = 3;
	int type = 0;

	cout << c << endl;
	cout << "ws = " << ws << "; hs = " << hs << endl << endl;
	
	cout << "Original string" << endl;
	displayString(c, ws, sz);

	paintRectangle(c, ws, xl, yl, wr, hr, type);
	cout << endl << "Modification done" << endl << endl;

	cout << "Modified string" << endl;
	displayString(c, ws, sz);
	
	//to pause terminal
	int a = 0;
	cin >> a;
}

void displayString(char thestring[], int ws, int sz)
{
//	int sz; 
	int symbol;

	ws /= 8;
	
	//sz = strlen(thestring); // sometimes, when type is set to zero, sz equals zero. No idea why
	for(int j = 0; j < sz; j++)
	{
		for(int i = 7;  i >= 0; --i)
		{
			symbol = ((*(thestring+j) >> i) & 1);
			if (symbol == 0)
				cout << ".";
			else
				cout << "-";
		}
		if (j%ws == (ws-1))
			cout << endl;
	}
	cout << endl;
}
char paintRectangle(char thestring[], int ws, int xl, int yl, int wr, int hr, int type)
{
	int x = 0;
	int y = 0;
	for(int i = 0; i < wr; i++)
	{
		x = xl+i;
		for(int j = 0; j < hr; j++)
		{
			y = yl+j;
			*thestring = paintPixel(thestring, ws, x, y, type);
		}
	}
	return *thestring;
}

char paintPixel(char thestring[], int ws, int xp, int yp, int type)
{
	int word, posx;
	word = (ws*yp)/8 + xp/8;
	posx = 7-xp%8; // "7-" - to account for bit numbering in char

	if (type == 0)
	{
		char temp_str = *(thestring+word);
		*(thestring+word) = ~(~temp_str | 1<<posx);
	}
	else
		*(thestring+word) |= 1<<posx;

	return *thestring;
}

char paintChunk(char thestring[], int ws, int xst, int yst, int wr, int type)
{

}
