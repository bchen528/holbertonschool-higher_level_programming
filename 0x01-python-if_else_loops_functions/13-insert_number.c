#include "lists.h"

/**
 * insert_node - inserts number into a sorted singly linked list
 *
 * @head: linked list
 * @number: value to be assigned to new node
 * Return: address of new node or NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *current = NULL;

	current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || new_node->n < current->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current->next != NULL && (current->n < new_node->n)
	       && ((current->next)->n < new_node->n))
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
