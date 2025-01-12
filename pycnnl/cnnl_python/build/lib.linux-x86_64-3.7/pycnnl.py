# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pycnnl
else:
    import _pycnnl

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pycnnl.delete_SwigPyIterator

    def value(self):
        return _pycnnl.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pycnnl.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pycnnl.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pycnnl.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pycnnl.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pycnnl.SwigPyIterator_copy(self)

    def next(self):
        return _pycnnl.SwigPyIterator_next(self)

    def __next__(self):
        return _pycnnl.SwigPyIterator___next__(self)

    def previous(self):
        return _pycnnl.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pycnnl.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pycnnl.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pycnnl.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pycnnl.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pycnnl.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pycnnl.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pycnnl.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _pycnnl:
_pycnnl.SwigPyIterator_swigregister(SwigPyIterator)
class FloatVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _pycnnl.FloatVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pycnnl.FloatVector___nonzero__(self)

    def __bool__(self):
        return _pycnnl.FloatVector___bool__(self)

    def __len__(self):
        return _pycnnl.FloatVector___len__(self)

    def __getslice__(self, i, j):
        return _pycnnl.FloatVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pycnnl.FloatVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pycnnl.FloatVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pycnnl.FloatVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pycnnl.FloatVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pycnnl.FloatVector___setitem__(self, *args)

    def pop(self):
        return _pycnnl.FloatVector_pop(self)

    def append(self, x):
        return _pycnnl.FloatVector_append(self, x)

    def empty(self):
        return _pycnnl.FloatVector_empty(self)

    def size(self):
        return _pycnnl.FloatVector_size(self)

    def swap(self, v):
        return _pycnnl.FloatVector_swap(self, v)

    def begin(self):
        return _pycnnl.FloatVector_begin(self)

    def end(self):
        return _pycnnl.FloatVector_end(self)

    def rbegin(self):
        return _pycnnl.FloatVector_rbegin(self)

    def rend(self):
        return _pycnnl.FloatVector_rend(self)

    def clear(self):
        return _pycnnl.FloatVector_clear(self)

    def get_allocator(self):
        return _pycnnl.FloatVector_get_allocator(self)

    def pop_back(self):
        return _pycnnl.FloatVector_pop_back(self)

    def erase(self, *args):
        return _pycnnl.FloatVector_erase(self, *args)

    def __init__(self, *args):
        _pycnnl.FloatVector_swiginit(self, _pycnnl.new_FloatVector(*args))

    def push_back(self, x):
        return _pycnnl.FloatVector_push_back(self, x)

    def front(self):
        return _pycnnl.FloatVector_front(self)

    def back(self):
        return _pycnnl.FloatVector_back(self)

    def assign(self, n, x):
        return _pycnnl.FloatVector_assign(self, n, x)

    def resize(self, *args):
        return _pycnnl.FloatVector_resize(self, *args)

    def insert(self, *args):
        return _pycnnl.FloatVector_insert(self, *args)

    def reserve(self, n):
        return _pycnnl.FloatVector_reserve(self, n)

    def capacity(self):
        return _pycnnl.FloatVector_capacity(self)
    __swig_destroy__ = _pycnnl.delete_FloatVector

# Register FloatVector in _pycnnl:
_pycnnl.FloatVector_swigregister(FloatVector)
class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _pycnnl.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pycnnl.IntVector___nonzero__(self)

    def __bool__(self):
        return _pycnnl.IntVector___bool__(self)

    def __len__(self):
        return _pycnnl.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _pycnnl.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pycnnl.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pycnnl.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pycnnl.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pycnnl.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pycnnl.IntVector___setitem__(self, *args)

    def pop(self):
        return _pycnnl.IntVector_pop(self)

    def append(self, x):
        return _pycnnl.IntVector_append(self, x)

    def empty(self):
        return _pycnnl.IntVector_empty(self)

    def size(self):
        return _pycnnl.IntVector_size(self)

    def swap(self, v):
        return _pycnnl.IntVector_swap(self, v)

    def begin(self):
        return _pycnnl.IntVector_begin(self)

    def end(self):
        return _pycnnl.IntVector_end(self)

    def rbegin(self):
        return _pycnnl.IntVector_rbegin(self)

    def rend(self):
        return _pycnnl.IntVector_rend(self)

    def clear(self):
        return _pycnnl.IntVector_clear(self)

    def get_allocator(self):
        return _pycnnl.IntVector_get_allocator(self)

    def pop_back(self):
        return _pycnnl.IntVector_pop_back(self)

    def erase(self, *args):
        return _pycnnl.IntVector_erase(self, *args)

    def __init__(self, *args):
        _pycnnl.IntVector_swiginit(self, _pycnnl.new_IntVector(*args))

    def push_back(self, x):
        return _pycnnl.IntVector_push_back(self, x)

    def front(self):
        return _pycnnl.IntVector_front(self)

    def back(self):
        return _pycnnl.IntVector_back(self)

    def assign(self, n, x):
        return _pycnnl.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _pycnnl.IntVector_resize(self, *args)

    def insert(self, *args):
        return _pycnnl.IntVector_insert(self, *args)

    def reserve(self, n):
        return _pycnnl.IntVector_reserve(self, n)

    def capacity(self):
        return _pycnnl.IntVector_capacity(self)
    __swig_destroy__ = _pycnnl.delete_IntVector

# Register IntVector in _pycnnl:
_pycnnl.IntVector_swigregister(IntVector)
class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _pycnnl.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pycnnl.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _pycnnl.DoubleVector___bool__(self)

    def __len__(self):
        return _pycnnl.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _pycnnl.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pycnnl.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pycnnl.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pycnnl.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pycnnl.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pycnnl.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _pycnnl.DoubleVector_pop(self)

    def append(self, x):
        return _pycnnl.DoubleVector_append(self, x)

    def empty(self):
        return _pycnnl.DoubleVector_empty(self)

    def size(self):
        return _pycnnl.DoubleVector_size(self)

    def swap(self, v):
        return _pycnnl.DoubleVector_swap(self, v)

    def begin(self):
        return _pycnnl.DoubleVector_begin(self)

    def end(self):
        return _pycnnl.DoubleVector_end(self)

    def rbegin(self):
        return _pycnnl.DoubleVector_rbegin(self)

    def rend(self):
        return _pycnnl.DoubleVector_rend(self)

    def clear(self):
        return _pycnnl.DoubleVector_clear(self)

    def get_allocator(self):
        return _pycnnl.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _pycnnl.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _pycnnl.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _pycnnl.DoubleVector_swiginit(self, _pycnnl.new_DoubleVector(*args))

    def push_back(self, x):
        return _pycnnl.DoubleVector_push_back(self, x)

    def front(self):
        return _pycnnl.DoubleVector_front(self)

    def back(self):
        return _pycnnl.DoubleVector_back(self)

    def assign(self, n, x):
        return _pycnnl.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _pycnnl.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _pycnnl.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _pycnnl.DoubleVector_reserve(self, n)

    def capacity(self):
        return _pycnnl.DoubleVector_capacity(self)
    __swig_destroy__ = _pycnnl.delete_DoubleVector

# Register DoubleVector in _pycnnl:
_pycnnl.DoubleVector_swigregister(DoubleVector)
class FloatVector2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _pycnnl.FloatVector2_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pycnnl.FloatVector2___nonzero__(self)

    def __bool__(self):
        return _pycnnl.FloatVector2___bool__(self)

    def __len__(self):
        return _pycnnl.FloatVector2___len__(self)

    def __getslice__(self, i, j):
        return _pycnnl.FloatVector2___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pycnnl.FloatVector2___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pycnnl.FloatVector2___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pycnnl.FloatVector2___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pycnnl.FloatVector2___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pycnnl.FloatVector2___setitem__(self, *args)

    def pop(self):
        return _pycnnl.FloatVector2_pop(self)

    def append(self, x):
        return _pycnnl.FloatVector2_append(self, x)

    def empty(self):
        return _pycnnl.FloatVector2_empty(self)

    def size(self):
        return _pycnnl.FloatVector2_size(self)

    def swap(self, v):
        return _pycnnl.FloatVector2_swap(self, v)

    def begin(self):
        return _pycnnl.FloatVector2_begin(self)

    def end(self):
        return _pycnnl.FloatVector2_end(self)

    def rbegin(self):
        return _pycnnl.FloatVector2_rbegin(self)

    def rend(self):
        return _pycnnl.FloatVector2_rend(self)

    def clear(self):
        return _pycnnl.FloatVector2_clear(self)

    def get_allocator(self):
        return _pycnnl.FloatVector2_get_allocator(self)

    def pop_back(self):
        return _pycnnl.FloatVector2_pop_back(self)

    def erase(self, *args):
        return _pycnnl.FloatVector2_erase(self, *args)

    def __init__(self, *args):
        _pycnnl.FloatVector2_swiginit(self, _pycnnl.new_FloatVector2(*args))

    def push_back(self, x):
        return _pycnnl.FloatVector2_push_back(self, x)

    def front(self):
        return _pycnnl.FloatVector2_front(self)

    def back(self):
        return _pycnnl.FloatVector2_back(self)

    def assign(self, n, x):
        return _pycnnl.FloatVector2_assign(self, n, x)

    def resize(self, *args):
        return _pycnnl.FloatVector2_resize(self, *args)

    def insert(self, *args):
        return _pycnnl.FloatVector2_insert(self, *args)

    def reserve(self, n):
        return _pycnnl.FloatVector2_reserve(self, n)

    def capacity(self):
        return _pycnnl.FloatVector2_capacity(self)
    __swig_destroy__ = _pycnnl.delete_FloatVector2

# Register FloatVector2 in _pycnnl:
_pycnnl.FloatVector2_swigregister(FloatVector2)
class IntVector2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _pycnnl.IntVector2_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pycnnl.IntVector2___nonzero__(self)

    def __bool__(self):
        return _pycnnl.IntVector2___bool__(self)

    def __len__(self):
        return _pycnnl.IntVector2___len__(self)

    def __getslice__(self, i, j):
        return _pycnnl.IntVector2___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pycnnl.IntVector2___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pycnnl.IntVector2___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pycnnl.IntVector2___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pycnnl.IntVector2___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pycnnl.IntVector2___setitem__(self, *args)

    def pop(self):
        return _pycnnl.IntVector2_pop(self)

    def append(self, x):
        return _pycnnl.IntVector2_append(self, x)

    def empty(self):
        return _pycnnl.IntVector2_empty(self)

    def size(self):
        return _pycnnl.IntVector2_size(self)

    def swap(self, v):
        return _pycnnl.IntVector2_swap(self, v)

    def begin(self):
        return _pycnnl.IntVector2_begin(self)

    def end(self):
        return _pycnnl.IntVector2_end(self)

    def rbegin(self):
        return _pycnnl.IntVector2_rbegin(self)

    def rend(self):
        return _pycnnl.IntVector2_rend(self)

    def clear(self):
        return _pycnnl.IntVector2_clear(self)

    def get_allocator(self):
        return _pycnnl.IntVector2_get_allocator(self)

    def pop_back(self):
        return _pycnnl.IntVector2_pop_back(self)

    def erase(self, *args):
        return _pycnnl.IntVector2_erase(self, *args)

    def __init__(self, *args):
        _pycnnl.IntVector2_swiginit(self, _pycnnl.new_IntVector2(*args))

    def push_back(self, x):
        return _pycnnl.IntVector2_push_back(self, x)

    def front(self):
        return _pycnnl.IntVector2_front(self)

    def back(self):
        return _pycnnl.IntVector2_back(self)

    def assign(self, n, x):
        return _pycnnl.IntVector2_assign(self, n, x)

    def resize(self, *args):
        return _pycnnl.IntVector2_resize(self, *args)

    def insert(self, *args):
        return _pycnnl.IntVector2_insert(self, *args)

    def reserve(self, n):
        return _pycnnl.IntVector2_reserve(self, n)

    def capacity(self):
        return _pycnnl.IntVector2_capacity(self)
    __swig_destroy__ = _pycnnl.delete_IntVector2

# Register IntVector2 in _pycnnl:
_pycnnl.IntVector2_swigregister(IntVector2)
class DoubleVector2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _pycnnl.DoubleVector2_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pycnnl.DoubleVector2___nonzero__(self)

    def __bool__(self):
        return _pycnnl.DoubleVector2___bool__(self)

    def __len__(self):
        return _pycnnl.DoubleVector2___len__(self)

    def __getslice__(self, i, j):
        return _pycnnl.DoubleVector2___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pycnnl.DoubleVector2___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pycnnl.DoubleVector2___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pycnnl.DoubleVector2___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pycnnl.DoubleVector2___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pycnnl.DoubleVector2___setitem__(self, *args)

    def pop(self):
        return _pycnnl.DoubleVector2_pop(self)

    def append(self, x):
        return _pycnnl.DoubleVector2_append(self, x)

    def empty(self):
        return _pycnnl.DoubleVector2_empty(self)

    def size(self):
        return _pycnnl.DoubleVector2_size(self)

    def swap(self, v):
        return _pycnnl.DoubleVector2_swap(self, v)

    def begin(self):
        return _pycnnl.DoubleVector2_begin(self)

    def end(self):
        return _pycnnl.DoubleVector2_end(self)

    def rbegin(self):
        return _pycnnl.DoubleVector2_rbegin(self)

    def rend(self):
        return _pycnnl.DoubleVector2_rend(self)

    def clear(self):
        return _pycnnl.DoubleVector2_clear(self)

    def get_allocator(self):
        return _pycnnl.DoubleVector2_get_allocator(self)

    def pop_back(self):
        return _pycnnl.DoubleVector2_pop_back(self)

    def erase(self, *args):
        return _pycnnl.DoubleVector2_erase(self, *args)

    def __init__(self, *args):
        _pycnnl.DoubleVector2_swiginit(self, _pycnnl.new_DoubleVector2(*args))

    def push_back(self, x):
        return _pycnnl.DoubleVector2_push_back(self, x)

    def front(self):
        return _pycnnl.DoubleVector2_front(self)

    def back(self):
        return _pycnnl.DoubleVector2_back(self)

    def assign(self, n, x):
        return _pycnnl.DoubleVector2_assign(self, n, x)

    def resize(self, *args):
        return _pycnnl.DoubleVector2_resize(self, *args)

    def insert(self, *args):
        return _pycnnl.DoubleVector2_insert(self, *args)

    def reserve(self, n):
        return _pycnnl.DoubleVector2_reserve(self, n)

    def capacity(self):
        return _pycnnl.DoubleVector2_capacity(self)
    __swig_destroy__ = _pycnnl.delete_DoubleVector2

# Register DoubleVector2 in _pycnnl:
_pycnnl.DoubleVector2_swigregister(DoubleVector2)
class Layer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    layer = property(_pycnnl.Layer_layer_get, _pycnnl.Layer_layer_set)
    name = property(_pycnnl.Layer_name_get, _pycnnl.Layer_name_set)
    type = property(_pycnnl.Layer_type_get, _pycnnl.Layer_type_set)
    isParamLoaded = property(_pycnnl.Layer_isParamLoaded_get, _pycnnl.Layer_isParamLoaded_set)

    def __init__(self, layer, name, type, is_param_loaded):
        _pycnnl.Layer_swiginit(self, _pycnnl.new_Layer(layer, name, type, is_param_loaded))
    __swig_destroy__ = _pycnnl.delete_Layer

# Register Layer in _pycnnl:
_pycnnl.Layer_swigregister(Layer)
class CnnlNet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _pycnnl.CnnlNet_swiginit(self, _pycnnl.new_CnnlNet())
    __swig_destroy__ = _pycnnl.delete_CnnlNet

    def setInputShape(self, *args):
        return _pycnnl.CnnlNet_setInputShape(self, *args)

    def setOutputShape(self, *args):
        return _pycnnl.CnnlNet_setOutputShape(self, *args)

    def createConvLayer(self, layer_name, input_shape, out_channel, kernel_size, stride, dilation, pad):
        return _pycnnl.CnnlNet_createConvLayer(self, layer_name, input_shape, out_channel, kernel_size, stride, dilation, pad)

    def createMlpLayer(self, layer_name, input_shape, weight_shape, output_shape):
        return _pycnnl.CnnlNet_createMlpLayer(self, layer_name, input_shape, weight_shape, output_shape)

    def createReLuLayer(self, layer_name):
        return _pycnnl.CnnlNet_createReLuLayer(self, layer_name)

    def createSoftmaxLayer(self, layer_name, input_shape, axis):
        return _pycnnl.CnnlNet_createSoftmaxLayer(self, layer_name, input_shape, axis)

    def createPoolingLayer(self, layer_name, input_shape, kernel_size, stride):
        return _pycnnl.CnnlNet_createPoolingLayer(self, layer_name, input_shape, kernel_size, stride)

    def setInputData(self, data):
        return _pycnnl.CnnlNet_setInputData(self, data)

    def forward(self):
        return _pycnnl.CnnlNet_forward(self)

    def getOutputData(self):
        return _pycnnl.CnnlNet_getOutputData(self)

    def loadParams(self, layer_id, filter_data, bias_data):
        return _pycnnl.CnnlNet_loadParams(self, layer_id, filter_data, bias_data)

    def size(self):
        return _pycnnl.CnnlNet_size(self)

    def getLayerName(self, layer_id):
        return _pycnnl.CnnlNet_getLayerName(self, layer_id)

    def needToBeQuantized(self, layer_id):
        return _pycnnl.CnnlNet_needToBeQuantized(self, layer_id)

# Register CnnlNet in _pycnnl:
_pycnnl.CnnlNet_swigregister(CnnlNet)
OPT_LEN = _pycnnl.OPT_LEN
CAST = _pycnnl.CAST
CONVOLUTION = _pycnnl.CONVOLUTION
LRN = _pycnnl.LRN
MLP = _pycnnl.MLP
NORMALIZE = _pycnnl.NORMALIZE
RELU = _pycnnl.RELU
SOFTMAX = _pycnnl.SOFTMAX
POOL = _pycnnl.POOL
FLATTEN = _pycnnl.FLATTEN
class QuantParam(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    position = property(_pycnnl.QuantParam_position_get, _pycnnl.QuantParam_position_set)
    scale = property(_pycnnl.QuantParam_scale_get, _pycnnl.QuantParam_scale_set)

    def __init__(self, *args):
        _pycnnl.QuantParam_swiginit(self, _pycnnl.new_QuantParam(*args))
    __swig_destroy__ = _pycnnl.delete_QuantParam

# Register QuantParam in _pycnnl:
_pycnnl.QuantParam_swigregister(QuantParam)
class QuantTool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def getQuantParam(self, input_data, layer_name):
        return _pycnnl.QuantTool_getQuantParam(self, input_data, layer_name)

    def __init__(self):
        _pycnnl.QuantTool_swiginit(self, _pycnnl.new_QuantTool())
    __swig_destroy__ = _pycnnl.delete_QuantTool

# Register QuantTool in _pycnnl:
_pycnnl.QuantTool_swigregister(QuantTool)
class Kernel(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    kh = property(_pycnnl.Kernel_kh_get, _pycnnl.Kernel_kh_set)
    kw = property(_pycnnl.Kernel_kw_get, _pycnnl.Kernel_kw_set)
    sh = property(_pycnnl.Kernel_sh_get, _pycnnl.Kernel_sh_set)
    sw = property(_pycnnl.Kernel_sw_get, _pycnnl.Kernel_sw_set)
    dh = property(_pycnnl.Kernel_dh_get, _pycnnl.Kernel_dh_set)
    dw = property(_pycnnl.Kernel_dw_get, _pycnnl.Kernel_dw_set)

    def __init__(self):
        _pycnnl.Kernel_swiginit(self, _pycnnl.new_Kernel())
    __swig_destroy__ = _pycnnl.delete_Kernel

# Register Kernel in _pycnnl:
_pycnnl.Kernel_swigregister(Kernel)
class Shape2D(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    n = property(_pycnnl.Shape2D_n_get, _pycnnl.Shape2D_n_set)
    c = property(_pycnnl.Shape2D_c_get, _pycnnl.Shape2D_c_set)
    h = property(_pycnnl.Shape2D_h_get, _pycnnl.Shape2D_h_set)
    w = property(_pycnnl.Shape2D_w_get, _pycnnl.Shape2D_w_set)

    def size(self):
        return _pycnnl.Shape2D_size(self)

    def __init__(self):
        _pycnnl.Shape2D_swiginit(self, _pycnnl.new_Shape2D())
    __swig_destroy__ = _pycnnl.delete_Shape2D

# Register Shape2D in _pycnnl:
_pycnnl.Shape2D_swigregister(Shape2D)
class Pad(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    pt = property(_pycnnl.Pad_pt_get, _pycnnl.Pad_pt_set)
    pb = property(_pycnnl.Pad_pb_get, _pycnnl.Pad_pb_set)
    pl = property(_pycnnl.Pad_pl_get, _pycnnl.Pad_pl_set)
    pr = property(_pycnnl.Pad_pr_get, _pycnnl.Pad_pr_set)

    def __init__(self):
        _pycnnl.Pad_swiginit(self, _pycnnl.new_Pad())
    __swig_destroy__ = _pycnnl.delete_Pad

# Register Pad in _pycnnl:
_pycnnl.Pad_swigregister(Pad)
class DataType(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    input_dtype = property(_pycnnl.DataType_input_dtype_get, _pycnnl.DataType_input_dtype_set)
    weight_dtype = property(_pycnnl.DataType_weight_dtype_get, _pycnnl.DataType_weight_dtype_set)
    output_dtype = property(_pycnnl.DataType_output_dtype_get, _pycnnl.DataType_output_dtype_set)
    layout = property(_pycnnl.DataType_layout_get, _pycnnl.DataType_layout_set)

    def __init__(self):
        _pycnnl.DataType_swiginit(self, _pycnnl.new_DataType())
    __swig_destroy__ = _pycnnl.delete_DataType

# Register DataType in _pycnnl:
_pycnnl.DataType_swigregister(DataType)
class ShapeParam(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    input = property(_pycnnl.ShapeParam_input_get, _pycnnl.ShapeParam_input_set)
    weight = property(_pycnnl.ShapeParam_weight_get, _pycnnl.ShapeParam_weight_set)
    output = property(_pycnnl.ShapeParam_output_get, _pycnnl.ShapeParam_output_set)
    bias = property(_pycnnl.ShapeParam_bias_get, _pycnnl.ShapeParam_bias_set)
    kernel = property(_pycnnl.ShapeParam_kernel_get, _pycnnl.ShapeParam_kernel_set)
    pad = property(_pycnnl.ShapeParam_pad_get, _pycnnl.ShapeParam_pad_set)
    datainfo = property(_pycnnl.ShapeParam_datainfo_get, _pycnnl.ShapeParam_datainfo_set)
    has_bias = property(_pycnnl.ShapeParam_has_bias_get, _pycnnl.ShapeParam_has_bias_set)
    group_count = property(_pycnnl.ShapeParam_group_count_get, _pycnnl.ShapeParam_group_count_set)

    def __init__(self):
        _pycnnl.ShapeParam_swiginit(self, _pycnnl.new_ShapeParam())
    __swig_destroy__ = _pycnnl.delete_ShapeParam

# Register ShapeParam in _pycnnl:
_pycnnl.ShapeParam_swigregister(ShapeParam)
class DataAddress(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    cpu_data = property(_pycnnl.DataAddress_cpu_data_get, _pycnnl.DataAddress_cpu_data_set)
    fp_data = property(_pycnnl.DataAddress_fp_data_get, _pycnnl.DataAddress_fp_data_set)
    host = property(_pycnnl.DataAddress_host_get, _pycnnl.DataAddress_host_set)
    device = property(_pycnnl.DataAddress_device_get, _pycnnl.DataAddress_device_set)
    mlu_size = property(_pycnnl.DataAddress_mlu_size_get, _pycnnl.DataAddress_mlu_size_set)
    fp_size = property(_pycnnl.DataAddress_fp_size_get, _pycnnl.DataAddress_fp_size_set)

    def __init__(self):
        _pycnnl.DataAddress_swiginit(self, _pycnnl.new_DataAddress())
    __swig_destroy__ = _pycnnl.delete_DataAddress

# Register DataAddress in _pycnnl:
_pycnnl.DataAddress_swigregister(DataAddress)
class HostTimer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    t0 = property(_pycnnl.HostTimer_t0_get, _pycnnl.HostTimer_t0_set)
    t1 = property(_pycnnl.HostTimer_t1_get, _pycnnl.HostTimer_t1_set)
    tv_nsec = property(_pycnnl.HostTimer_tv_nsec_get, _pycnnl.HostTimer_tv_nsec_set)
    tv_sec = property(_pycnnl.HostTimer_tv_sec_get, _pycnnl.HostTimer_tv_sec_set)
    tv_usec = property(_pycnnl.HostTimer_tv_usec_get, _pycnnl.HostTimer_tv_usec_set)

    def start(self):
        return _pycnnl.HostTimer_start(self)

    def stop(self):
        return _pycnnl.HostTimer_stop(self)

    def __init__(self):
        _pycnnl.HostTimer_swiginit(self, _pycnnl.new_HostTimer())
    __swig_destroy__ = _pycnnl.delete_HostTimer

# Register HostTimer in _pycnnl:
_pycnnl.HostTimer_swigregister(HostTimer)

def initDevice(dev, queue, handle):
    return _pycnnl.initDevice(dev, queue, handle)

def dataSize(dtype):
    return _pycnnl.dataSize(dtype)

def convertCnnlDtypeToCnrt(dtype):
    return _pycnnl.convertCnnlDtypeToCnrt(dtype)

def getPosition(input, num, datatype, position):
    return _pycnnl.getPosition(input, num, datatype, position)

def getPositionAndScale(input, size, dtype, pos, scale):
    return _pycnnl.getPositionAndScale(input, size, dtype, pos, scale)

def castData(src_data, src_dtype, dst_data, dst_dtype, dequantify_data, quant_mode, size, pos, scale, offset):
    return _pycnnl.castData(src_data, src_dtype, dst_data, dst_dtype, dequantify_data, quant_mode, size, pos, scale, offset)

def parserParam(argc, argv, param):
    return _pycnnl.parserParam(argc, argv, param)

def setTensorDesc(desc, shape, dtype, layout):
    return _pycnnl.setTensorDesc(desc, shape, dtype, layout)

def mallocDataRandf(size, low, hight):
    return _pycnnl.mallocDataRandf(size, low, hight)

def saveDataToFile(file, data, count):
    return _pycnnl.saveDataToFile(file, data, count)

def saveHexDataToFile(file, data, dtype, count):
    return _pycnnl.saveHexDataToFile(file, data, dtype, count)

def computeDiff1(cpu_result, mlu_result, count):
    return _pycnnl.computeDiff1(cpu_result, mlu_result, count)

def computeDiff2(cpu_result, mlu_result, count):
    return _pycnnl.computeDiff2(cpu_result, mlu_result, count)

