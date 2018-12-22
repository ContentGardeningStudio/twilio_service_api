
def pytest_addoption(parser):
    parser.addoption("--number", action="append", default=[], help="Number to pass to test functions")
    
    parser.addoption("--message", action="append", default=[],
        help="Message to pass to test functions")
    
def pytest_generate_tests(metafunc):
    if 'number' in metafunc.fixturenames:
        metafunc.parametrize("number",
                             metafunc.config.getoption('number'))
        
    if 'message' in metafunc.fixturenames:
        metafunc.parametrize("message",
                             metafunc.config.getoption('message'))
