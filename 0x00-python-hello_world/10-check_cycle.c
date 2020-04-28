#include "lists.h"
/**
 * check_cycle - Check if a linked list is a cicle
 * @list: linked list
 * Return: If the linked is, 1 and if is 0
 **/
int check_cycle(listint_t *list)
{
	listint_t *low = NULL, *run = NULL;
	int count = 0;

	low = run = list;

	while (low != NULL)
	{
		low = low->next;
		count++;

		if (count == 3)
		{
			run = run->next;
			count = 0;
		}

		if (low == run)
		{
			return (1);
		}
	}
	return (0);
}
