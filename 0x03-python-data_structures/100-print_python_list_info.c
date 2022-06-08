#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about
 * Python lists
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	PyListObject *list;
	PyObject *item;
	long int i;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
