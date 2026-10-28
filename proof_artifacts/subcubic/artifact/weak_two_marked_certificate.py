"""Independent standard-library certificate for four long ports and two marks."""
import itertools
import json
from pathlib import Path
from sparse_bip_core_certificate import verify_certificate as verify_chain_saturation


def verify_certificate(data):
    previous = verify_chain_saturation(data["chain_saturation"])
    safe = {0, 1, 3, 5, 6}
    def unary(states):
        found = set()
        for incoming in range(3):
            for child_edge, child_red in states:
                for private in (0, 2):
                    red = incoming + child_edge + private
                    if red in safe and red != child_red:
                        found.add((incoming, red))
        return found
    U = [{(x, x + 2*k) for x in range(3) for k in range(3) if x + 2*k in safe}]
    Q = [{(0, 1), (2, 5)}]
    for _ in range(3):
        U.append(unary(U[-1]))
    for _ in range(6):
        Q.append(unary(Q[-1]))
    assert U[2] == U[3] and Q[5] == Q[6]
    assert data["unmarked_arm_layers"] == [sorted(map(list,t)) for t in U]
    assert data["marked_arm_layers"] == [sorted(map(list,t)) for t in Q]
    types = {"u0": None, "m0": None}
    types.update({"u"+str(i+1): t for i,t in enumerate(U[:3])})
    types.update({"m"+str(i+1): t for i,t in enumerate(Q[:6])})
    assert not data["failures"] and data["domain_cases"]==4256
    assert data["branch_types"]=={name:None if t is None else sorted(map(list,t)) for name,t in types.items()}
    u, m = ["u"+str(i) for i in range(4)], ["m"+str(i) for i in range(7)]
    side_pairs = list(itertools.product(list(itertools.combinations_with_replacement(m,2)),
                                       list(itertools.combinations_with_replacement(u,2))))
    side_pairs += list(itertools.product(list(itertools.product(m,u)),repeat=2))
    expected = {(tuple(a),tuple(b),n) for a,b in side_pairs for n in (1,3,5,7)}
    records = data["records"]
    keys = [(tuple(r["left"]),tuple(r["right"]),r["length"]) for r in records]
    assert len(keys)==len(set(keys))==len(expected)==4256 and set(keys)==expected
    def side(types_here, state, witnesses):
        edge, red = state
        assert edge in (0,1,2) and 0<=red<=6 and len(witnesses)==2
        assert red == edge + sum(x for x,other in witnesses)
        for name,(value,other) in zip(types_here,witnesses):
            if name=="u0":
                assert value in (0,2) and other is None
            elif name=="m0":
                assert value==1 and other is None and red!=3
            else:
                assert (value,other) in types[name] and red!=other
    def chain(length,first,L,last,R):
        possible={(first,L)}
        for _ in range(length-1):
            following=set()
            for x,old in possible:
                for y,p in itertools.product(range(3),(0,2)):
                    red=x+y+p
                    if red in safe and red!=old:following.add((y,red))
            possible=following
        return any(x==last and red!=R for x,red in possible)
    for record in records:
        w=record["witness"]
        side(record["left"],w["left_state"],w["left_branches"])
        side(record["right"],w["right_state"],w["right_branches"])
        x,L=w["left_state"]; y,R=w["right_state"]
        assert chain(record["length"],x,L,y,R)
    # Red two/four at an unconstrained end removes a comparison against
    # an internal SAFE red; it dominates the same-port red-three relation.
    for x in range(3):
        for r in (2,4):
            if not x<=r<=x+4:continue
            for y,p in itertools.product(range(3),(0,2)):
                s=x+y+p
                if s in safe and s!=3:assert s!=r
    return {"complete_side_and_connector_cases":4256,"arm_unmarked_stable_from_length":3,
            "arm_marked_stable_from_length":6,"all_odd_connector_lengths_covered":True,
            "unconstrained_end_red_two_four_dominance_verified":True,
            "chain_saturation":previous,"all_checks_passed":True,"mother_conjecture_proved":False}


if __name__=="__main__":
    base=Path(__file__).parent
    result=verify_certificate(json.loads((base/"weak_two_marked_interfaces.json").read_text(encoding="utf-8")))
    (base/"weak_two_marked_certificate_check.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result))
