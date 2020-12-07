#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function to determine if there is a cycle in a linked list
 * @list: linked list to check
 * Return: 0 if no cycle and 1 if cycle is present
 */

int check_cycle(listint_t *list)
{
	listint_t *test = list, *test2 = list;

	if (!list)
		return (0);

	while (test && test2 && test2->next)
	{
		test = test->next;
		test2 = test2->next->next;

		if (test == test2)
			return (1);
	}

	return (0);
}
