#include "lists.h"

/**
 * insert_node - inserts a node in the middle of a linked list
 * @head: Start of the list
 * @number: Where to insert
 * Return: List with inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old, *trav, *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	if (!*head)
	{
		*head = node;
		node->next = NULL;
		return (node);
	}
	old = *head;
	if (number <= old->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	trav = old->next;
	while (trav)
	{
		if (number <= trav->n)
		{
			old->next = node;
			node->next = trav;
			return (node);
		}
		old = trav;
		trav = trav->next;
	}
	node = add_nodeint_end(head, number);
	return (node);
}
