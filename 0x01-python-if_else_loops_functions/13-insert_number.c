#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: singly linked list head
 * @number: number to be inserted
 *
 * Return: modified singly list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *my_node = NULL;
	listint_t *node = NULL;

	if (head != NULL)
	{
		node = malloc(sizeof(listint_t));
		if (node == NULL)
			return (node)

		node->n = number;
		my_node = *head;

		while ((my_node != NULL) && (my_node->n < number))
		{
			if ((my_node->next != NULL) && (my_node->next->n < number))
				my_node = my_node->next;
			else
				break;
		}

		if (my_node != NULL) && (my_node->n < number)
		{
			node->next = my_node->next;
			my_node->next = node;
		}
		else
		{
			node->next = *head;
			*head = node;
		}
	}
	return (node)
}
