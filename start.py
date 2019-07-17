import datetime

from flask import Flask, request, escape, jsonify, json, url_for, render_template, make_response, Response
from dataObjects import account, csvhandler, client, transaction
from flask_cors import CORS

saveDirectory = '/home/craigg/cpdUpload/'

app = Flask(__name__)
CORS(app)

@app.route('/import')
def zaza():
    csvhandler.csvhandler.parseItem('/home/craigg/Downloads/Transaction.csv')
    csvhandler.csvhandler.parseItem('/home/craigg/Downloads/Account.csv')
    csvhandler.csvhandler.parseItem('/home/craigg/Downloads/Client.csv')
    return ''


@app.route('/import', methods=['POST'])
def accountImport():
    file = request.files['file']
    fname = file.filename
    if fname in ('Transaction.csv', 'Client.csv', 'Account.csv'):
        file.save(saveDirectory+file.filename)
        csvhandler.csvhandler.parseItem(saveDirectory+file.filename)
    else:
        Flask.abort(404, 'Could not find a location for the specified file')
    return "happy days"


@app.route('/logon', methods=['POST'])
def accountLogon():
    content = request.get_json(silent=True)
    cli = client.Client();
    cli.logon(content['username'], content['password'])
    if cli.clientid:#ok we found something... lets get the accounts.
        acc = account.Account()
        items = acc.getAccountsByClientID(cli.clientid)
        return make_response(jsonify(accounts=[i.serialize() for i in items]))
    return Response('{"status":"account_not_found"}', status=404, mimetype='application/json')


@app.route('/balance', methods=['POST'])
def getBalance():
    content = request.get_json(silent=True)
    accountIdentity = content['account']
    acc = account.Account()
    balance = acc.queryBalance(accountIdentity)
    return make_response(jsonify({"balance": balance}))


@app.route('/withdraw', methods=['POST'])
def makeWithdrawel():
    content = request.get_json(silent=True)
    accountIdentity = content['account']
    amount = content['amount']
    date = datetime.datetime.today()
    acc = account.Account()
    balance = acc.queryBalance(accountIdentity)
    if balance < int(amount):
        return make_response(jsonify({"error":"1","message":"balance too low"}))
    trans = transaction.Transaction()
    trans.save(date, int(amount)*-1, accountIdentity)
    balance = acc.queryBalance(accountIdentity)
    return make_response(jsonify({"balance": balance}))



@app.route('/',methods=['GET'])
def index():
    return render_template('page.html')


app.run('127.0.0.1', '5000', debug=True)