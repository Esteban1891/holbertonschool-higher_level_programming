#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node into a sorted linked list
 * @head: linked list to inster into
 * @number: value of node to insert
 *
 * Return: address of the new node, NULL if error
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pt1 = *head, *pt2, *new = malloc(sizeof(listint_t));

	new->n = number;
	new->next = NULL;

	if (p1 == NULL)
	{
		*head = new;
		return (new);
	}

	if (p1->n > number)
	{
		*head = new;
		new->next = pt1;
		return (new);
	}

	pt2 = pt1->next;

	while (pt2 != NULL)
	{
		if (pt2->n > number)
			break;
		pt1 = pt2;
		pt2 = pt2->next;
	}

	pt1->next = new;
	new->next = pt2;

	return (new);
}
