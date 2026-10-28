"""Independent stdlib-only audit of the COMPLETE sparse-core finite kernel.

No import from the producer and no constraint solver. This verifies finite
coverage and the chain saturation certificate; it does not claim that the
global mother conjecture follows.
"""

import itertools
import json
from pathlib import Path


def verify_certificate(data):
    safe = (0, 1, 3, 5, 6)
    states = [(edge, red) for edge in range(3) for red in safe if edge <= red <= edge + 4]
    assert [list(state) for state in states] == data["states"]
    transitions = []
    for edge, old_red in states:
        allowed = set()
        for new_edge, boundary in itertools.product(range(3), (0, 2)):
            red = edge + new_edge + boundary
            if red in safe and red != old_red:
                allowed.add(states.index((new_edge, red)))
        transitions.append(allowed)
    assert [sorted(row) for row in transitions] == data["transition_rows"]
    walks = data["six_step_walks"]
    assert len(walks) == 81
    assert {(row[0], row[-1]) for row in walks} == set(itertools.product(range(9), repeat=2))
    for row in walks:
        assert len(row) == 7 and all(0 <= v < 9 for v in row)
        assert all(v in transitions[u] for u, v in zip(row, row[1:]))
    # Every state has an incoming edge, so universality at six transitions
    # implies universality at every larger number of transitions.
    assert set().union(*transitions) == set(range(9))
    assert all(transitions)
    leaf_good = {i for i, (edge, old_red) in enumerate(states)
                 if any(edge + 2 * k in safe and edge + 2 * k != old_red for k in range(3))}
    assert {i for i, row in enumerate(transitions) if row & leaf_good} == set(range(9))
    assert all(i in leaf_good for i, (_, red) in enumerate(states) if red % 2)
    expected = {("claw", ())}
    expected |= {("lollipop", (length,)) for length in (4, 6, 8)}
    expected |= {("double_star", (length,)) for length in range(1, 9)}
    expected |= {("lollipop_fork", (a, b)) for a, b in itertools.product((4, 6, 8), range(1, 9))}
    expected |= {("cycle_two_arms", (a, b)) for a in range(1, 9) for b in range(a, 9)
                 if (a + b) % 2 == 0 and a + b >= 4}
    expected |= {("theta", lengths) for lengths in itertools.combinations_with_replacement(range(1, 9), 3)
                 if len({n % 2 for n in lengths}) == 1 and lengths.count(1) <= 1}
    expected |= {("barbell", lengths) for lengths in itertools.product((4, 6, 8), (4, 6, 8), range(1, 9))}
    records = data["finite_records"]
    keys = [(record["shape"], tuple(record["lengths"])) for record in records]
    assert len(keys) == len(set(keys)) == len(expected) == 163 and set(keys) == expected
    assert not data["failures"]
    def chain(length, left_red, first, right_red, last):
        current = {(first, left_red)}
        for _ in range(length - 1):
            following = set()
            for edge, red in current:
                for new_edge, boundary in itertools.product(range(3), (0, 2)):
                    new_red = edge + new_edge + boundary
                    if new_red in safe and new_red != red:
                        following.add((new_edge, new_red))
            current = following
        return any(edge == last and red != right_red for edge, red in current)
    chain_checks = 0
    for record in records:
        shape, lengths, witness = record["shape"], record["lengths"], record["witness"]
        reds, ports = witness["root_red"], witness["root_ports"]
        assert len(reds) == len(ports) == (1 if shape in ("claw", "lollipop") else 2)
        assert all(r in (1, 3, 5) for r in reds)
        assert all(len(row) == 3 and all(x in range(3) for x in row) and sum(row) == red
                   for row, red in zip(ports, reds))
        chains, leaves = [], []
        if shape == "claw":
            leaves = [(0, i) for i in range(3)]
        elif shape == "lollipop":
            chains = [(lengths[0], 0, 0, 0, 1)]
            leaves = [(0, 2)]
        elif shape == "double_star":
            chains = [(lengths[0], 0, 2, 1, 2)]
            leaves = [(v, i) for v in (0, 1) for i in (0, 1)]
        elif shape == "lollipop_fork":
            chains = [(lengths[0], 0, 0, 0, 1), (lengths[1], 0, 2, 1, 2)]
            leaves = [(1, 0), (1, 1)]
        elif shape == "cycle_two_arms":
            chains = [(length, 0, i, 1, i) for i, length in enumerate(lengths)]
            leaves = [(0, 2), (1, 2)]
        elif shape == "theta":
            chains = [(length, 0, i, 1, i) for i, length in enumerate(lengths)]
        else:
            assert shape == "barbell"
            chains = [(lengths[0], 0, 0, 0, 1), (lengths[1], 1, 0, 1, 1),
                      (lengths[2], 0, 2, 1, 2)]
        for length, u, a, v, b in chains:
            assert chain(length, reds[u], ports[u][a], reds[v], ports[v][b]), record
            chain_checks += 1
        for root, slot in leaves:
            edge, red = ports[root][slot], reds[root]
            assert any(edge + 2 * k in safe and edge + 2 * k != red for k in range(3))
    result = {"finite_records_verified": len(records), "six_step_walks_verified": len(walks),
              "representative_chain_interfaces_verified": chain_checks,
              "chain_saturation_from_six_steps": True, "leaf_arm_induction_verified": True,
              "complete_finite_domain_verified": True, "mother_conjecture_proved": False,
              "scope": "Complete finite auxiliary lemma certificate. Infinite graph scope uses the separate structural classification and lifting proof."}
    return result


def main():
    data = json.loads(Path(__file__).with_name("sparse_bip_core_interfaces.json").read_text(encoding="utf-8"))
    result = verify_certificate(data)
    Path(__file__).with_name("sparse_bip_core_certificate_check.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
