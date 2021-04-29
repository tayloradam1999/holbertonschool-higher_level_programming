#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - Checks to see if a linked list is a palindrome
 * @head: Double pointer to start of list
 * Return: Values of elements in list
 */

int is_palindrome(listint_t **head)
{
	size_t len = 0, i = 0;
	listint_t *mid = *head, *trav = *head, *temp;

	if (!head || !*head)
		return (1);
	while (trav->next)
		trav = trav->next, len++;
	/* Loop to middle of list */
	while (i < len / 2)
	{
		mid = mid->next;
		i++;
	}
	/* Account for linked list size being odd, skip middle node */
	if (len % 2 != 0)
		mid = mid->next;
	/* Loop through rest of list and reverse it's order */
	trav = mid;
	trav = trav->next;
	mid->next = NULL;
	while (trav)
	{
		temp = trav->next;
		trav->next = mid;
		mid = trav;
		trav = temp;
	}
	/* Compare both halfs of list */
	for (i = 0; i < (len / 2); i++)
	{
		if ((*head)->n != mid->n)
			return (0);
		*head = (*head)->next;
		mid = mid->next;
	}
	return (1);
}
