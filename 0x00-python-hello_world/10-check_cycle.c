#include "lists.h"

/**
 * check_cycle - checks for a cycle in a singly linked list
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fir, *ace;

	if (list == NULL)
		return (0);

	ace = list;
	fir = list->next;

	if (fir == NULL)
		return (0);

	while (fir != ace)
	{
		if (fir->next == NULL || fir->next->next == NULL)
			return (0);
		ace = ace->next;
		fir = fir->next->next;
	}
	return (1);
}
