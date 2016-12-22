#include <stdio.h>
 main()
{
	int decks;
	puts("Enter a number of decks");
	scanf("%i", &decks);
	if (decks < 1) {
		puts("That is not a valid number of decks");
	}
	printf("There are %i cards\n", (decks * 52));
}