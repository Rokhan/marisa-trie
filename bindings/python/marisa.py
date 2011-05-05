# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_marisa', [dirname(__file__)])
        except ImportError:
            import _marisa
            return _marisa
        if fp is not None:
            try:
                _mod = imp.load_module('_marisa', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _marisa = swig_import_helper()
    del swig_import_helper
else:
    import _marisa
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


MARISA_OK = _marisa.MARISA_OK
MARISA_STATE_ERROR = _marisa.MARISA_STATE_ERROR
MARISA_NULL_ERROR = _marisa.MARISA_NULL_ERROR
MARISA_BOUND_ERROR = _marisa.MARISA_BOUND_ERROR
MARISA_RANGE_ERROR = _marisa.MARISA_RANGE_ERROR
MARISA_CODE_ERROR = _marisa.MARISA_CODE_ERROR
MARISA_RESET_ERROR = _marisa.MARISA_RESET_ERROR
MARISA_SIZE_ERROR = _marisa.MARISA_SIZE_ERROR
MARISA_MEMORY_ERROR = _marisa.MARISA_MEMORY_ERROR
MARISA_IO_ERROR = _marisa.MARISA_IO_ERROR
MARISA_FORMAT_ERROR = _marisa.MARISA_FORMAT_ERROR
MARISA_MIN_NUM_TRIES = _marisa.MARISA_MIN_NUM_TRIES
MARISA_MAX_NUM_TRIES = _marisa.MARISA_MAX_NUM_TRIES
MARISA_DEFAULT_NUM_TRIES = _marisa.MARISA_DEFAULT_NUM_TRIES
MARISA_HUGE_CACHE = _marisa.MARISA_HUGE_CACHE
MARISA_LARGE_CACHE = _marisa.MARISA_LARGE_CACHE
MARISA_NORMAL_CACHE = _marisa.MARISA_NORMAL_CACHE
MARISA_SMALL_CACHE = _marisa.MARISA_SMALL_CACHE
MARISA_TINY_CACHE = _marisa.MARISA_TINY_CACHE
MARISA_DEFAULT_CACHE = _marisa.MARISA_DEFAULT_CACHE
MARISA_TEXT_TAIL = _marisa.MARISA_TEXT_TAIL
MARISA_BINARY_TAIL = _marisa.MARISA_BINARY_TAIL
MARISA_DEFAULT_TAIL = _marisa.MARISA_DEFAULT_TAIL
MARISA_LABEL_ORDER = _marisa.MARISA_LABEL_ORDER
MARISA_WEIGHT_ORDER = _marisa.MARISA_WEIGHT_ORDER
MARISA_DEFAULT_ORDER = _marisa.MARISA_DEFAULT_ORDER
class Key(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Key, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Key, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def str(self): return _marisa.Key_str(self)
    def length(self): return _marisa.Key_length(self)
    def id(self): return _marisa.Key_id(self)
    def weight(self): return _marisa.Key_weight(self)
    __swig_destroy__ = _marisa.delete_Key
    __del__ = lambda self : None;
Key_swigregister = _marisa.Key_swigregister
Key_swigregister(Key)

class Query(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Query, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Query, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def str(self): return _marisa.Query_str(self)
    def length(self): return _marisa.Query_length(self)
    def key_id(self): return _marisa.Query_key_id(self)
    __swig_destroy__ = _marisa.delete_Query
    __del__ = lambda self : None;
Query_swigregister = _marisa.Query_swigregister
Query_swigregister(Query)

class Keyset(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Keyset, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Keyset, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _marisa.new_Keyset()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _marisa.delete_Keyset
    __del__ = lambda self : None;
    def push_back(self, *args): return _marisa.Keyset_push_back(self, *args)
    def key(self, *args): return _marisa.Keyset_key(self, *args)
    def num_keys(self): return _marisa.Keyset_num_keys(self)
    def empty(self): return _marisa.Keyset_empty(self)
    def size(self): return _marisa.Keyset_size(self)
    def total_length(self): return _marisa.Keyset_total_length(self)
    def reset(self): return _marisa.Keyset_reset(self)
    def clear(self): return _marisa.Keyset_clear(self)
Keyset_swigregister = _marisa.Keyset_swigregister
Keyset_swigregister(Keyset)

class Agent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Agent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Agent, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _marisa.new_Agent()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _marisa.delete_Agent
    __del__ = lambda self : None;
    def set_query(self, *args): return _marisa.Agent_set_query(self, *args)
    def key(self): return _marisa.Agent_key(self)
    def query(self): return _marisa.Agent_query(self)
Agent_swigregister = _marisa.Agent_swigregister
Agent_swigregister(Agent)

class Trie(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trie, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Trie, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _marisa.new_Trie()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _marisa.delete_Trie
    __del__ = lambda self : None;
    def build(self, *args): return _marisa.Trie_build(self, *args)
    def mmap(self, *args): return _marisa.Trie_mmap(self, *args)
    def load(self, *args): return _marisa.Trie_load(self, *args)
    def save(self, *args): return _marisa.Trie_save(self, *args)
    def lookup(self, *args): return _marisa.Trie_lookup(self, *args)
    def reverse_lookup(self, *args): return _marisa.Trie_reverse_lookup(self, *args)
    def common_prefix_search(self, *args): return _marisa.Trie_common_prefix_search(self, *args)
    def predictive_search(self, *args): return _marisa.Trie_predictive_search(self, *args)
    def num_tries(self): return _marisa.Trie_num_tries(self)
    def num_keys(self): return _marisa.Trie_num_keys(self)
    def num_nodes(self): return _marisa.Trie_num_nodes(self)
    def tail_mode(self): return _marisa.Trie_tail_mode(self)
    def node_order(self): return _marisa.Trie_node_order(self)
    def empty(self): return _marisa.Trie_empty(self)
    def size(self): return _marisa.Trie_size(self)
    def total_size(self): return _marisa.Trie_total_size(self)
    def io_size(self): return _marisa.Trie_io_size(self)
    def clear(self): return _marisa.Trie_clear(self)
Trie_swigregister = _marisa.Trie_swigregister
Trie_swigregister(Trie)


