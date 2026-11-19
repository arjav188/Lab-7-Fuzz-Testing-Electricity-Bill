from hypothesis import given, strategies as st
from electricity_bill import units_consumed, daily_average, tariff_rate


@given(st.text() | st.none())
def test_units_consumed_no_crash(s):
    result = units_consumed(s)
    assert isinstance(result, int)


@given(st.text() | st.none())
def test_daily_average_no_crash(s):
    result = daily_average(s)
    assert isinstance(result, (int, float))


@given(st.text() | st.none())
def test_tariff_rate_no_crash(s):
    result = tariff_rate(s)
    assert isinstance(result, int)
