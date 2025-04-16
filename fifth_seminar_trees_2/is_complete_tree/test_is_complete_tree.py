import pytest

from fifth_seminar_trees_2.is_complete_tree.is_complete_tree import is_complete_tree
from fourth_seminar_trees_1.tree_node import TreeNode


@pytest.mark.parametrize("tree, expected",
                         [
                             (None, True),

                             (TreeNode(1), True),

                             (TreeNode(1, TreeNode(2), TreeNode(3)), True),

                             (TreeNode(1, TreeNode(2)), True),

                             (TreeNode(1, TreeNode(2, None, TreeNode(4))), False),

                             (
                                     TreeNode(1,
                                              TreeNode(2,
                                                       TreeNode(4),
                                                       TreeNode(5)),
                                              TreeNode(3,
                                                       TreeNode(6))),
                                     True
                             ),

                             (
                                     TreeNode(1,
                                              TreeNode(2,
                                                       TreeNode(4)),
                                              TreeNode(3,
                                                       None,
                                                       TreeNode(7))),
                                     False
                             ),

                             (
                                     TreeNode(1,
                                              TreeNode(2,
                                                       TreeNode(4),
                                                       TreeNode(5)),
                                              TreeNode(3,
                                                       TreeNode(6),
                                                       TreeNode(7))),
                                     True
                             ),
                         ]
                         )
def test_is_complete_tree(tree, expected):
    assert is_complete_tree(tree) == expected
