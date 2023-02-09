from src.modules.retrieve_data import get_data

def test_table_data():
    table_data = get_data()
    assert len(table_data) == 11
    assert table_data == [ 
        ['DB', '', '', '', 'DB 1'], 
        ['', 'TBL', '', '', 'TBL 1'], 
        ['', '', 'COL1', 'int', 'Column 1'], 
        ['', '', 'COL2', 'string', 'Column 2'], 
        ['DB', '', '', '', 'DB 2'], 
        ['', 'TBL', '', '', 'TBL 2'], 
        ['', '', 'COL1', 'int', 'Column 1'], 
        ['', '', 'COL2', 'string', 'Column 2'], 
        ['', 'TBL', '', '', 'TBL 3'], 
        ['', '', 'COL1', 'int', 'Column 1'], 
        ['', '', 'COL2', 'string', 'Column 2'], 
    ]