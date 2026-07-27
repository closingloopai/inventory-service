import pytest
from inventory.models.stock import StockLevel
from inventory.services.reservation import reserve_order
from inventory.errors import OutOfStockError

def test_reservation_is_all_or_nothing():
    levels = {"A": StockLevel("A", 5), "B": StockLevel("B", 0)}
    with pytest.raises(OutOfStockError):
        reserve_order(levels, [("A", 2), ("B", 1)])
    assert levels["A"].reserved == 0, "A must not stay reserved when B fails"
