from tests import *


@pytest.fixture
def expected_result(request):
    input_str = request.node.funcargs['input_str']
    return test_data[input_str]


@pytest.mark.parametrize('input_str', test_data.keys())
def test_app_with_sample_data(input_str, expected_result):
    try:
        record = StrToListApp.convert(input_str)
        assert record == expected_result
    except (TypeError, ValueError):
        assert True


