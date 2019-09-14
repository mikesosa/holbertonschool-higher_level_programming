#include "lists.h"

/**
 * free_dlistint - freeing a double linked list
 * @head: head node given by main
 *
 * Return: void
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *tmp = head;

	while (tmp)
	{
		tmp = head->next;
		free(head);
		head = tmp;
	}
}
