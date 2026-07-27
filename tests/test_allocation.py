from inventory.services.allocation import allocate
def test_no_zero_allocation():
    out = allocate(10, [("w1", 7), ("w2", 7)])
    assert all(q > 0 for _, q in out)
    assert sum(q for _, q in out) == 10
