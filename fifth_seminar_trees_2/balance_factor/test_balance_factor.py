import pytest

from balance_factor import balance_factor_and_height
from fourth_seminar_trees_1.tree_node import TreeNode


@pytest.mark.parametrize(
    "tree, expected_height, expected_balance",
    [
        (None, 0, 0),

        (TreeNode(1), 1, 0),

        (
                TreeNode(1,
                         TreeNode(2,
                                  TreeNode(3))),
                3, 2
        ),

        (
                TreeNode(1,
                         None,
                         TreeNode(2,
                                  None,
                                  TreeNode(3))),
                3, -2
        ),

        (
                TreeNode(1,
                         TreeNode(2,
                                  TreeNode(4),
                                  TreeNode(5)),
                         TreeNode(3,
                                  TreeNode(6),
                                  TreeNode(7))),
                3, 0
        ),

        (
                TreeNode(1,
                         TreeNode(2,
                                  TreeNode(3,
                                           TreeNode(4))),
                         TreeNode(5)),
                4, 2
        ),
    ],
)
def test_balance_factor(tree, expected_height, expected_balance):
    height, balance = balance_factor_and_height(tree)
    assert height == expected_height
    assert balance == expected_balance
