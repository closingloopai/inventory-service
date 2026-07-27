"""Reserve stock for an order's lines."""
from inventory.errors import OutOfStockError, UnknownSkuError

def reserve_order(levels, lines):
    """Reserve every line in ``lines`` against ``levels`` (dict sku -> StockLevel).

    It must validate availability for ALL lines first and only then reserve, so the
    operation is all-or-nothing.
    """
    for sku, qty in lines:
        lvl = levels.get(sku)
        if lvl is None:
            raise UnknownSkuError(sku)
        if lvl.available < qty:
            raise OutOfStockError(sku)
    
    for sku, qty in lines:
        levels[sku].reserved += qty
    return True
