#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if
 * a list is a palindrome
 * @head: head pointer to list
 * Return: 1 or 0 if palindrome
 * or not respectively
 */

int is_palindrome(listint_t **head)
{
	int size = 0;
	listint_t *node;
	int arr[1024], i, ret = 0;

	if (!head || !*head)
		return (1);
	node = *head;
	while (node)
	{
		size++;
		node = node->next;
	}
	node = *head;
	i = size - 1;
	while (node && i >= 0)
	{
		*(arr + i) = node->n;
		node = node->next;
		i--;
	}
	node = *head;
	i = 0;
	while (node)
	{
		if (node->n != arr[i])
			break;
		i++;
		node = node->next;
	}
	if (!node)
		ret = 1;
	return (ret);
}

