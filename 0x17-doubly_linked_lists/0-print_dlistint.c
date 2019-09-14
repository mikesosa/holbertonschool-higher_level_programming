#include "lists.h"

/**
 * print_dlistint - Printing the nodes on a double linked list
 * @h: head node given by main
 *
 * Return: Ammount of nodes in the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
