from django.http import HttpResponse
from django.template import Template, Context

def search(request):
    extern_doc =  open("/Users/alejandrotero/Documents/UTEC/Ciclo 6/BD2/Proyecto2_Hito1_BD2/web_page/front_end/front_end/templates/search.html")
    template = Template(extern_doc.read())
    extern_doc.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)