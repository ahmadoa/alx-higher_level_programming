#include "lists.h"

/**
 * insert_node - inserts a node in a singly linked list
 * @head: already existing elements in linked list
 * @number: number to add to the new node
 * Return: new linked list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *temp_new;

	temp_new = malloc(sizeof(listint_t));
	if (temp_new == NULL)
		return (NULL);

	temp_new->n = number;

	while (curr && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	temp_new->next = curr;
	if (prev)
		prev->next = temp_new;
	else
		*head = temp_new;
	return (temp_new);
}
