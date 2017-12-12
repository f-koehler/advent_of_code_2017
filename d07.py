import re
import collections

if __name__ == "__main__":
    # parse the input
    weights = {}
    children = {}
    names = set()
    regex = re.compile(r"\w+")
    with open("input_07.txt") as fhandle:
        for line in fhandle:
            name, weight, *children_ = regex.findall(line)
            weights[name] = int(weight)
            children[name] = list(children_)
            names.add(name)

    # determine the set of all child nodes
    set_children = {
        child
        for children_ in children.values() for child in children_
    }

    # the root node will appear in the set of all node names but not
    # in the set of child nodes
    root_name, = names - set_children

    print(root_name)

    # compute the weight of all sub trees
    tree_weights = {name: -1 for name in names}

    def compute_tree_weight(name):
        tree_weights[name] = weights[name]
        for child in children[name]:
            if tree_weights[child] == -1:
                compute_tree_weight(child)
            tree_weights[name] += tree_weights[child]

    compute_tree_weight(root_name)

    # trace the imbalance into depths of the tree
    imbalances = []

    def get_sub_weights(name):
        return [tree_weights[child] for child in children[name]]

    def get_odd_sub_weight(sub_weights):
        most_common = collections.Counter(sub_weights).most_common()
        if len(most_common) == 1:
            return None, None
        (common_weight, _), (odd_weight, _) = most_common
        return common_weight, odd_weight

    def trace_imbalance(name):
        if not children[name]:
            raise RuntimeError("Reached leaf!")

        sub_weights = get_sub_weights(name)
        _, odd_weight = get_odd_sub_weight(sub_weights)
        if odd_weight is None:
            return
        else:
            imbalances.append(name)
            trace_imbalance(children[name][sub_weights.index(odd_weight)])

    # we found the last node to have different subtree weights
    trace_imbalance(root_name)
    imbalance = imbalances[-1]

    # find the node with the odd (own) weight
    sub_weights = get_sub_weights(imbalance)
    common_weight, odd_weight = get_odd_sub_weight(sub_weights)
    wrong_node = children[imbalance][sub_weights.index(odd_weight)]

    print(weights[wrong_node] + common_weight - odd_weight)
