#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node
 * @head: linked list to inster into
 * @number: value of node to insert
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p1 = *head, *p2, *new = malloc(sizeof(listint_t));

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
		new->next = p1;
		return (new);
	}

	p2 = p1->next;

	while (p2 != NULL)
	{
		if (p2->n > number)
			break;
		p1 = p2;
		p2 = p2->next;
	}

	p1->next = new;
	new->next = p2;

	return (new);
}
