


#değişiklik talebi formu view

def Degisiklik(request):
    Degisiklik_Talep = DegisiklikTalep
    if request.method == 'POST':
        form = Degisiklik_Talep(data=request.POST)

        if form.is.valid():
            Gun = request.POST.get('contact_name')
            Mevcut_Durum = request.POST.get('Mevcut_Durum')
            Talep = request.POST.get('Talep')
            Sebep = request.POST.get('Sebep')
            Degisiklik_Talep = request.POST.get('Degisiklik_Talep')

            template = get_template('')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_content': contact_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "Creative web" + '',
                [''],
                headers={'Reply To': Degisiklik_Talep}
            )

            email.send()

            return redirect('blog:success')
        return render(request, '.html', {'form': Degisiklik_Talep})
