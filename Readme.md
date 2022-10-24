# Running `mod1` through pants

The file `src/mod1/BUILD` includes `src:dist_info` as dependency, allowing `mod1` to find the entry point
`myentrypoint = mod2:a`. However, `mod1` does not explicitly depend on `mod2`, so `mod2` is not found in its
execution environment:

    $ ./pants run src/mod1:mod1
    EntryPoint(name='myentrypoint', value='mod2:a', group='mygroup')
    Traceback (most recent call last):
    File "/home/dba2hi/.cache/pants/named_caches/pex_root/venvs/4cba44b7a8cd020f88a564de7661ae4c501a299d/1299f19e99b0881f9442f8df4bf8071cddae4678/pex", line 235, in <module>
        runpy.run_module(module_name, run_name="__main__", alter_sys=True)
    File "/software/Modules/installations/python/3.8.5/lib/python3.8/runpy.py", line 207, in run_module
        return _run_module_code(code, init_globals, run_name, mod_spec)
    File "/software/Modules/installations/python/3.8.5/lib/python3.8/runpy.py", line 97, in _run_module_code
        _run_code(code, mod_globals, init_globals,
    File "/software/Modules/installations/python/3.8.5/lib/python3.8/runpy.py", line 87, in _run_code
        exec(code, run_globals)
    File "/tmp/pants-sandbox-igaRTD/src/mod1/__init__.py", line 10, in <module>
        main()
    File "/tmp/pants-sandbox-igaRTD/src/mod1/__init__.py", line 6, in main
        func = ep.load()
    File "/software/Modules/installations/python/3.8.5/lib/python3.8/importlib/metadata.py", line 77, in load
        module = import_module(match.group('module'))
    File "/software/Modules/installations/python/3.8.5/lib/python3.8/importlib/__init__.py", line 127, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
    File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
    File "<frozen importlib._bootstrap>", line 991, in _find_and_load
    File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
    ModuleNotFoundError: No module named 'mod2'

# Running `mod1` through package installation

    $ ./pants package src:mypkg
    20:19:05.55 [INFO] Completed: Building build_backend.pex from setuptools_default.lock
    20:19:06.09 [INFO] Wrote dist/mypkg-1.0.0-py3-none-any.whl
    20:19:06.09 [INFO] Wrote dist/mypkg-1.0.0.tar.gz
    $ ./pants export ::
    Wrote virtualenv (using Python 3.8.5) to dist/export/python/virtualenv
    Wrote virtualenv for the tool 'pytest' to dist/export/python/virtualenvs/tools
    $ source dist/export/python/virtualenv/3.8.5/bin/activate
    (3.8.5) $ pip install dist/mypkg-1.0.0-py3-none-any.whl
    Processing ./dist/mypkg-1.0.0-py3-none-any.whl
    Installing collected packages: mypkg
    Successfully installed mypkg-1.0.0
    (3.8.5) $ mod1
    EntryPoint(name='myentrypoint', value='mod2:b', group='mygroup')
    b()
    (3.8.5) $

Here the entry point is found, as defining `"myentrypoint": "mod2:b"` in the `python_distribution` in `src/BUILD` makes
it a dependency and it is included in the wheel file.
