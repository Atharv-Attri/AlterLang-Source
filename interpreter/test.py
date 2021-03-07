x = 5
y = 10
s = "ii"
f = 23423.1234

_varlist = globals().copy()
for _i in _varlist.keys():
    if _i.startswith("_"):
        continue
    print("!>>" + "hello" + "<<!")
    print(f"__TRANSPILER.VAR.OUT__--N:{_i}--V:{_varlist[_i]};")
