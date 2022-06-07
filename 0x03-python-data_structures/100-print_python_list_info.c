#include "listobject.h"
#include "object.h"
#include <stdio.h>

/**
 * print_python_list_info - prints basic
 * onfo about python lists
 * @p: python object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	printf("%d", PyList_Size(p));
}
