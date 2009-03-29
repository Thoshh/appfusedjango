Validació Ajax amb Django
==========================

A un dels projectes que estam fent el client va demanar una funcionalitat que
requeria que s'enviàs un formulari al servidor i se'n fessin les validacions,
però que la plana no es tornàs a recarregar. Un treball per Ajax, se'ns dubte.
El problema era que tal com funciona el mecanisme habitual de processament de
formularis amb Django, es requereix que es torni a recarregar la plana.

Una opció podria ser la de fer tota la validació del formulari amb Javascript,
però llavors tendríem el perill de que l'usuari desactivàs el Javascript al
navegador i pogués enviar dades directament sense validar. Podría fer-se tot
per duplicat, és a dir, fer la validació amb Javascript i també al servidor,
però això va en contra de la norma DRY (**Don't repeat yourself**).

Així doncs el que volem és el següent:

 * Enviar el formulari per ajax, però que sigui també possible fer un POST
normal.

 * El servidor ha de fer les validacions i la plana presentar el missatge
d'error si hi ha problemes.

Primer sense javascript
-----------------------

El primer que hem de fer és veure que tot funciona abans de posar-hi el
javascript, així que crearem la nostra aplicació, crearem el formulari i hi
posarem les valicacions que vulguem.

Farem un formulari molt senzill, el típic formulari de contatcte, però ho aprofitarem
per introduïr-hi una opció nova a Django 1.0: la personalització dels missatges
de validació.

<pre class="sh_python">

    from django import forms

    class ContactForm(forms.Form):
        "Defines the login for as in the Django sample"
        subject = forms.CharField(label="subject: *", max_length=100)
        message = forms.CharField(label="Request",
            widget=forms.Textarea(attrs={'rows':'10', 'cols':'80'}))
        email = forms.EmailField(label = "Your email *", max_length=120,
            error_messages = {'required': u"No e-mail, no message"})
        cc_myself = forms.BooleanField(required=False)

        def clean_message(self):
            "We wan't to verify that it containts some words"
            msg = self.cleaned_data['message'].strip()
            if len(msg.split(None)) >5:
                raise forms.ValidationError(u"Really? This is quite short for a message")
            return msg
</pre>

La manera més ràpida de mostrar el formulari és quelcom com

<pre>
    &lt;table>
    &lt;form action='.' method="POST">
    {{form}}
    &lt;tr>&lt;td span="2">&lt;input type="submit" value="send" name="enviar" />&lt;/td>&lt;/tr>
    &lt;/form>
    &lt;/table>
</pre>

Però té un problema, que no controlam on es posen els missatges d'error i nosaltres
volem controlar-ho. En aquest cas, i per simplicitat, posarem tots els missatges
d'error a la part superior de la pantalla. Així que hem de rescriure la plantilla
per a que ho contempli.

El nostre formulari queda doncs com

<pre>
    {% if form.errors %}
        {{ form.errors }}
    {% endif %}
    &lt;table>
    &lt;form action='.' method="POST" >
    &lt;tr>&lt;td>{{form.subject.label}}&lt;td>{{form.subject}}&lt;/td>&lt;/tr>
    &lt;tr>&lt;td>{{form.message.label}}&lt;td>{{form.message}}&lt;/td>&lt;/tr>
    &lt;tr>&lt;td>{{form.email.label}}&lt;td>{{form.email}}&lt;/td>&lt;/tr>
    &lt;tr>&lt;td>{{form.cc_myself.label}}&lt;td>{{form.cc_myself}}&lt;/td>&lt;/tr>
    &lt;tr>&lt;td span="2">&lt;input type="submit" value="send" name="enviar" />&lt;/td>&lt;/tr>
    &lt;/form>
    &lt;/table>
</pre>

És a dir, ara tenim exactament el que teníem abans (no us hi fixeu amb la maquetació),
però ara si hi ha errors es presentaran a la part superior del formulari.

Concentrem-nos ara en la manera de presentar els errors. Com que la nostra idea
és que es puguin mostrar els errors que venguin per Ajax, el que farem és no
presentar-los així, sinó que els posarem dins un div i farem que aquest es presenti
o no en funció de si hi ha errors.

<pre>
    {% block errors %}
    &lt;div class="errores" {% if not form.errors %} style="display: none" {% endif %} >
      &lt;p id="error_msg">
          {{form.errors}}
      &lt;/p>
    &lt;/div>
    {% endblock errors %}
</pre>

Això a efectes pràctics és el mateix que el cas anterior, ja que com que si no
hi ha errors <code>from.errors</code> no mostrarà res. El que sí hi ha ja és
tota l'estructura que ens servirà per mostrar els errors dins l'arbre DOM de la
plana web.

I ara i afegim l'Ajax
----------------------

Necessitam tres coses: enviar el formulari per ajax, que si hi ha errors de
validació els puguem presentar i que si tot va bé es faci la redirecció cap
a la plana que toqui.

Hi ha alguns projectes que volen fer aquest tipus de coses de manera més o manco
genèrica, però ara per ara no n'hi ha cap que em convenci, així que millor ho
feim a mà. Si més no us deixo alguns enllaços:

 * [Ajax form with jQuery]("un snippet", http://www.djangosnippets.org/snippets/992/)
 * [Django-ajax-forms]("un projecte", http://code.google.com/p/django-ajax-forms/)

El que sí faré es manllevar codi d'aquests projectes per als nostres propòsits.

En concret, adaptam el codi que ens permet obtenir els errors i passar-los a una
estructura json:


<pre class="sh_python">

    class LazyEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Promise):
                return force_unicode(obj)
            return obj

    def validate(request, form, new_url=''):
        if form.is_valid():
            data = {
                'valid': True,
                'url': new_url
            }
        else:
            if request.POST.getlist('fields'):
                fields = request.POST.getlist('fields') + ['__all__']
                errors = dict([(key, val) for key, val in form.errors.iteritems() if key in fields])
            else:
                errors = form.errors
            final_errors = {}
            for key, val in errors.iteritems():
                if key == '__all__':
                    final_errors['__all__'] = val
                if not isinstance(form.fields[key], forms.FileField):
                    html_id = form.fields[key].widget.attrs.get('id') or form[key].auto_id
                    html_id = form.fields[key].widget.id_for_label(html_id)
                    final_errors[html_id] = val
            data = {
                'valid': False,
                'url': new_url,
                'errors': final_errors,
            }
        json_serializer = LazyEncoder()
        return HttpResponse(json_serializer.encode(data), mimetype='application/json')
</pre>

El *validate* és una funció prou genèrica, ens tornará una variable, **valid** que ens
indicarà si hi ha errors de validació o no, la url on s'ha de redireccionar i
la matriu d'errors.

Django ja posa al request una variable per indicar-nos si la petició s'ha fet per
HttpRequest o no, **request.is_ajax()** això ens permetrà distingir com s'ha
enviat el post i fer la validació d'una manera o altra

<pre class="sh_python">

    def index(request):
        redirect_url = '/thanks'
        if request.method == 'POST':
            contact_form = ContactForm(request.POST)
            if request.is_ajax():
                return validate(contact_form, redirect_url)
            else:
                if contact_form.is_valid():
                # do whatever you need as everything is valid
                    return HttpResponseRedirect(redirect_url)
        else:
            contact_form = ContactForm()
        return render_to_response('index.html', {'form': contact_form})
</pre>

El codi del view.py és d'allò més senzillet, sols feim que si la petició ve per
post, tornam una cosa o altra en funció de si aquesta és una petició Ajax o si
és una petició normal.

Fins ara no hem posat gens de javascript i tot segueix funcionant amb normalitat.

És temps de posar-ho les llibreries javascript. Ho farem amb jQuery, que és la que tenc més
per mà, supòs que amb altres llibreries no hi ha d'haver cap problema, i a més
faré server un plugin força bo per al tractament de formularis amb jQuery, el
[jQuery Form Plugin](http://malsup.com/jquery/form/).

Com presentar els missatges, si s'han de presentar tots, els efectques que volguem,
ja es cosa nostra. El json el que ens torna és l'identificador del camp i una
matriu amb tots els errors que hi hagi. El procés que facem ja és cosa nostra.

<pre class="sh_javascript">
    $(document).ready(function(){
            form_options = {
              timeout: 3000,
              dataType: 'json',
              type: 'POST',
              beforeSubmit: function(formData, jqForm, options) {
                  // you can add additional validation here and return
                  // false if it's not valid
                  jQuery('#boton').toggle();
              },
              success: function(responseJson, statusText) {
                  if (responseJson.valid) {
                     // redirect to hte new url
                     document.location.href = responseJson.url;
                  } else {
                      // create the error structure
                      var msg = ""
                      for (key in  responseJson.errors) {
                        camp = key.split('_')[1];
                        msg = msg + camp+":"+responseJson.errors[key][0]+"&lt;br/>";
                      }
                      $('#error_msg').html(msg+'&lt;br/>');
                      $('.errores').show(100);
                      jQuery('#boton').toggle();
                  }
              }
            };
            $('#testform').ajaxForm(form_options);
    });
</pre>

A l'exemple el que he fet és montar un missatge amb el primer error de cada camp sols
a efectes demostratius, podeu fer el que us vengui millor: validar abans d'enviar,
mostrar efectes als camps dels errors, mostrar un diàleg, sols estau limitats
per la vostra imaginiació i el Javascript.

El [codi complet de l'exemple](http://code.google.com/p/appfusedjango/source/browse/#svn/trunk/ajax_validation)
 l'he pujat al [projecte appfusedjango](http://code.google.com/p/appfusedjango/)