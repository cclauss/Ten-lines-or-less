def set_theory(abc, ac, cde):
    print(f"abc: {sorted(abc)}\n ac: {sorted(ac)}\ncde: {sorted(cde)}")
    print(f"Union:                abc | cde --> {sorted(abc | cde)}")
    print(f"Intersection:         abc & cde --> {sorted(abc & cde)}")
    print(f"Set difference:       abc - cde --> {sorted(abc - cde)}")
    print(f"Symmetric difference: abc ^ cde --> {sorted(abc ^ cde)}")
    print(
        "Is suubset:           ac <= abc, abc <= abc --> {}, {}".format(
            ac <= abc,
            abc <= abc,
        ),
    )
    print(
        "Is superset:          abc >= ac, abc >= abc --> {}, {}".format(
            abc >= ac,
            abc >= abc,
        ),
    )
    print(
        "Is proper suubset:    ac  < abc, abc <  abc --> {}, {}".format(
            ac < abc,
            abc < abc,
        ),
    )
    print(
        "Is proper superset:   abc >  ac, abc >  abc --> {}, {}".format(
            abc > ac,
            abc > abc,
        ),
    )


if __name__ == "__main__":
    # --> ['a', 'b', c'] with duplicate c's will be thrown away
    abc = {"a", "b", "c", "c", "c"}
    ac = abc - {"b"}  # --> ['a', 'c'] with 'b' removed
    cde = {"c", "d", "e"}
    set_theory(abc, ac, cde)

"""
abc: ['a', 'b', 'c']
 ac: ['a', 'c']
cde: ['c', 'd', 'e']
Union:                abc | cde --> ['a', 'b', 'c', 'd', 'e']
Intersection:         abc & cde --> ['c']
Set difference:       abc - cde --> ['a', 'b']
Symmetric difference: abc ^ cde --> ['a', 'b', 'd', 'e']
Is suubset:           ac <= abc, abc <= abc --> True, True
Is superset:          abc >= ac, abc >= abc --> True, True
Is proper suubset:    ac  < abc, abc <  abc --> True, False
Is proper superset:   abc >  ac, abc >  abc --> True, False
"""
