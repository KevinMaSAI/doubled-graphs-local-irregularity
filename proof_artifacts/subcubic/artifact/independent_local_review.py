"""Fresh A1 local audit from actual red/blue conditions, no producer imports.

This finite computation is paired with explicit infinite lifting arguments
in the review report; graph samples are not used as an existence proof.
"""
from itertools import product, combinations_with_replacement
from pathlib import Path
import json, time

SAFE={0,1,3,5,6}

def edge_ok(weight, left, right, left_degree, right_degree):
    return (weight==0 or left!=right) and (
        weight==2 or 2*left_degree-left!=2*right_degree-right)

def path_exists(n,a,b,left,right,rd=3):
    assert n>=2
    current={(a,left)}
    for j in range(1,n):
        following=set()
        for old_edge,old_red in current:
            for x in ([b] if j==n-1 else range(3)):
                red=old_edge+x
                if edge_ok(old_edge,old_red,red,3 if j==1 else 2,2):
                    following.add((x,red))
        current=following
    return any(edge_ok(b,r,right,2,rd) for e,r in current)

def pendant_exists(n,a,r):
    if n==1:return edge_ok(a,r,a,3,1)
    return any(path_exists(n,a,b,r,b,rd=1) for b in range(3))

def local_paths():
    physical=[(a,r) for a in range(3) for r in range(a,a+5)]
    p3=0;pure=0;returns=0;pendants=0
    for (a,r),(b,s) in product(physical,repeat=2):
        pred=a!=b and not ((a==1 or b==1) and r==s==3)
        assert path_exists(3,a,b,r,s)==pred,(a,r,b,s)
        p3+=1
        if a in (0,2) and b in (0,2):
            assert path_exists(2,a,b,r,s)==(r!=2+b and s!=2+a)
            for n in range(3,33):
                if n>=4 or a!=b:
                    assert path_exists(n,a,b,r,s),(n,a,r,b,s)
                    pure+=1
    for n in range(3,33):
        for a,b in [(0,1),(0,2),(1,2)]:
            for r in range(a+b,a+b+3):
                if (a,b)==(0,2) or r%3:
                    assert path_exists(n,a,b,r,r),(n,a,b,r)
                    returns+=1
    for n in range(1,33):
        for a,r in physical:
            if a not in (0,2):continue
            if r in SAFE:
                assert pendant_exists(n,a,r),(n,a,r)
                pendants+=1
            phi=r%3
            chosen=2 if (n==1 and phi==1) or (n==2 and phi==2) else 0
            if a==chosen:
                assert pendant_exists(n,a,r),(n,a,r)
    return dict(exact_three_edge_interfaces=p3,pure_path_checks=pure,
                return_path_checks=returns,safe_pendant_checks=pendants)

def arm_step(states):
    return {(x,x+y+p) for x in range(3) for y,s in states for p in (0,2)
            if x+y+p in SAFE and x+y+p!=s}

def side_states(names,types):
    sets=[]
    for name in names:
        sets.append([(0,None),(2,None)] if name=='u0' else
                    [(1,None)] if name=='m0' else list(types[name]))
    out=set()
    for x in range(3):
        for (y,r),(z,s) in product(*sets):
            red=x+y+z
            if r==red or s==red:continue
            if 'm0' in names and red==3:continue
            out.add((x,red))
    return out

def connector_relation(n):
    relation=set()
    for x in range(3):
        for R in range(x,x+5):
            current={(x,R)}
            for j in range(n-1):
                nxt=set()
                for prev,r in current:
                    for e,p in product(range(3),(0,2)):
                        s=prev+e+p
                        if s in SAFE and edge_ok(prev,r,s,3,3):nxt.add((e,s))
                current=nxt
            for e,s in current:
                for S in range(e,e+5):
                    if edge_ok(e,s,S,3,3):relation.add(((x,R),(e,S)))
    return relation

def kernel():
    u=[{(x,x+a+b) for x,a,b in product(range(3),(0,2),(0,2)) if x+a+b in SAFE}]
    m=[{(x,x+1+p) for x,p in product(range(3),(0,2)) if x+1+p in SAFE-{3}}]
    while len(u)<5:u.append(arm_step(u[-1]))
    while len(m)<8:m.append(arm_step(m[-1]))
    assert u[2]==u[3]==u[4] and m[5]==m[6]==m[7]==u[2]
    assert list(map(len,u[:3]))==[5,7,9]
    assert list(map(len,m[:6]))==[2,3,5,7,7,9]
    types={'u'+str(i+1):v for i,v in enumerate(u[:3])}
    types.update({'m'+str(i+1):v for i,v in enumerate(m[:6])})
    unmarked=['u'+str(i) for i in range(4)]
    marked=['m'+str(i) for i in range(7)]
    configs=list(product(combinations_with_replacement(marked,2),combinations_with_replacement(unmarked,2)))
    configs+=list(product(product(marked,unmarked),repeat=2))
    assert len(configs)==1064
    relations={n:connector_relation(n) for n in (1,3,5,7)}
    side_cache={names:side_states(names,types) for c in configs for names in c}
    count=0
    for left,right in configs:
        for n,rel in relations.items():
            assert any((a,b) in rel for a,b in product(side_cache[left],side_cache[right])),(left,right,n)
            count+=1
    # Independent proof of the saturation assertion, including persistence.
    states={(x,r) for x in range(3) for r in SAFE if x<=r<=x+4}
    T={(a,b) for a,b in product(states,repeat=2)
       if a[1]!=b[1] and b[1]-a[0]-b[0] in (0,2)}
    powers={1:T}
    for n in range(2,8):powers[n]={(a,c) for a,b in powers[n-1] for bb,c in T if b==bb}
    assert len(states)==9 and powers[6]==powers[7]==set(product(states,repeat=2))
    assert {b for a,b in T}==states
    return dict(fresh_kernel_cases=count,unmarked_arm_sizes=list(map(len,u[:4])),
                marked_arm_sizes=list(map(len,m[:7])),state_count=len(states),
                six_step_pairs=len(powers[6]),seven_step_pairs=len(powers[7]),
                arbitrary_long_lifting_requires_written_induction=True)

def mod3_local():
    n=0
    for f in (0,1,2,3):
        for ports in product((0,2),repeat=f):
            L={0,1,2}-{(2+a)%3 for a in ports}
            assert 0 in L and len(L)>=3-f
            n+=1
    for a,b,c in product((1,2),(1,2),range(3)):
        assert {(c+a*x+b*y)%3 for x,y in product((0,1),repeat=2)}=={0,1,2}
    for phi in range(3):
        a=2 if phi==2 else 0
        assert phi!=(2+a)%3
    return dict(list_patterns=n,independent_binary_sums=12,short_target_rules=3)

if __name__=='__main__':
    start=time.monotonic()
    result={'scope':'Independent local A1 audit, not a proof by graph sampling',
            'paths':local_paths(),'fresh_kernel':kernel(),'mod3':mod3_local(),
            'all_checks_passed':True,'lean_used':False}
    result['seconds']=round(time.monotonic()-start,3)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2),flush=True)
