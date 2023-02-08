import pytest


@pytest.fixture
def get_data(request):
    if request.param == 'small':
        return [
            ['DB', '', '', '', 'DB 1'],
            ['', 'TBL', '', '', 'TBL 1'],
            ['', '', 'COL1', 'int', 'Column 1'],
        ]
    elif request.param == 'large':
        return [
            ['DB', '', '', '', 'DB 1'],
            ['', 'TBL', '', '', 'TBL 1'],
            ['', '', 'COL1', 'int', 'Column 1'],
            ['DB', '', '', '', 'DB 2'],
            ['', 'TBL', '', '', 'TBL 2'],
            ['', '', 'COL1', 'int', 'Column 1'],
            ['', '', 'COL2', 'string', 'Column 2'],
            ['', 'TBL', '', '', 'TBL 3'],
            ['', '', 'COL1', 'int', 'Column 1'],
            ['', '', 'COL2', 'string', 'Column 2'],
        ]
