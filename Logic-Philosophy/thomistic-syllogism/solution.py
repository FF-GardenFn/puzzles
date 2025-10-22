from z3 import *

# Sorts / predicates
Object = DeclareSort('Object')
Composite = Function('Composite', Object, BoolSort())
Body      = Function('Body',      Object, BoolSort())
Movable   = Function('Movable',   Object, BoolSort())
god = Const('god', Object)

# Axioms (tracked)
A1 = Bool('A1'); A2 = Bool('A2'); A3 = Bool('A3'); Claim = Bool('Claim')

def refutation():
    s = Solver()
    x = Const('x', Object)
    s.assert_and_track(ForAll([x], Implies(Composite(x), Body(x))), A1)
    s.assert_and_track(ForAll([x], Implies(Body(x), Movable(x))),   A2)
    s.assert_and_track(Not(Movable(god)), A3)
    s.assert_and_track(Composite(god),    Claim)   # negation of desired conclusion
    res = s.check()
    return res, s.unsat_core() if res == unsat else None

def non_vacuous_model():
    s = Solver()
    x = Const('x', Object)
    h = Const('h', Object)
    s.add(ForAll([x], Implies(Composite(x), Body(x))))
    s.add(ForAll([x], Implies(Body(x), Movable(x))))
    s.add(Not(Movable(god)))
    s.add(Composite(h))
    res = s.check()
    return res, s.model() if res == sat else None

if __name__ == "__main__":
    r, core = refutation()
    print("Refutation:", r)
    if core: print("Unsat core:", core)
    r2, m = non_vacuous_model()
    print("Non-vacuous model:", r2)
    if m: print(m)