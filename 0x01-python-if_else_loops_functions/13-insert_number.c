#include "lists.h"
#include <stdlib.h>

/**
 * insrt_node - inserting a new node to be sorted
 * @ptr: pointr in the beginning of linked list
 * @numb:  n value
 * Return: new node adress or NULL if error
 */

listint_t *insrt_node(listint_t **ptr, int numb)
{
	listint_t *nv, *hold = *ptr;
	unsigned int i = 0;

	if (!(hold) || (*hold).n > numb) /*in the beginning of linked list*/
	{
		nv = malloc(sizeof(listint_t));
		if (!nv)
			return (NULL);

		(*nv).n = numb;
		(*nv).next = *ptr;

		*ptr = nv;

		return (*ptr);
	}

	while (hold)
	{
		if (!((*hold).next) || (*hold).next->n > numb)
		{
			nv = malloc(sizeof(listint_t));
			if (!nv)
				return (NULL);
			(*nv).n = numb;
			(*nv).next = (*hold).next;
			(*hold).next = nv;
			return (nv);
		}
		hold = (*hold).next;
		i++;
	}

	return (NULL);
}
