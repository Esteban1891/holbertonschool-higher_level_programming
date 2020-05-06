#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints python the list
 * @p: a pointer to a py objetive
 * Return: is a void function
 */
void print_python_list_info(PyObject *p)
{
	long int s, a, i;
    PyObject *pyitem;

	s = PyList_Size(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", a);

	for (i = 0; i < s; i++)
	{
		pyitem = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(pyitem)->tp_name);

	}
}
