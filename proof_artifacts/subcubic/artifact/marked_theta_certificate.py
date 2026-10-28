"""Standard-library checker for a fixed mixed port in a bipartite theta."""
import itertools
import json
from pathlib import Path

from sparse_bip_core_certificate import verify_certificate as verify_chain_certificate


def verify_certificate(data):
    chain_data = data["unmarked_chain_certificate"]
    previous = verify_chain_certificate(chain_data)
    expected = {(p, q, a, b) for p, q in itertools.product(range(1, 9), repeat=2)
                for a in range(1, 9) for b in range(a, 9)
                if a % 2 == b % 2 == (p + q) % 2 and not a == b == 1}
    records = data["marked_records"]
    keys = [tuple(record["lengths"]) for record in records]
    assert len(keys) == len(set(keys)) == len(expected) == 608 and set(keys) == expected
    safe = (0, 1, 3, 5, 6)
    def path(length, left_red, first, right_red, last):
        current = {(first, left_red)}
        for _ in range(length - 1):
            following = set()
            for edge, previous_red in current:
                for new, port in itertools.product(range(3), (0, 2)):
                    red = edge + new + port
                    if red in safe and red != previous_red:
                        following.add((new, red))
            current = following
        return any(edge == last and red != right_red for edge, red in current)
    for record in records:
        p, q, a, b = record["lengths"]
        left, right = record["left_ports"], record["right_ports"]
        assert len(left) == len(right) == 3 and all(x in (0, 1, 2) for x in left + right)
        L, R = sum(left), sum(right)
        assert L in safe and R in safe
        assert path(p, L, left[0], 1, 0)
        assert path(q, 1, 0, R, right[0])
        assert path(a, L, left[1], R, right[1])
        assert path(b, L, left[2], R, right[2])
    return {"complete_marked_records": 608, "representative_chains_checked": 2432,
            "unmarked_chain_certificate": previous,
            "marked_mixed_port_one_root_red_one": True,
            "all_checks_passed": True, "mother_conjecture_proved": False}


if __name__ == "__main__":
    base = Path(__file__).parent
    result = verify_certificate(json.loads((base / "marked_theta_interfaces.json").read_text(encoding="utf-8")))
    (base / "marked_theta_certificate_check.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result))
