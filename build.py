def build(gen, env):
    env = env.clone()

    env['CPPFLAGS'] += [
        '-D__linux__=1',
        '-D_GNU_SOURCE',
        '-D_TPMCPPLIB',
    ]
    env['CPPPATH'] += [
        'src/libs/tss/TSS.CPP/include',
        'src/libs/openssl/include',
    ]

    # shut off warnings
    env['CXXFLAGS'] += [
        '-Wno-sign-conversion',
        '-Wno-unused-parameter',
        '-Wno-unused-variable',
        '-Wno-parentheses',
        '-Wno-type-limits',
    ]

    files = env.glob('TSS.CPP/Src/*.cpp')
    lib = env.static_lib(gen, out = 'libtss', ins = files)
    env.install(gen, env['LIBDIR'], lib)
