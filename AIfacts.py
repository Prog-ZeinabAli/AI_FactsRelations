from logpy import run,var,Relation,facts,conde
father=Relation();
mother=Relation();
facts(father, ('John','William'),
                 ('John', 'David'),
                 ('John', 'Adam'),
                 ("William", "Chris"),
                 ("William", "Stephanie"),
                 ("David","Wayne"))
facts(mother,('majda','zeinab'),
              ('majda','leila'),
              ('majda','William'))
x=var()

y=var()
print run(0,y,mother('majda',y))


def parent(x,y):
    return conde([mother(x,y)],[father(x,y)])

z=run(0,x,parent(x,'William'))
print z

def grandparetn(x,y):
   temp=var()
   return conde([father(temp,y)],[father(x,temp)])

q=var()
print run(0,x,grandparetn(x,'chris'))
