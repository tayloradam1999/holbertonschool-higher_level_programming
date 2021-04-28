#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * revArray - Reverses an array
 * @arr: The array to reverse
 * Return: Reversed array
 */

int *revArray(int *arr)
{
	int *newArr, len = 0, i = 0, ii = 0;

	while (arr[i])
		len++, i++;
	newArr = malloc(sizeof(int) * len);
	if (!newArr)
		return (NULL);
	ii = len - 1;
	for (i = 0; i < len; i++, ii--)
		newArr[i] = arr[ii];
	free(arr);
	return (newArr);
		
}

/**
 * listint_len - Returns the number of elements in a list
 * @h: Pointer to header
 * Return: Number of elements
 */

size_t listint_len(listint_t *h)
{
	size_t x = 0;

	if (!h)
		return (x);
	while (h->next)
	{
		x++;
		h = h->next;
	}
	x++;
	return (x);
}

/**
 * is_palindrome - Checks to see if a linked list is a palindrome
 * @head: Double pointer to start of list
 * Return: Values of elements in list
 */

int is_palindrome(listint_t **head)
{
	size_t len = listint_len(*head), i = 0;
	listint_t *mid = *head;
	int *arr1, *arr2;

	if (!head || !*head)
		return (1);
	arr1 = malloc(sizeof(int) * (len / 2));
	if (!arr1)
		return (0);
	arr2 = malloc(sizeof(int) * (len / 2));
	if (!arr2)
		return (0);
	/* Loop to middle of list and populate arr1 */
	while (i < len / 2)
	{
		arr1[i] = mid->n;
		mid = mid->next;
		i++;
	}
	/* Account for linked list size being odd, skip middle node */
	if (len % 2 != 0)
		mid = mid->next;
	/* Loop through rest of list and populate arr2 */
	i = 0;
	while (mid)
	{
		arr2[i] = mid->n;
		mid = mid->next;
		i++;
	}
	arr2 = revArray(arr2);
	/* Compare arrays */
	for (i = 0; arr1[i] && arr2[i]; i++)
	{
		if (arr1[i] != arr2[i])
		{
			free(arr1), free(arr2);
			return (0);
		}
	}
	free(arr1), free(arr2);
	return (1);
}
