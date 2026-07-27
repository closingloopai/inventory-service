"""Reserve stock for an order's lines."""
from inventory.errors import OutOfStockError, UnknownSkuError

def reserve_order(levels, lines):
    """Reserve every line in ``lines`` against ``levels`` (dict sku -> StockLevel).

    BUG: it reserves each line as it goes, so if a LATER line is out of stock the
    EARLIER lines are left reserved (a partial reservation that leaks stock). It
    must validate availability for ALL lines first and only then reserve, so the
    operation is all-or-nothing.
    """
    for sku, qty in lines:
        lvl = levels.get(sku)
        if lvl is None:
            raise UnknownSkuError(sku)
        if lvl.available < qty:
            raise OutOfStockError(sku)
        lvl.reserved += qty
    return True
