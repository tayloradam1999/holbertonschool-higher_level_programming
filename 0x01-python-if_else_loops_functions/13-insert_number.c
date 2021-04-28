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
	new_node->n = number;
	if (!*head)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	old = *head;
	if (number <= old->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	trav = old->next;
	while (trav)
	{
		if (number <= trav->n)
		{
			old->next = new_node;
			new_node->next = trav;
			return (new_node);
		}
		old = trav;
		trav = trav->next;
	}
	new_node = add_noteint_end(head, number);
	return (new_node);
}
