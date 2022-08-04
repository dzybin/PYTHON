#include <stdio.h>

int	main()
{
	int	n;

	n = 3;
	while(n = n-1 && n != 0)
	{
		n = n * 3;
	}
	printf("%d", n);
	return(n);
}
