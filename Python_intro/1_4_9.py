root = { 'global' : {} }

def searchNamespace(node, keyword):
    for name in node:
        if type(node[name]) is dict:
            if name == keyword:
                return node[keyword]
    for name in node:
        if type(node[name]) is dict:
            result = searchNamespace(node[name], keyword)
            if result is None:
                continue
            else:
                return result
    return None

def create(namespace, parent):
    parentNamespace = searchNamespace(root, parent)
    parentNamespace[namespace] = {}

# добавить в пространство <namespace> переменную <var>
def add(namespace, var):
    targetNamespace = searchNamespace(root, namespace)
    targetNamespace[var] = None

def searchVar(node, keyword, nodeName):
    for name in node:
        if node[name] is None:
            if name == keyword:
                return nodeName
    return None

def searchParent(node, child, nodeName):
    for name in node:
        if node[name] is child:
            return nodeName
        elif type(node[name]) is dict:
            result = searchParent(node[name], child, name)
            if result is None:
                continue
            else:
                return result
    return None

# получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не сущет
def get(namespace, var):
    targetNamespace = searchNamespace(root, namespace)
    if targetNamespace is None:
        return None
    else:
        result = searchVar(targetNamespace, var, namespace)
        if (result is None) and (namespace != 'global'):
            parent = searchParent(root['global'], targetNamespace, 'global')
            result = get(parent, var)
        return result
