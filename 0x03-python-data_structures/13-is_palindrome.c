#include "lists.h"
/**
 * is_palindrome - Checks if a linked list is palindrome
 * @head: pointer to head of list
 * Return: 1 if it's palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int *arr = NULL;
	int nodo = 0;
	int i = 0;

	if (*head == NULL)
		return (1);

	while (tmp != NULL)
	{
		nodo++;
		tmp = tmp->next;
	}

	arr = malloc(sizeof(int) * nodo);
	tmp = *head;

	while (tmp != NULL)
	{
		arr[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}

	for (i = 0; i < nodo / 2; i++)
	{
		if (arr[i] != arr[(nodo - 1) - i])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}
