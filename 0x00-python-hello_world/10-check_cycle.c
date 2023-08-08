#include "lists.h"

/**
 * check_cycle - finding a loop in a linked list
 * @list: begin with linked list
 * Return: 1 if loop 0 if fail
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && (*fast).next)
	{
		slow = (*slow).next;
		fast = (*(*fast).next).next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
