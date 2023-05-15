#include <listobject.h>
#include <object.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints info about python lists
 * @p: python lisze
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
		print("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
