#include "lists.h"

/**
 * check_cycle - Entry point
 * @list: pointer to the list
 *
 * Description: checks if singly linked list is a cycle or not.
 * Returb: 0 if no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s = list;

	if (!list)
		return (0);

	while (1)
	{
		if (f->next != NULL && f->next->next != NULL)
		{
			f = f->next->next;
			s = s->next;

			if (f == s)
				return (1);
		}
		else
			return (0);
	}
}
