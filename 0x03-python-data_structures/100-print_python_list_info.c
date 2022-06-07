#include "Python.h"

/**
 * print_python_list_info - prints infor about python objects
 * @p: pyobject
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %d\n", Py_SIZE(p));
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i)->tp_name);
	}
}
