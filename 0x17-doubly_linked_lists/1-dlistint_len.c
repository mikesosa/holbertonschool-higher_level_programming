#include "lists.h"

/**
 * dlistint_len - Counting nodes on the list
 * @h: head node given by main
 *
 * Return: Ammount of nodes in the list
 */
size_t dlistint_len(const dlistint_t *h)
{
	int count = 0;

	while (h)
	{
		h = h->next;
		count++;
	}
	return (count);
}
