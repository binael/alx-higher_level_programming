#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * print_python_list_info - prints infor about python objects
 * @p: pyobject
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize i, size;
	PyListObject *object;

	object = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", object->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i)->tp_name);
	}
}
