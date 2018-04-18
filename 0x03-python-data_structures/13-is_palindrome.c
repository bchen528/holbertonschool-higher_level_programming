#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 *
 * @head: start of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	listint_t *p = NULL;
	int len = 0;
	int count = 0;

	if (*head == NULL || head == NULL)
		return (1);

	while (p != NULL)
	{
		p = p->next;
		len++;
	}

	while (*head != NULL && *head != temp)
	{
		temp = *head;
		if (*head == temp)
			return (1);
		while (count < len)
		{
			temp = temp->next;
			count++;
		}
		len = count;
		if ((*head)->n == temp->n)
			*head = (*head)->next;
		len--;
		count = 0;
	}
	if (*head == temp)
		return (1);
	return (0);
}
