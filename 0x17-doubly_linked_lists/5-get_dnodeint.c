#include "lists.h"

/**
 * add_dnodeint_end - Adding a node to the end of list
 * @head: head node given by main
 * @n: data to store in the new node
 *
 * Return: New node
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *tmp = head;
	unsigned int count = 0;

	while (tmp)
	{
		if (count == index)
			break;
		tmp = tmp->next;
		count++;
	}
	return (tmp);
}
