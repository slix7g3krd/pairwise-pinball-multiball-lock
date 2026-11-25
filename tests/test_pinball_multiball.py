import pytest
import gameplay.pinball_multiball as mod

CASES = [
    ("pool_unique_handle", (1,)),
    ("collide_per_step", (1,)),
    ("nudge_edge_trigger", (1,)),
    ("lock_clock_pause", (1,)),
    ("hit_dedup", (1,)),
    ("entry_double_confirm", (1,)),
    ("load_table", (1,)),
    ("launch", (1,)),
    ("tick_balls", (1,)),
    ("present", (1,)),
    ("validate_multiball", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
