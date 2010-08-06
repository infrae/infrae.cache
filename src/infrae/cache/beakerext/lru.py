from beaker.container import MemoryNamespaceManager, AbstractDictionaryNSManager
from repoze.lru import LRUCache


class LRUDict(LRUCache):
    """ Wrapper to provide partial dict access
    """
    def __setitem__(self, key, value):
        return self.put(key, value)
    def __getitem__(self, key):
        return self.get(key)


class MemoryLRUNamespaceManager(MemoryNamespaceManager):
    """ A memory namespace manager that return with LRU dicts backend
    """
    default_max_items = 10000

    def __init__(self, namespace, **kwargs):
        AbstractDictionaryNSManager.__init__(self, namespace)
        if kwargs.has_key('max_items'):
            max_items = kwargs['max_items']
        else:
            max_items = self.default_max_items
        self.dictionary = MemoryNamespaceManager.namespaces.get(
            self.namespace, LRUDict(max_items))
