def func(node):
    if node == null:
        return 0;
    a = func(node.left)
    b = func(node.right)
    return (max(a,b)+1)

# root given

print(func(root))