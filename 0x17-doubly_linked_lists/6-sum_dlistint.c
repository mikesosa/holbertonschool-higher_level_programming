#include "lists.h"

/**
 * sum_dlistint - Returns the sum of all elements of the list
 * @head: head node given by main
 *
 * Return: Sum
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *tmp = head;
	unsigned int count = 0;

	while (tmp)
	{
		count += tmp->n;
		tmp = tmp->next;
	}
	return (count);
}
