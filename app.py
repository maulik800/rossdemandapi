try:
    from flask import Flask, request,render_template
    # from azure.storage.blob import BlockBlobService
    import time
    import json
    import requests
    app = Flask(__name__)


    @app.route('/testpy', methods=['GET'])
    def result():
        store = request.args.get("Storeid")
        print(store)
        dayofweek = request.args.get("DayOfWeek")
        customer = request.args.get("Customers")
        ShipmentCost = request.args.get("ShipmentCost")
        timesegment = request.args.get("TimeSegment")
        tenderstatus = request.args.get("TenderStatus")
        checkstatus = request.args.get("CheckIn")
        day = request.args.get("Day")
        month = request.args.get("Month")
        year = request.args.get("Year")
        storetype = request.args.get("StoreType")
        assortment = request.args.get("Assortment")
        compdist = request.args.get("CompetitionDistance")
        compmonth = request.args.get("CompetitionOpenSinceMonth")
        compyear = request.args.get("CompetitionOpenSinceYear")
        promo = request.args.get("Promo2")
        promoyear = request.args.get("Promo2SinceYear")
        promoweek = request.args.get("Promo2SinceWeek")
        dic = {}
        dic['Store']=int(store)
        dic['DayOfWeek'] = int(dayofweek)
        dic['Customers']= int(customer)
        dic['Shipment costs relevance']=int(ShipmentCost)
        dic['Time segment exists']=int(timesegment)
        dic['Tender Status'] = int(tenderstatus)
        dic['Status of check-in']=int(checkstatus)
        dic['Day which record Was Created']=int(day)
        dic['Month on which record Was Created']=int(month)
        dic['Year on which record Was Created']=int(year)
        dic['StoreType']=int(storetype)
        dic['Assortment']=int(assortment)
        dic['CompetitionDistance']=int(compdist)
        dic['CompetitionOpenSinceMonth']=int(compmonth)
        dic['CompetitionOpenSinceYear']=int(compyear)
        dic['Promo2']=int(promo)
        dic['Promo2SinceWeek']=int(promoweek)
        dic['Promo2SinceYear']=int(promoyear)
        print(dic)
        URL = "http://7bd6b1e5-7b7a-4438-b00a-4eea149b8103.eastus.azurecontainer.io/score"
        string_json = json.dumps(dic)
        print(string_json)
        PARAMS = string_json
        print(URL)
        print(PARAMS)
        r = requests.get(url = URL, params = PARAMS)
        print(r.url)
        print(r)
        data = r.json()
        print(data)
        data_new = data[0]
        return data_new
        # return "Modified on: "+str(resp.last_modified)

    @app.route('/')
    def home():
        return render_template('form.html')
    if __name__ == '__main__':
        app.run(debug = "false")

except Exception as e:
    file1 = open("Erros.txt","w")
    file1.write(str(e))
    file1.close()
