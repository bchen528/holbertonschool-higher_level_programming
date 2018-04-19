#include "lists.h"

/**
 * _strlen_recursion - returns length of a string
 * @s: string to be assessed
 * Return: length of string
 */

int _strlen_recursion(char *s)
{
	if (*s == '\0')
		return (0);
	return (_strlen_recursion(s + 1) + 1);
}

/**
 * check_palin - check if string is a palindrome
 * @s: string to be assessed
 * @start: first index
 * @end: end index
 * Return: 1 if palindrome, 0 if not palindrome
 */

int check_palin(char *s, int start, int end)
{
	if (s[start] != s[end])
		return (0);
	if (start >= end)
		return (1);
	return (check_palin(s, start + 1, end - 1));
}

/**
 * is_palin - determine if string is a palindrome
 * @s: string to be assessed
 * Return: 1 if string is palindrome and 0 if not
 */

int is_palin(char *s)
{
	int end;

	if (*s == '\0')
		return (1);
	end = _strlen_recursion(s) - 1;
	return (check_palin(s, 0, end));
}

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
	char *s;
	int numNodes = 0;
	int i = 0;

	if (*head == NULL || head == NULL)
		return (1);

	p = *head;
	while (p != NULL)
	{
		p = p->next;
		numNodes++;
	}

	s = malloc(sizeof(int) * numNodes);
	if (s == NULL)
		return (-1);

	temp = *head;

	while (temp != NULL)
	{
		s[i] = temp->n;
		temp = temp->next;
		i++;
	}

	if (is_palin(s) == 1)
	{
		free(s);
		return (1);
	}
	free(s);
	return (0);
}
