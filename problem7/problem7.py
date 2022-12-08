from tree import Node


def crate_directory_tree(terminal: list[str]) -> Node:
    """
    Given the terminal output as printed in the input file,
    parse the infrmomation and return a Node object representing
    the complete directory tree.
    """
    # initialize tree
    node = Node(name='/', node_type='dir')
    for line in terminal:
        # if the line is not a command it means we are printing files or dirs and
        # we should introduce that info in our current node of the tree
        if line == '$ cd /':
            node = node.go_to_root()

        elif not line.startswith('$'):
            node_type, node_name = line.split(' ')
            file_size = None
            if node_type != 'dir':
                file_size = int(node_type)
                node_type = 'file'

            node.add_children(Node(node_name, node_type, file_size))

        # move up a directory
        elif line == '$ cd ..':
            node = node.move_up()

        # move to subdirectory
        elif line.startswith('$ cd '):
            dir_to_go = line.split(' ')[-1]
            node = node.move_down(dir_to_go)

    return node.go_to_root()


def get_subdirectories_sizes(tree_root: Node) -> list[int]:
    """
    Giving a node pointing to the root of a tree: traverse the whole tree and
    return the sizes of each diretory in a list.
    """
    node = tree_root
    sizes = [tree_root.get_size()]
    for kid in node.children:
        if kid.type == 'dir':
            sizes += get_subdirectories_sizes(kid)

    return sizes


def get_sum_valid_directories(tree_root: Node, max_dir_size: int) -> int:
    """
    Giving the root of a tree (or sub tree), return the sum of all subdirectory
    size that are equal or smaller than max_dir_size
    """
    dir_sizes = get_subdirectories_sizes(tree_root=tree_root)

    acc = 0
    for dir_size in dir_sizes:
        if dir_size <= max_dir_size:
            acc += dir_size

    return acc


def get_size_of_min_directory_to_delete(tree: Node, min_free_space: int) -> int:
    """
    Return the size of the smallest directory with size greater than space_to_free.
    """
    min_dir_size = 70000000

    dir_sizes = get_subdirectories_sizes(tree_root=tree)

    free_space = 70000000 - tree.get_size()
    space_to_free = min_free_space-free_space

    for size in dir_sizes:
        if (size > space_to_free) & (size < min_dir_size):
            min_dir_size = size

    return min_dir_size


if __name__ == '__main__':
    # read file and store each line in list
    with open('problem7/input7.txt', 'r') as input:
        terminal = [line.rstrip('\n') for line in input]

    tree = crate_directory_tree(terminal)
    print(get_sum_valid_directories(tree, 100000))

    print(get_size_of_min_directory_to_delete(tree, 30000000))
