"""Independent STANDARD-LIBRARY checker for all rooted odd-cactus interfaces."""

import itertools
import json
from pathlib import Path


def verify_certificate(data):
    safe = {0, 1, 3, 5, 6}
    states = [(x, r) for x in range(3) for r in sorted(safe) if x <= r <= x + 4]
    assert data["state_order"] == [list(s) for s in states]
    types = {
        "L": {(0, 0), (1, 1), (1, 3), (1, 5), (2, 6)},
        "O": {(0, 1), (0, 3), (1, 1), (1, 3), (1, 5), (2, 3), (2, 5)},
        "A": set(states),
        "C": {(0, 0), (0, 1), (1, 3), (2, 5), (2, 6)},
        "D": {(0, 0), (0, 1), (0, 3), (1, 3), (2, 3), (2, 5), (2, 6)},
        "E": {(0, 0), (0, 1), (1, 1), (1, 3), (1, 5), (2, 5), (2, 6)},
    }
    assert data["types"] == {name: [list(s) for s in sorted(t)] for name, t in types.items()}
    name_by_states = {frozenset(t): name for name, t in types.items()}
    actual_local = {}
    for c in range(3):
        for names in itertools.product(types, repeat=c):
            found = set()
            for incoming in range(3):
                for choices in itertools.product(*(types[name] for name in names)):
                    for free_ports in itertools.product((0, 2), repeat=2 - c):
                        red = incoming + sum(s[0] for s in choices) + sum(free_ports)
                        if red in safe and all(red != s[1] for s in choices):
                            found.add((incoming, red))
            assert frozenset(found) in name_by_states
            actual_local[names] = name_by_states[frozenset(found)]
    stored_local = {}
    for record in data["local_records"]:
        key = tuple(record["children"])
        assert key not in stored_local
        stored_local[key] = record["result"]
    assert stored_local == actual_local and len(actual_local) == 43
    # Rows and columns are actual (edge_weight, previous_vertex_red) states.
    def matrix(name):
        result = []
        for previous_edge, previous_red in states:
            row = 0
            for j, (following_edge, red) in enumerate(states):
                if red == previous_red:
                    continue
                port = red - previous_edge - following_edge
                if name == "F":
                    allowed = port in (0, 2)
                else:
                    allowed = any(x == port and child_red != red for x, child_red in types[name])
                if allowed:
                    row += 1 << j
            result.append(row)
        return tuple(result)
    matrices = {name: matrix(name) for name in ["F"] + list(types)}
    assert data["letter_matrices"] == {name: list(m) for name, m in matrices.items()}
    def product(left, right):
        rows = []
        for row in left:
            value = 0
            for j in range(9):
                if row & (1 << j):
                    value |= right[j]
            rows.append(value)
        return tuple(rows)
    pair = {product(a, b) for a in matrices.values() for b in matrices.values()}
    four = {product(a, b) for a in pair for b in pair}
    six = {product(a, b) for a in four for b in pair}
    eight = {product(a, b) for a in six for b in pair}
    for label, expected in [("two", pair), ("four", four), ("six", six)]:
        stored = [tuple(row) for row in data["even_product_layers"][label]]
        assert len(stored) == len(set(stored)) and set(stored) == expected
    assert [len(pair), len(four), len(six)] == [14, 11, 2]
    assert eight == six  # Induction: all longer even products stay here.
    lookup = {s: i for i, s in enumerate(states)}
    def rooted_cycle_interface(m):
        found = set()
        for incoming, anchor_red in states:
            for first in range(3):
                last = anchor_red - incoming - first
                if last not in (0, 1, 2) or (first, anchor_red) not in lookup:
                    continue
                row = m[lookup[(first, anchor_red)]]
                if any(row & (1 << j) and z == last and red != anchor_red
                       for j, (z, red) in enumerate(states)):
                    found.add((incoming, anchor_red))
                    break
        assert frozenset(found) in name_by_states
        return name_by_states[frozenset(found)]
    profiles = {label: sorted(rooted_cycle_interface(m) for m in layer)
                for label, layer in [("two", pair), ("four", four), ("six", six)]}
    assert profiles == data["cycle_interface_profiles"]
    assert profiles["two"] == ["C"] + ["D"] * 13
    assert profiles["four"] == ["A"] * 10 + ["D"]
    assert profiles["six"] == ["A", "A"]
    assert all(any(x == 0 for x, red in t) for t in types.values())
    return {"local_records": 43, "matrix_layer_sizes": [14, 11, 2],
            "six_letter_layer_closed_under_any_two_more_letters": True,
            "all_interfaces_accept_zero_incoming_port": True, "all_checks_passed": True,
            "scope": "Finite identities for universal rooted-tree and arbitrary odd-cycle induction.",
            "mother_conjecture_proved": False}


if __name__ == "__main__":
    base = Path(__file__).parent
    result = verify_certificate(json.loads((base / "safe_cactus_interfaces.json").read_text(encoding="utf-8")))
    (base / "safe_cactus_certificate_check.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result))
