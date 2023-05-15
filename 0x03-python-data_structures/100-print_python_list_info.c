#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	int i = 0;
	long int length = PyList_Size(p);
	PyListObject *elements = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", elements->allocated);
	while (i < length)
	{
		print("Element %i: %s\n", i, Py_TYPE(elements->ob_item[i])->tp_name);
		i++;
	}
}
