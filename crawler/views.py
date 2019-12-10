import datetime
from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from selenium import webdriver
from selenium.common import exceptions
from crawler.models import Schedule
from crawler.serializers import ScheduleSerializer
# Create your views here.


class BookingView(APIView):

    def post(self, request):
        browser = webdriver.Chrome('/usr/bin/chromedriver/chromedriver')
        browser.get('https://www.hapag-lloyd.com/en/home.html')
        login_toggle = browser.find_element_by_id('loginlink')
        login_toggle.click()
        email_field = browser.find_element_by_id('login_f:hl8')
        # email_field.click()
        browser.execute_script("arguments[0].click();", email_field)
        email_field.send_keys(settings.HAPAGLLOYD_EMAIL)
        password_field = browser.find_element_by_id('login_f:hl13')
        # password_field.click()
        browser.execute_script("arguments[0].click();", password_field)
        password_field.send_keys(settings.HAPAGLLOYD_PASSWORD)
        login_btn = browser.find_element_by_id('login_f:hl14')
        # login_btn.click()
        browser.execute_script("arguments[0].click();", login_btn)
        nav_links = browser.find_elements_by_css_selector('nav.hal-navigation-list.hal-navigation-list--main .hal-navigation-item .hal-rtl--alt')
        booking_link = nav_links[86]
        booking_link.click()
        booking_table = browser.find_element_by_id('booking_s9820_f:hl134')
        bk_tbody = booking_table.find_element_by_tag_name('tbody')
        bk_rows = bk_tbody.find_elements_by_tag_name('tr')
        for row in bk_rows:
            data = row.find_elements_by_tag_name('td')
            booking_num = int(data[1].text)
            customer_reference = data[2].text
            loading_port = data[3].text
            departure_date_txt = data[4].text
            departure_date = datetime.datetime.strptime(departure_date_txt, '%Y-%m-%d')
            vessel = data[5].text
            discharge_port = data[6].text
            creation_date_txt = data[7].text
            creation_date = datetime.datetime.strptime(creation_date_txt, '%Y-%m-%d')
            created_by = data[8].text
            try:
                booking = Schedule.objects.get(booking_number=booking_num)
            except Schedule.DoesNotExist:       
                booking = Schedule.objects.create(
                    booking_number=booking_num,
                    customer_reference=customer_reference,
                    loading_port=loading_port,
                    vessel_departure=departure_date,
                    vessel_name=vessel,
                    discharge_port=discharge_port,
                    created_date=creation_date,
                    created_by=created_by
                )
        bookings = Schedule.objects.all()
        browser.quit()
        serialized_data = ScheduleSerializer(bookings, many=True)
        return Response(
            {
                'status': 'success',
                'data': serialized_data.data
            },
            status=status.HTTP_200_OK
        )
