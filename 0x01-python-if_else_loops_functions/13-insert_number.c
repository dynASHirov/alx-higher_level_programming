#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *heads, *news;

	news = malloc(sizeof(listint_t));
	if (news == NULL)
		return (NULL);
	news->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*heads = new;
		return (news);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	news->next = node->next;
	node->next = new;

	return (news);
}
