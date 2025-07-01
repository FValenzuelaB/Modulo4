from clases import Social,Video,Display
from error import SubTipoInvalidoError

a = Social(2,3,"sadsa","2342","subtipo")

v = Video(12,"awa de owo")

d = Display(1,2,"asdsa", "asdsad","subtipo")

print(a ,  v,  d)

a.sub_tipo = "FACEBu"