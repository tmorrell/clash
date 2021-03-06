import glob
import p3d.protein

def clash(pdb,resids):
    searchstr = ''
    for r in resids:
        searchstr = searchstr + ' resid ' + str(r) + ' or '
    searchstr = searchstr[0:-3] #remove extra or
    newp = p3d.protein.Protein(pdb)

    res = newp.query(searchstr)
    clash = len(newp.query('within 1.0 of ',res,' and not ',res))
    #for j in newp.query('within 1.0 of ',fu,' and not ',fu):
    #    print(j.resid,j.atype)
    if clash > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    pdbs = glob.glob('pdbs/*')
    for p in pdbs:
        print(p)
        print(clash(p,[266,517,653,706,872,930]))

