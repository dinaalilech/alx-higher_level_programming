#include <Python.h>

void print_python_string(PyObject *);

/**
 * print_python_string - prints Python strings
 * @p: python string object
 * Return: Nothing
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
