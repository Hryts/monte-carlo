from system import System


if __name__ == '__main__':
    DIMENSIONS = 3
    L = 2

    SYSTEM = System(L, DIMENSIONS)
    print(SYSTEM)
    MODIFIED = True

    while MODIFIED:
        MODIFIED = next(SYSTEM.simulate())
        print(SYSTEM)
