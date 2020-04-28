#include "lists.h"
/**
 * check_cycle - Check if a linked list is a cicle
 * @list: linked list
 * Return: If the linked is, 1 and if is 0
 **/
int check_cycle(listint_t *list)
{
	listint_t *low, *run;

	low = run = list;
	while (low != NULL && run != NULL && run->next != NULL)
	{
		low = low->next;
		run = run->next->next;

		if (low == run)
			return (1);
	}

	return (0);
}
