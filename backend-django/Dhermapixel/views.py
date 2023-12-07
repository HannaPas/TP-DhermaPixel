from django.views.generic import TemplateView

class dhermapixel(TemplateView):
    template_name = "index.html"
    
class promociones(TemplateView):
    template_name = "pages/promociones.html"

class tratamientos(TemplateView):
    template_name = "pages/tratamientos.html"
    
class contacto(TemplateView):
    template_name = "pages/contacto.html"

class inicioDeSesión(TemplateView):
    template_name = "pages/inicioDeSesión.html"
    
class dermapen(TemplateView):
    template_name = "pages/dermapen.html"

class prp(TemplateView):
    template_name = "pages/prp.html"
    
class hialuronico(TemplateView):
    template_name = "pages/hialuronico.html"

class meso(TemplateView):
    template_name = "pages/meso.html"
    
class mesoterapiaCapilar(TemplateView):
    template_name = "pages/mesoterapia-capilar.html"

class criolipolisis(TemplateView):
    template_name = "pages/Criolipolisis.html"
    
class registro(TemplateView):
    template_name = "pages/registro.html"