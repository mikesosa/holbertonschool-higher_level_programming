#include "lists.h"

/**
 * delete_dnodeint_at_index - deletes node at index
 * @index: index given by main
 * @head: head node given by main
 *
 * Return: 1 if success -1 if failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *tmp;
	unsigned int count = 0;

	tmp = *head;
	if (index == 0)
	{
		if (!tmp)
			return (-1);
		if (!tmp->next)
		{
			*head = tmp->next;
			tmp->prev = NULL;
			tmp->next = NULL;
			return (-1);
		}
		*head = tmp->next;
		tmp->prev = NULL;
		tmp->next->prev = NULL;
		return (1);
	}
	while (count < index)
	{
		tmp = tmp->next;
		if (!tmp)
			return (-1);
		count++;
	}
	tmp->prev->next = tmp->next;
	tmp->next->prev = tmp->prev;
	return (1);
}
