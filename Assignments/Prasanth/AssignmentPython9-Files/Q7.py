import sys
file_name=sys.argv[1:]
try:
    with open(file_name[0],'r') as f:
        content=f.read()
        res={}
        for i in content:
            res[i]=1+res.get(i,0)
        print(res)
except Exception as err:
    print(err)