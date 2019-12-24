class Node():
    '''
    节点类型
    '''

    def __init__(self, data, level=0):
        self.data = data  # 节点数据
        self.level = level  # 节点类型
        self.fatherNode = None  # 父节点
        self.children = []  # 子节点


class MenuTree():
    def __init__(self, rootData):
        self.initTree(rootData)

    def initTree(self, rootData):
        self.root = Node(rootData)
        rootChildNode_1 = Node('第一章', level=1)
        node1 = Node('1.1', level=2)
        node2 = Node('1.2', level=2)
        node3 = Node('1.3', level=2)
        node4 = Node('1.4', level=2)
        node5 = Node('1.5', level=2)
        rootChildNode_1.children.append(node1)
        rootChildNode_1.children.append(node2)
        rootChildNode_1.children.append(node3)
        rootChildNode_1.children.append(node4)
        rootChildNode_1.children.append(node5)
        self.root.children.append(rootChildNode_1)
        rootChildNode2 = Node('第二章', level=1)
        self.root.children.append(rootChildNode2)
        rootChildNode3 = Node('第三章', level=1)
        self.root.children.append(rootChildNode3)
        rootChildNode4 = Node('第四章', level=1)
        self.root.children.append(rootChildNode4)
        rootChildNode5 = Node('第五章', level=1)
        self.root.children.append(rootChildNode5)
        rootChildNode6 = Node('第六章', level=1)
        self.root.children.append(rootChildNode6)

    @staticmethod
    def viewTree(node):
        level = node.level
        print('    ' * level + node.data)
        children = node.children
        for itemNode in children:
            MenuTree.viewTree(itemNode)

    @staticmethod
    def findNodeByData(node, nodeData):
        if node.data == nodeData:
            return node
        else:
            children = node.children
            if len(children) > 0:
                for child in children:
                    revNode = MenuTree.findNodeByData(child, nodeData)
                    if revNode != None:
                        return revNode
            else:
                pass

    # 添加节点
    @staticmethod
    def add_node(node, level, name):
        node.children.append(Node(name, level=int(level, 10)))

    # 删除节点
    @staticmethod
    def delete_node(node, name):
        current_data = MenuTree.findNodeByData(node, name)
        if current_data in node.children:
            return node.children.remove(current_data)
        else:
            children = node.children
            if len(children) > 0:
                for child in children:
                    remove_node = MenuTree.findNodeByData(child, name)
                    if remove_node is not None and child is not Node:
                        child.children.remove(remove_node)
            else:
                pass


tree = MenuTree('python 目录')
# Tree.viewTree(tree.root)
while True:
    recevieStr = input('查看树输入1，添加树输入2,查找树节点输入3,删除树节点输入4:')
    if recevieStr == '1':
        print('查看树')
        MenuTree.viewTree(tree.root)

    elif recevieStr == '2':
        print('添加树')
        add_node_name = input('请输入希望添加的节点名称')
        add_node_level = input('请输入与希望添加节点的级别')
        find_node = MenuTree.findNodeByData(tree.root, add_node_name)
        if find_node is not None:
            print("该节点已经存在")
        else:
            MenuTree.add_node(tree.root, add_node_level, add_node_name)
            print("添加节点已经成功")

    elif recevieStr == '3':
        print('查找树节点')
        findNodeData = input('请输入查找节点')
        findNode = MenuTree.findNodeByData(tree.root, findNodeData)
        if findNode is None:
            print('没有这个节点')
        else:
            print('find success')
            print(findNode.data)
    elif recevieStr == '4':
        print('删除树节点')
        delete_node_name = input('请输入希望删除的节点名称')
        find_node = MenuTree.findNodeByData(tree.root, delete_node_name)
        if find_node is Node:
            print('没有这个节点')
        else:
            MenuTree.delete_node(tree.root, delete_node_name)
            print('删除树节点成功')

    else:
        print('')
