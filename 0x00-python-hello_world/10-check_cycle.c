#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if there is a loop in a linked list
 * @list: list of nodes
 *
 * Return: 1 if there is a loopk 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL;
	listint_t *fast = NULL;

	slow = list;
	fast = list->next;
	while (fast && fast->next && slow)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
