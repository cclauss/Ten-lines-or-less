def set_theory(abc, ac, cde):
    print('abc: {}\n ac: {}\ncde: {}'.format(sorted(abc), sorted(ac), sorted(cde)))
    print('Union:                abc | cde --> {}'.format(sorted(abc | cde)))
    print('Intersection:         abc & cde --> {}'.format(sorted(abc & cde)))
    print('Set difference:       abc - cde --> {}'.format(sorted(abc - cde)))
    print('Symmetric difference: abc ^ cde --> {}'.format(sorted(abc ^ cde)))
    print('Is suubset:           ac <= abc, abc <= abc --> {}, {}'.format(ac <= abc, abc <= abc))
    print('Is superset:          abc >= ac, abc >= abc --> {}, {}'.format(abc >= ac, abc >= abc))
    print('Is proper suubset:    ac  < abc, abc <  abc --> {}, {}'.format(ac < abc, abc < abc))
    print('Is proper superset:   abc >  ac, abc >  abc --> {}, {}'.format(abc > ac, abc > abc))

if __name__ == '__main__':
    abc = {'a', 'b', 'c', 'c', 'c'}  # --> ['a', 'b', c'] with duplicate c's will be thrown away
    ac = abc - {'b'}                 # --> ['a', 'c'] with 'b' removed
    cde = {'c', 'd', 'e'}
    set_theory(abc, ac, cde)

'''
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
'''
