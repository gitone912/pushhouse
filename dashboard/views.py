from datetime import datetime, timedelta
import io
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from rest_framework.parsers import JSONParser
from dashboard.forms import userdataform
from .models import Plan, Subscription
import json


# Create your views here.
@login_required(login_url='/signin')
def dashboard(request):
    return render(request, 'index.html')

@login_required(login_url='/signin')
def project_dashboard(request):
    return render(request, 'dashboards/projects.html')


@login_required
def select_monthly_plan(request):
    plans = Plan.objects.all()
    subscription = Subscription.objects.filter(user=request.user).first()
    if request.method == 'POST':
        selected_plan_id = request.POST.get('plan')
        if selected_plan_id:
            selected_plan = Plan.objects.get(pk=selected_plan_id)
            start_date = date.today()
            end_date = start_date + timedelta(days=selected_plan.duration)
            if subscription:
                subscription.plan = selected_plan
                subscription.start_date = start_date
                subscription.end_date = end_date
                subscription.save()
            else:
                subscription = Subscription.objects.create(user=request.user, plan=selected_plan, start_date=start_date, end_date=end_date)
            return redirect('/project_dashboard', subscription_id=subscription.id)
    return render(request, 'monthly_plan.html', {'plans': plans})


@login_required
def select_yearly_plan(request):
    plans = Plan.objects.all()
    subscription = Subscription.objects.filter(user=request.user).first()
    if request.method == 'POST':
        selected_plan_id = request.POST.get('plan')
        if selected_plan_id:
            selected_plan = Plan.objects.get(pk=selected_plan_id)
            start_date = date.today()
            end_date = start_date + timedelta(days=selected_plan.duration)
            if subscription:
                subscription.plan = selected_plan
                subscription.start_date = start_date
                subscription.end_date = end_date
                subscription.save()
            else:
                subscription = Subscription.objects.create(user=request.user, plan=selected_plan, start_date=start_date, end_date=end_date)
            return redirect('/project_dashboard', subscription_id=subscription.id)
    return render(request, 'yearly_plan.html', {'plans': plans})


from django.shortcuts import render
import requests
import lxml.etree as ET
import datetime
import csv
from django.http import HttpResponse

def run_script(request):
    import requests
    import lxml.etree as ET
    import datetime
    import csv

    # Get current server time
    now = datetime.datetime.now()

    # Subtract 3 hours from current time
    start_time = now - datetime.timedelta(hours=3)

    # Format server time in the desired format
    start_time_str = start_time.strftime("%Y-%m-%dT"+"07:00:00")

    # Format server time in the desired format
    end_time_str = now.strftime("%Y-%m-%dT%H:%M:%S")

    url = "http://localhost:8010/proxy/servis/SiparisServis.svc"
    headers = {
        "user-agent": "sampleTest",
        "Content-Type": "text/xml;charset=UTF-8",
        "SOAPAction": "http://tempuri.org/ISiparisServis/SelectSepet",
        "Accept-Encoding": "application/xml",
    }

    xml = """
    <x:Envelope
        xmlns:x="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:tem="http://tempuri.org/"
        xmlns:ndf="http://karumrouge.com/servis/SiparisServis.svc?wsdl">
        <x:Header/>
        <x:Body>
            <tem:SelectSepet>
                <tem:UyeKodu>1MAG6YAT4FFLA1FG5Y1UJFQE10JK6T</tem:UyeKodu>
                <tem:sepetId>-1</tem:sepetId>
                <tem:uyeId>-1</tem:uyeId>
                <tem:BaslangicTarihi>{}</tem:BaslangicTarihi>
                <tem:BitisTarihi>{}</tem:BitisTarihi>
            </tem:SelectSepet>
        </x:Body>
    </x:Envelope>
    """.format(start_time_str, end_time_str)

    response = requests.post(url, data=xml, headers=headers)

    root = ET.fromstring(response.text)
    members = []

    for Urunler in root.findall(".//{http://schemas.datacontract.org/2004/07/}WebSepet"):
        UyeID = Urunler.find("{http://schemas.datacontract.org/2004/07/}UyeID").text

        member = {
            'UyeID': UyeID,
        }
        members.append(member)

        filename = "dashboard/data/member_ids_{}.csv".format(now.strftime("%H-%d-%m-%Y"))
        with open(filename, mode='w', newline='') as csv_file:
            fieldnames = ['UyeID']
            writer = csv.DictWriter(csv_file, fieldnames)
            writer.writeheader()
            for member in members:
                if any(val for val in member.values()):
                    writer.writerow(member)

    url2 = "http://localhost:8010/proxy/servis/UyeServis.svc"
    headers = {
        "user-agent": "sampleTest",
        "Content-Type": "text/xml;charset=UTF-8",
        "SOAPAction": "http://tempuri.org/IUyeServis/SelectUyeler",
        "Accept-Encoding": "application/xml",
    }
    members = []
    now = datetime.datetime.now()
    filename = "dashboard/data/member_ids_{}.csv".format(now.strftime("%H-%d-%m-%Y"))
    with open(filename, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            uye_id = row['UyeID']

            xml = """
            <x:Envelope
                xmlns:x="http://schemas.xmlsoap.org/soap/envelope/"
                xmlns:tem="http://tempuri.org/"
                xmlns:ns="http://schemas.datacontract.org/2004/07/">
                <x:Header/>
                <x:Body>
                    <tem:SelectUyeler>
                        <tem:UyeKodu>1MAG6YAT4FFLA1FG5Y1UJFQE10JK6T</tem:UyeKodu>
                        <tem:filtre>
                            <ns:Aktif>-1</ns:Aktif>
                            <ns:AlisverisYapti>-1</ns:AlisverisYapti>
                            <ns:Cinsiyet>-1</ns:Cinsiyet>
                            <ns:MailIzin>-1</ns:MailIzin>
                            <ns:SmsIzin>1</ns:SmsIzin>
                            <ns:UyeID>{}</ns:UyeID>
                        </tem:filtre>
                        <tem:sayfalama>
                            <ns:KayitSayisi>-1</ns:KayitSayisi>
                            <ns:SayfaNo>-1</ns:SayfaNo>
                            <ns:SiralamaDegeri>id</ns:SiralamaDegeri>
                            <ns:SiralamaYonu>Desc</ns:SiralamaYonu>
                        </tem:sayfalama>
                    </tem:SelectUyeler>
                </x:Body>
            </x:Envelope>
            """.format(uye_id)

            response = requests.post(url2, data=xml, headers=headers)
            root = ET.fromstring(response.text)

            # Process the response and extract the relevant information
            for Uye in root.findall(".//{http://schemas.datacontract.org/2004/07/}Uye"):
                CepTelefonu = Uye.find("{http://schemas.datacontract.org/2004/07/}CepTelefonu").text
                Isim = Uye.find("{http://schemas.datacontract.org/2004/07/}Isim").text
                Soyisim = Uye.find("{http://schemas.datacontract.org/2004/07/}Soyisim").text
                SmsIzin = Uye.find("{http://schemas.datacontract.org/2004/07/}SmsIzin").text

                member = {
                    'Isim': Isim,
                    'Soyisim': Soyisim,
                    'SmsIzin': SmsIzin,
                    'CepTelefonu': CepTelefonu,
                    'UyeID': uye_id
                }
                members.append(member)

    # Write the information to a new CSV file
    filename = "dashboard/data/member_data_{}.csv".format(now.strftime("%H-%d-%m-%Y"))
    with open(filename, mode='w', newline='',encoding='utf-8') as csv_file:
        fieldnames = ['Isim', 'Soyisim', 'SmsIzin', 'CepTelefonu', 'UyeID']
        writer = csv.DictWriter(csv_file, fieldnames)

        writer.writeheader()
        for member in members:
            if any(val for val in member.values()):
                writer.writerow(member)

    url3 = "http://localhost:8010/proxy/servis/SiparisServis.svc"
    headers = {
        "user-agent": "sampleTest",
        "Content-Type": "text/xml;charset=UTF-8",
        "SOAPAction": "http://tempuri.org/ISiparisServis/SelectSepet",
        "Accept-Encoding": "application/xml",
    }

    # Get current server time
    now = datetime.datetime.now()

    start_time_str = now.strftime("%Y-%m-%dT"+"07:00:00")

    # Format server time in the desired format
    end_time_str = now.strftime("%Y-%m-%dT%H:%M:%S")

    xml = """
    <x:Envelope
        xmlns:x="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:tem="http://tempuri.org/"
        xmlns:ndf="http://karumrouge.com/servis/SiparisServis.svc?wsdl">
        <x:Header/>
        <x:Body>
            <tem:SelectSepet>
                <tem:UyeKodu>1MAG6YAT4FFLA1FG5Y1UJFQE10JK6T</tem:UyeKodu>
                <tem:sepetId>-1</tem:sepetId>
                <tem:uyeId>-1</tem:uyeId>
                <tem:BaslangicTarihi>{}</tem:BaslangicTarihi>
                <tem:BitisTarihi>{}</tem:BitisTarihi>
            </tem:SelectSepet>
        </x:Body>
    </x:Envelope>
    """.format(start_time_str, end_time_str)

    response = requests.post(url3, data=xml, headers=headers)
    root = ET.fromstring(response.text)

    print(start_time_str)
    print(end_time_str)

    now = datetime.datetime.now()
    filename = "dashboard/data/member_id_and_product-{}.csv".format(now.strftime("%H-%d-%m-%Y"))

    with open(filename, mode='w', newline='' ,encoding="utf-8") as csv_file:
        fieldnames = ['UyeID']
        product_list = []
        max_products_count = 0
        for sepet in root.findall(".//{http://schemas.datacontract.org/2004/07/}WebSepet"):
            product_count = 0
            for urunler in sepet.findall(".//{http://schemas.datacontract.org/2004/07/}WebSepetUrun"):
                product_count += 1
            max_products_count = max(max_products_count, product_count)
        for i in range(max_products_count):
            fieldnames.append("products_{}".format(i+1))
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for sepet in root.findall(".//{http://schemas.datacontract.org/2004/07/}WebSepet"):
            uye_id = sepet.find("{http://schemas.datacontract.org/2004/07/}UyeID").text
            row = {'UyeID': uye_id}
            product_count = 1
            for urunler in sepet.findall(".//{http://schemas.datacontract.org/2004/07/}WebSepetUrun"):
                urun_adi = urunler.find("{http://schemas.datacontract.org/2004/07/}UrunAdi").text
                row["products_{}".format(product_count)] = urun_adi
                product_count += 1
            if row.get("products_1") is not None and row.get("products_1") != "":
                writer.writerow(row)
    print("member_id_and_product-{}.csv olarak kaydedildi.")

    now = datetime.datetime.now()

    # File names
    product_file = "dashboard/data/member_id_and_product-{}.csv".format(now.strftime("%H-%d-%m-%Y"))
    member_file = "dashboard/data/member_data_{}.csv".format(now.strftime("%H-%d-%m-%Y"))
    merged_file = "dashboard/data/merged_data_{}.csv".format(now.strftime("%H-%d-%m-%Y"))

    # Read the first CSV file
    products = []
    with open(product_file, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            products.append(row)

    # Read the second CSV file
    members = []
    with open(member_file, mode='r',encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            members.append(row)

    # Create a dictionary mapping member IDs to products
    product_map = {}
    for product in products:
        uye_id = product['UyeID']
        if uye_id in product_map:
            product_map[uye_id].append(product)
        else:
            product_map[uye_id] = [product]

    # Combine the data from both files
    combined_data = []
    for member in members:
        uye_id = member['UyeID']
        member_products = product_map.get(uye_id, [])
        for product in member_products:
            combined = {**member, **product}
            combined_data.append(combined)

    with open(merged_file, mode='w', newline='',encoding='utf-8') as csv_file:
        fieldnames = list(combined_data[0].keys())
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(combined_data)
        
def test(request):
    now = datetime.datetime.now()
    # with open('dashboard/data/merged_data.csv', 'r',encoding='utf-8') as f:
    #     reader = csv.DictReader(f)
    #     rows = list(reader)

    # # Open the JSON file and write the rows as JSON objects
    # with open('dashboard/data/merged.json', 'w',encoding='utf-8') as f:
    #     json.dump(rows, f,ensure_ascii=False)
    
        # Load the JSON data from the request
    with open('dashboard/data/merged.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
    json_data = data
    json_data_str = json.dumps(json_data , ensure_ascii=False)
    stream = io.BytesIO(json_data_str.encode())
    pythondata = JSONParser().parse(stream)
    serializer = userdataform(data=pythondata, many=True)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        print("form saved")
        # Return a success response
        return redirect('/project_dashboard')
    
    print("form not saved")
    # Render the update data template
    return redirect('/dashboard')
