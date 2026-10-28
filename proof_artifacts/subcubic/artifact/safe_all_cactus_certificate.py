"""Standard-library verification of both cycle parities and a marked port."""

import json
from pathlib import Path

from safe_cactus_certificate import verify_certificate


def verify_all_cactus_certificate(data):
    previous = verify_certificate(data)
    states = [tuple(s) for s in data["state_order"]]
    names = {frozenset(map(tuple, values)): name for name, values in data["types"].items()}
    letters = set(map(tuple, data["letter_matrices"].values()))
    pair = set(map(tuple, data["even_product_layers"]["two"]))
    def mul(left, right):
        rows = []
        for row in left:
            value = 0
            for j in range(9):
                if row & 1 << j:
                    value |= right[j]
            rows.append(value)
        return tuple(rows)
    three = {mul(a, b) for a in pair for b in letters}
    five = {mul(a, b) for a in three for b in pair}
    seven = {mul(a, b) for a in five for b in pair}
    nine = {mul(a, b) for a in seven for b in pair}
    assert nine == seven
    assert [len(three), len(five), len(seven)] == [23, 6, 2]
    def interface(matrix):
        allowed = set()
        for incoming, root_red in states:
            for first in range(3):
                last = root_red - incoming - first
                if last not in (0, 1, 2) or (first, root_red) not in states:
                    continue
                row = matrix[states.index((first, root_red))]
                if any(row & 1 << j and edge == last and red != root_red
                       for j, (edge, red) in enumerate(states)):
                    allowed.add((incoming, root_red))
                    break
        return names[frozenset(allowed)]
    layers = {"three": three, "five": five, "seven": seven}
    for name, layer in layers.items():
        stored = list(map(tuple, data["odd_product_layers"][name]))
        assert len(stored) == len(set(stored)) and set(stored) == layer
    profiles = {name: sorted(interface(matrix) for matrix in layer) for name, layer in layers.items()}
    assert profiles == data["even_cycle_profiles"]
    assert profiles["three"] == ["A"] * 21 + ["O"] * 2
    assert profiles["five"] == ["A"] * 6 and profiles["seven"] == ["A"] * 2
    # A bipartite cactus uses only even cycle blocks and the three tree
    # types. Its complete rooted induction therefore stays in L/O/A.
    tree_names = {"L", "O", "A"}
    assert all(record["result"] in tree_names for record in data["local_records"]
               if set(record["children"]) <= tree_names)
    assert all(any(x == 1 and r in (1, 5) for x, r in map(tuple, data["types"][name]))
               for name in tree_names)
    assert all([1, 3] in t for t in data["types"].values())
    return {"odd_cactus_certificate": previous, "odd_product_layer_sizes": [23, 6, 2],
            "seven_letter_layer_closed_under_two_more": True,
            "bipartite_cactus_root_types": sorted(tree_names),
            "bipartite_one_marked_mixed_root_red_one_or_five": True,
            "arbitrary_cactus_one_marked_mixed_red_three": True,
            "all_checks_passed": True, "mother_conjecture_proved": False}


if __name__ == "__main__":
    base = Path(__file__).parent
    result = verify_all_cactus_certificate(json.loads(
        (base / "safe_all_cactus_interfaces.json").read_text(encoding="utf-8")))
    (base / "safe_all_cactus_certificate_check.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result))
