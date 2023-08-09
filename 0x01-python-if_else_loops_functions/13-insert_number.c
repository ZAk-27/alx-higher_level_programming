#include "lists.h"

/**
 * insert_node - inserts a new node so that linked list be sorted
 * @head: pointr in beginning of linked list
 * @numb: value for n
 * Return: new node adress or NULL if error
 */

listint_t *insert_node(listint_t **head, int numb)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = numb;
	new->next = NULL;

	if (!*head)
		*head = new;
	else if (current->n >= numb)
	{
		*head = new;
		new->next = current;
	}
	else if (current->next)
	{
		while (current->next)
		{
			if (current->next->n >= numb)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			if (!current->next->next)
				break;
			current = current->next;
		}
		current->next->next = new;
	}
	else
		current->next = new;
	return (new);
}
