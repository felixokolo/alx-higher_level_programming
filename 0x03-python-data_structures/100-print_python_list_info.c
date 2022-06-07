#include <stdio.h>
#include <stdlib.h>
#include <Python.h>


/**
 * print_python_list_info - prints basic
 * onfo about python lists
 * @p: python object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size1, size2, i;
	PyObject *n;

	size1 = PyList_Size(p);
	size2 = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size1);
	printf("[*] Allocated = %ld\n", size2);
	for (i = 0; i < size1; i++)
	{
		n = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(n)->tp_name);
	}

}
