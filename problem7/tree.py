class Node(object):
    def __init__(self, name: str, node_type: str, file_size: int = None):
        self.name = name
        self.type = node_type
        self.children = []
        self.parent = None

        if self.type == 'file':
            self.size = file_size

    def add_children(self, obj: object):
        obj.parent = self
        self.children.append(obj)

    def move_up(self):
        if self.name != '/':
            return self.parent
        else:
            return self

    def move_down(self, subdir: str):
        for kid in self.children:
            if kid.name == subdir:
                return kid

        print(f"There is no subdirecory named {subdir}")
        return self

    def go_to_root(self):
        curr_node = self
        while curr_node.name != '/':
            curr_node = curr_node.move_up()

        return curr_node

    def get_size(self) -> int:
        if self.type == 'file':
            return self.size

        acc = 0
        for kid in self.children:
            acc += kid.get_size()

        return acc
