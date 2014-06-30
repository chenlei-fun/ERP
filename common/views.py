from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from reportlab.pdfgen import canvas
from django.template import Template, RequestContext
from django.conf import settings
from rlextra.rml2pdf import rml2pdf
import cStringIO
from reportlab.pdfbase import pdfmetrics, ttfonts

# Create your views here.

def login(request):
    if request.method == "POST" :
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/distributor/list/')
    else:
       return render_to_response("registration/Login.html",context_instance = RequestContext(request))

def logout(request):
    auth.logout(request)

# Create your views here.
def hello_pdf(request):

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Create the PDF object, using the StringIO object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 50, "Oh My Baby!")
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    return response


def search_form(request):
    return render_to_response('search_form.html')


def getPDF(request):
    """Returns PDF as a binary stream."""

    pdfmetrics.registerFont(ttfonts.TTFont("song", "simsun.ttc"))

    if 'q' in request.GET:

        rml = getRML(request.GET['q'])

        buf = cStringIO.StringIO()

        #create the pdf
        rml2pdf.go(rml, outputFileName=buf)
        buf.reset()
        pdfData = buf.read()

        #send the response
        response = HttpResponse(mimetype='application/pdf')
        response.write(pdfData)
        response['Content-Disposition'] = 'attachment; filename=output.pdf'
        return response

def getRML(name):
    """We used django template to write the RML, but you could use any other
    template language of your choice.
    """
    t = Template(open('test.rml').read())
    c = RequestContext({"name": name,'STATIC_DIR': settings.STATIC_PATH,})
    rml = t.render(c)
    #django templates are unicode, and so need to be encoded to utf-8
    return rml.encode('utf8')