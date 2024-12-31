def hamiltonian_system(q, p, H):
    """
    Represents a Hamiltonian system's canonical coordinates.

    Args:
        q (dict): Position coordinates {q_i: position_value}.
        p (dict): Momentum coordinates {p_i: momentum_value}.
        H (function): Hamiltonian function H(q, p) -> real number.
    """
    coordinates = {q, p}  # Merge q and p into one dictionary
    energy = H(q, p)  # Evaluate Hamiltonian at current (q, p)

    return coordinates, energy

def H(q, p):
    return 0.5 * (p['p1']**2 + q['q1']**2)  # Simple harmonic oscillator

q = {'q1': 1.0}
p = {'p1': 0.0}

coords, energy = hamiltonian_system(q, p, H)
print(coords)  # {'q1': 1.0, 'p1': 0.0}
print(energy)  # 0.5
