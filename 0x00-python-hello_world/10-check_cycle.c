#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle
 * @list: A singly linked list
 *
 * Return: 0 - no cycle, 1 - A cycle exists
 */

int check_cycle(listint_t *list)
{
	listint_t *f_list;
	listint_t *s_list;

	if (list == NULL || list->next == NULL)
		return (0);

	f_list = f_list->next;
	s_list = s_list->next->next;

	while (f_list && s_list && s_list->next)
	{
		if (f_list == s_list)
			return (1);

		f_list = f_list->next;
		s_list = s_list->next->next;
	}

	return (0);
}
