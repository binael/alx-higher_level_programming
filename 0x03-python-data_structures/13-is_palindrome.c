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
	int my_list[1024], c = 0, i = 0;

	if ((!*head) || (!head))
		return (1);

	my_node = *head;

	if (!my_node->next)
		return (1);

	while (my_node != NULL)
	{
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

	return (1);
}
