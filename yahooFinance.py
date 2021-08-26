
import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import  requests
from urllib.request import urlopen
import mechanicalsoup

statistics = "https://finance.yahoo.com/quote/{}/key-statistics?p={}"
profile = "https://finance.yahoo.com/quote/{}/profile?p={}"
financials = "https://finance.yahoo.com/quote/{}/financials?p={}"

stock = "MCD"
response = requests.get(financials.format(stock,stock))
soup = BeautifulSoup(response.text,'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
scriptData = soup.find('script',text=pattern).contents[0]
jsonData = json.loads(scriptData[scriptData.find("context")-2:-12])

annualIncomeStatementJson = jsonData["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["incomeStatementHistory"]["incomeStatementHistory"]
quarterlyIncomeStatementJson = jsonData["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["incomeStatementHistoryQuarterly"]["incomeStatementHistory"]
annualCashFlowJson = jsonData["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["cashflowStatementHistory"]["cashflowStatements"]
quarterlyCashFlowJson = jsonData["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["cashflowStatementHistoryQuarterly"]["cashflowStatements"]
annualBalanceSheetJson = jsonData["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["balanceSheetHistory"]["balanceSheetStatements"]
quarterlyBalanceSheetJson = jsonData["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["balanceSheetHistoryQuarterly"]["balanceSheetStatements"]

def getAnnualIncomeStatement(stock):
    link = "https://finance.yahoo.com/quote/{}/financials?p={}"
    response = requests.get(link.format(stock,stock))
    soup = BeautifulSoup(response.text, 'html.parser')
    pattern = re.compile(r'\s--\sData\s--\s')
    scriptData = soup.find('script', text=pattern).contents[0]
    jsonData = json.loads(scriptData[scriptData.find("context") - 2:-12])
    annualIncomeStatementJson = jsonData["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["incomeStatementHistory"]["incomeStatementHistory"]
    result = {}
    for i in annualIncomeStatementJson:
        index = i["endDate"]['fmt']
        result[index]={}
        result[index]["Total Revenue"]=i["totalRevenue"]['raw']
        result[index]["Cost of Revenue"]=i["costOfRevenue"]['raw']
        result[index]["Gross Profit"]=i["grossProfit"]['raw']
        result[index]["Net Income"]=i["netIncome"]['raw']
        result[index]["Pretax Income"] = i["incomeBeforeTax"]['raw']
        result[index]["Operating Expenses"] = i["sellingGeneralAdministrative"]['raw']
        result[index]["Interest Expense Non Operating"] = i["interestExpense"]['raw']
        result[index]["Net Income from Continuing Operations"] = i["netIncomeFromContinuingOps"]['raw']
    return result

def getStats(stock):
    link = "https://finance.yahoo.com/quote/{}/key-statistics?p={}"
    response = requests.get(link.format(stock, stock))
    soup = BeautifulSoup(response.text, 'html.parser')
    pattern = re.compile(r'\s--\sData\s--\s')
    scriptData = soup.find('script', text=pattern).contents[0]
    jsonData = json.loads(scriptData[scriptData.find("context") - 2:-12])
    statsJson = jsonData["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]
    result={}
    result["PEG Ratio(5 yr expected)"]=statsJson["defaultKeyStatistics"]["pegRatio"]["raw"]
    result["Forward P/E"] = statsJson["defaultKeyStatistics"]["forwardPE"]["raw"]
    result["Payout Ratio"]=statsJson["summaryDetail"]["payoutRatio"]["raw"]
    result["Forward Annnual Dividend Yield"]=statsJson["summaryDetail"]["dividendYield"]["raw"]
    return result

zeb = ["NA.TO","CM.TO","BMO.TO","RY.TO","TD.TO","BNS.TO"]

def getStatsFromIndex(index):
    l = {}
    for i in index:
        l[i]=getStats(i)
    return l

h = getAnnualIncomeStatement("FB")
j = 1
'''
url = "http://olympus.realpython.org/login"
browser = mechanicalsoup.Browser()
loginPage = browser.get(url)
loginhtml = loginPage.soup

form = loginhtml.select("form")[0]
form.select("input")[0]["value"]="zeus"
form.select("input")[1]["value"]="ThunderDude"

profilePage = browser.submit(form,url)
print(profilePage.soup.title)
'''


