# -*- coding: utf-8 -*-
import py4hw
import py4hw.debug
import pytest

class Test_Add:
    
    
    def test_1(self):
        sys = py4hw.HWSystem()
        a = sys.wire("a", 32)
        b = sys.wire("b", 32)
        r1 = sys.wire("r", 32)
        py4hw.Constant(sys, "a", 10, a)
        py4hw.Constant(sys, "b", 20, b)
        py4hw.Add(sys, "add1", a,b, r1)
        sys.getSimulator().clk(1);
        assert (r1.get() == 30)
        
    def test_Integrity(self):
        sys = py4hw.HWSystem()
        
        a = sys.wire("a", 32)
        b = sys.wire("b", 32)
        c = sys.wire("c", 32)
        r1 = sys.wire("r", 32)
        r2 = sys.wire("r2", 32)
        
        py4hw.Add(sys, "add1", a,b, r1)
        py4hw.Add(sys, "add2", r1, c, r2)
        
        py4hw.Constant(sys, "a", 10, a)
        py4hw.Constant(sys, "b", 20, b)
        py4hw.Constant(sys, "c", 5, c)
        py4hw.Scope(sys, "r2", r2)
        
        py4hw.debug.checkIntegrity(sys)
        # py4hw.debug.printHierarchy(sys)
        
        # print('RESET')
        # sim = sys.getSimulator()
        
        # print()
        # print('CLK')
        # sim.clk(1)


if __name__ == '__main__':
    pytest.main(args=['-q', 'Test_Add.py'])