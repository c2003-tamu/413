import angr
import claripy

project = angr.Project('./crackme', auto_load_libs=False)

arg1 = claripy.BVS('arg1', 32)
arg2 = claripy.BVS('arg2', 32)

argv = ['./crackme', arg1, arg2]
state = project.factory.full_init_state(args=argv)

simulation = project.factory.simgr(state)

simulation.explore(find=lambda s: b"Granted" in s.posix.dumps(1))

if simulation.found:
    print(f"Found inputs: {simulation.found[0].solver.eval(arg1, cast_to=int)} , {simulation.found[0].solver.eval(arg2, cast_to=int)}")
else:
    print("inputs not found")
