class Tree(object):
    """ Simple BST (without the searching because YOLO) """
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data is None:
            self.data = data
        elif self.data < data:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Tree(data)
        else:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = Tree(data)

    def post_order(self):
        if self.left is None:
            left_post = []
        else:
            left_post = self.left.post_order()

        if self.right is None:
            right_post = []
        else:
            right_post = self.right.post_order()

        center = [self.data]
        
        return left_post + right_post + center
