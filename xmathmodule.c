#include <Python.h>

static PyObject *
xmath_fma(PyObject *self, PyObject *args)
{
    PyObject *ox, *oy, *oz;
    double r, x, y, z;
    if (!PyArg_UnpackTuple(args, "fma", 3, 3, &ox, &oy, &oz))
        return NULL;
    x = PyFloat_AsDouble(ox);
    y = PyFloat_AsDouble(oy);
    z = PyFloat_AsDouble(oz);
    r = fma(x, y, z);
    return PyFloat_FromDouble(r);
}

static PyMethodDef xmath_methods[] = {
    {"fma", xmath_fma, METH_VARARGS, "Fused multiply-add."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef xmathmodule = {
    PyModuleDef_HEAD_INIT,
    "fma",
    NULL,
    -1,
    xmath_methods
};

PyMODINIT_FUNC
PyInit_xmath(void)
{
    return PyModule_Create(&xmathmodule);
}
