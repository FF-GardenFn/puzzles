# Thomistic Syllogism (Z3)

**Goal**: Given axioms  
(i) ∀x (Composite(x) → Body(x))  
(ii) ∀x (Body(x) → Movable(x))  
(iii) ¬Movable(god)  
prove ¬Composite(god).
( Thomas aquinas)
**Tasks**
1. Show UNSAT when also asserting `Composite(god)` (refutation).
2. Print the UNSAT core (which assumptions clash).
3. Build a non-vacuous SAT model by asserting `Composite(h)` for some `h` and print it.