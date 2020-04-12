from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.utils import timezone
from .models import Donation
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models.functions import ExtractYear
from django.db.models import Sum
import logging
import stripe

stripe.api_key = "sk_test_7yuG2RAv7UCVvUVJZUXbmmd400jMvg3Ckz"

# Get an instance of a logger
logger = logging.getLogger(__name__)

@login_required
def donation(request):
	return render(request, 'donation.html')

@login_required
def charge(request):
	logger.info("charging...")
	if request.method == 'POST':
		logger.info('Data:', request.POST)

		customer = stripe.Customer.create(
			name = request.user.first_name,
			email = request.user.email,
			source  = request.POST['stripeToken']
		)

		amount=int(request.POST["amount"])

		charge = stripe.Charge.create(
			customer = customer,
			amount = amount,
			currency = "jpy",
			description = "Donation",
		)

		donation = Donation.objects.create(donator=request.user, donate_amount=amount, donate_time=timezone.now())
		donation.save()

	return redirect('charge_success')

@login_required
def charge_success(request):
	return render(request, 'charge_success.html')


@login_required
def update_chart(request):

	years_list  =  []
	queryset = Donation.objects.annotate(years=ExtractYear('donate_time')).values('years')
	for year in queryset:
		years_list.append(year["years"])

	years =  list(dict.fromkeys(years_list))

	donate_amount  =  []
	queryset = Donation.objects.annotate(years=ExtractYear('donate_time')).values('years').annotate(donate_amount_sum=Sum('donate_amount'))
	for amount in queryset:
		donate_amount.append(amount["donate_amount_sum"])

	return JsonResponse(data={
		'years': years,
		'donate_amount': donate_amount,
	})
