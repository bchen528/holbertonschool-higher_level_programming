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

	if (list == NULL)
		return (0);

	current = list;
	temp = list->next;

	while (temp != NULL && temp->next != NULL)
	{
		if (temp == current)
			return (1);
		current = current->next;
		temp = (temp->next)->next;
	}
	return (0);
}
