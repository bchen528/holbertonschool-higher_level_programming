#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = NULL;
	listint_t *temp = NULL;

	current = list;
	temp = current->next;

	while (temp->next != NULL)
	{
		if (&((temp->next)->n) == &(current->n))
			return (1);
		current = current->next;
		temp = temp->next;
	}
	return (0);
}
