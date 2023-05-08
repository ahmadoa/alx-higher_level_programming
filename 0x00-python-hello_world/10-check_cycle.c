#include "lists.h"

/**
 * check_cycle - checks if a linked list loops
 * @list: linked list
 * Return: 1 if linked list loops, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *lent = list;
	listint_t *rapide = list;

	if (list == NULL)
		return (0);

	while (rapide != NULL && rapide->next != NULL)
	{
		lent = lent->next;
		rapide = rapide->next;

		if (lent == rapide)
			return (1);
	}

	return (0);
}
