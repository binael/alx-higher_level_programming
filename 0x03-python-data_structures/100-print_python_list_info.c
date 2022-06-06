#include <python.h>
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
	PyObject *py_list;
	const char *list_type;
	PyListObject *object;

	object = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)object->allocated);

	for (i = 0; i < size; i++)
	{
		py_list = PyList_GetItem(p, i);
		list_type = Py_TYPE(py_list)->tp_name;
		printf("Element %d: %s\n", (int)i, list_type);
	}
}
