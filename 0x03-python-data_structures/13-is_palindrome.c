#include "lists.h"
/**
 *is_palindrome - a function that checks if a linked list
 *is palindrome or not .
 *@head: the head of the linked list.
 *Return: 1 if it is a palindrome otherwise 0.
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast)
		slow = slow->next;
	slow = reverse_listint(&slow);
	fast = *head;

	while (slow)
	{
		if (fast->n != slow->n)
			return (0);
		fast = fast->next;
		slow = slow->next;
	}
	return (1);
}



/**
 *reverse_listint - a function that reverses a linked list.
 *@head: a pointer to the head of the linked list.
 *Return: a pointer to the new head node's.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next_node, *prev_node = NULL;


	if (*head == NULL)
		return (NULL);

	while (*head)
	{
		next_node = (*head)->next;
		(*head)->next = prev_node;
		prev_node = *head;
		*head = next_node;
	}
	*head = prev_node;

	return (*head);
}



