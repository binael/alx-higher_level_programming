#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the singly linked list
 *
 * Return: 0 - if it  is not or 1- if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *my_node;
	int *my_list, c = 0, i = 0, len = 1024;

	my_list = malloc(sizeof(int) * len);

	if (my_list == NULL)
		return (0);
	if ((!*head) || (!head))
		return (1);
	my_node = *head;

	if (!my_node->next)
		return (1);
	while (my_node != NULL)
	{
		if ((len + 1) >= i)
		{
			len = len * 2;
			my_list = realloc(my_list, sizeof(int) * len);

			if (my_list == NULL)
				return (0);
		}
		my_list[i] = my_node->n;
		my_node = my_node->next;
		i++;
	}
	i--;
	while (i >= 0 && c <= i)
	{
		if (my_list[i] != my_list[c])
			return (0);
		i--, c++;
	}
	free(my_list);
	return (1);
}
