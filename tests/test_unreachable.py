import xmostest

def runtest():
    xmostest.build("unreachable_test")
     
    resources = xmostest.request_resource("xsim")
     
    tester = xmostest.ComparisonTester(open('unreachable_test.expect'),
                                       'lib_xassert', 'simple_tests',
                                       'unreachable_test', {})
     
    xmostest.run_on_simulator(resources['xsim'],
                              'unreachable_test/bin/unreachable_test.xe',
                              tester=tester)