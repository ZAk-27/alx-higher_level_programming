#include "lists.h"

/**
 * is_palindrome - Return 1  if palindrome, 0 if not
 * @head: linked list
 * Return: Return 1  if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *palin = *head;
	int counter = 0, a = 0, k = 0;

	if (!*head)
		return (1);

	while (current)
	{
		current = current->next;
		counter++;
	}
	current = *head;
	for (a = 1; a <= counter; a++)
	{
		for (k = a; k <= counter - a; k++)
			palin = palin->next;
		if (current->n != palin->n)
			return (0);
		current = current->next;
		palin = current;
	}
	return (1);
}
