#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *cool, *hot;

	if (list == NULL || list->next == NULL)
		return (0);

	cool = list->next;
	hot = list->next->next;

	while (cool && hot && hot->next)
	{
		if (cool == hot)
			return (1);

		cool = cool->next;
		hot = hot->next->next;
	}

	return (0);
}
