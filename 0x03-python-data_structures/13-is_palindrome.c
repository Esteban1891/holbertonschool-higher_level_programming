#include "lists.h"
/**
 * is_palindrome - Checks if a linked list is palindrome
 * @head: pointer to head of list
 * Return: 1 if it's palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int array[2048];
	int nodos = 0;
	int i = 0;

	if (*head == NULL || head == NULL)
		return (1);

	while (*head != NULL)
	{
		nodos++;
		array[nodos - 1] = (*head)->n;
		*head = (*head)->next;
	}

	for (i = 0; i < nodos / 2; i++)
	{
		if (array[i] != array[nodos - i - 1])
		{
			return (0);
		}
	}
	return (1);
}
