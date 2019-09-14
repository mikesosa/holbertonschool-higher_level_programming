#include "lists.h"

/**
 * add_dnodeint_end - Adding a node to the end of list
 * @head: head node given by main
 * @n: data to store in the new node
 *
 * Return: New node
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new;
	dlistint_t *tmp;

	new = malloc(sizeof(dlistint_t));/*Space for new node*/
	if (new == NULL)/*If malloc fails*/
		return (NULL);
	tmp = *head;/*Copy of head*/
	if (!tmp)/*Addind first node in case head is Null*/
	{
		new->n = n;
		new->prev = tmp;
		new->next = NULL;
		*head = new;
		return (new);
	}
	while (tmp->next)/*If there is a node already, move tmp before Null*/
		tmp = tmp->next;
	tmp->next = new;
	new->n = n;
	new->prev = tmp;
	new->next = NULL;
	return (new);
}
