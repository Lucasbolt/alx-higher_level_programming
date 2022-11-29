#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if linked list has a loop
 * @list: a singly-linked list
 * Return: 0 if not, 1 if true
 */
int check_cycle(listint_t *list)
{
	listint_t *chase, *catch;

	if (list == NULL || list->next == NULL)
		return (0);

	chase = list->next;
	catch = list->next->next;

	while (chase && catch && catch->next)
	{
		if (chase == catch)
			return (1);
		chase = chase->next;
		catch = catch->next->next;
	}
	return (0);
}
