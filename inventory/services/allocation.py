"""Split a required quantity across warehouses (most-stocked first)."""
def allocate(need, warehouses):
    """Return [(warehouse, qty), ...] fulfilling ``need`` from ``warehouses``
    (list of (name, available)), largest first.

    BUG: the loop stops with ``>`` instead of ``>=`` when the remaining need is
    exactly met, and it can also emit a final zero-qty allocation. When remaining
    hits 0 it must stop, and never append a 0-qty entry.
    """
    out = []
    remaining = need
    for name, avail in sorted(warehouses, key=lambda w: -w[1]):
        take = min(avail, remaining)
        out.append((name, take))
        remaining -= take
        if remaining > 0:
            continue
    return out
