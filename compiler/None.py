_varlist = globals().copy()
for _i in _varlist.keys():
	if _i.startswith("_"):
		continue
	print(f"__TRANSPILER.VAR.OUT__--N:{_i}--V:{_varlist[_i]};")