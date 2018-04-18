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
	int length = 0;
	int count = 0;

	if (*head == NULL || head == NULL)
		return (0);

	while (*head != NULL && *head != temp)
	{
		temp = *head;
		while (count < length)
		{
			temp = temp->next;
			count++;
		}
		length = count + 1;
		if ((*head)->n == temp->n)
			*head = (*head)->next;
		length--;
		count = 0;
	}
	if (*head == temp)
		return (1);
	return (0);
}
