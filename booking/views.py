from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from .forms import AccessCodeForm
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from zoneinfo import ZoneInfo
from datetime import datetime
from .models import AccessCode

EDMONTON_TZ = ZoneInfo("America/Edmonton")




def enter_code(request):
    now = timezone.now().astimezone(EDMONTON_TZ)


    if not AccessCode.objects.filter(expires_at__gt=now).exists():
        request.session['has_access'] = True 
        return redirect('appointments')

    if request.method == 'POST':
        form = AccessCodeForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['code'].strip().lower()
            try:
                access_code = AccessCode.objects.get(code__iexact=entered_code)
                if access_code.expires_at > now:
                    request.session['has_access'] = True
                    return redirect('appointments')
                else:
                    form.add_error('code', 'Code has expired')
            except AccessCode.DoesNotExist:
                form.add_error('code', 'Invalid code')
    else:
        form = AccessCodeForm()
    
    return render(request, 'enter_code.html', {'form': form})






def booking_page(request):
    now = timezone.now().astimezone(EDMONTON_TZ)

    has_valid_code = AccessCode.objects.filter(expires_at__gt=now).exists()
    if has_valid_code and not request.session.get('has_access'):
        return redirect('enter_code')

    return render(request, 'booking_page.html')