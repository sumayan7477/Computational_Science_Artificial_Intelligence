import csv

def load_energy_data(filename):
    data=[]

    csvfile = open(filename ,"r")
    reader = csv.DictReader(csvfile)

    for row in reader:
        row["kwh_used"]=float(row["kwh_used"])
        data.append(row)

    csvfile.close()
    return data

def appliance_totals(data):
    appliances = {}

    for row in data:
        appliance = row["appliance"]
        kwh = row["kwh_used"]

        if appliance in appliances:
            appliances[appliance]=appliances[appliance]+kwh
        else:
            appliances[appliance] =kwh
    return appliances

def monthly_totals(data):
    months={}

    for row in data:
        month = row["month"]
        kwh = row["kwh_used"]

        if month in months:
            months[month]=months[month]+kwh
        else:
            months[month]=kwh
    return months

def highest_usage_month(monthly_totals):
    if len(monthly_totals)==0:
        return None
    else:
        highest_month = None
        highest_total = 0

        for month in monthly_totals:
            if highest_month is None or monthly_totals[month]>highest_total:
                highest_total = monthly_totals[month]
                highest_month = month
        return highest_month

def appliance_percentage(data , appliance):
    if len(data) == 0:
        return 0.0
    else:
        total_energy = 0
        appliance_energy =0

        for row in  data:
            total_energy = total_energy + row["kwh_used"]

            if row["appliance"] == appliance:
                appliance_energy = appliance_energy+row["kwh_used"]

        if total_energy ==0:
            return 0.0
        else:
            return (appliance_energy / total_energy)*100

def cost_calculation(data, tariff_per_kwh = 0.15):
    total_energy = 0
    for row in data:
        total_energy = total_energy + row["kwh_used"]
    return total_energy * tariff_per_kwh


    

































