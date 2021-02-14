from viaduct import ISA
from viaduct import Public
from viaduct.utils import *

test = ISA("email", "pass", Reality.Real,
           browserPath=r"C:\Program Files\Mozilla Firefox\firefox.exe")
# print(test.getSettings(code="GYMl_EQ"))
# print(test.getFundamentals(isin="US36467W1099"))
#print(test.getInstrument(code="TSLA"))
#print(test.getChartData("TSLA", 1, 5))
#print(test.getPortfolioPerformance("LAST_YEAR"))

public = Public(loadSymbols=False)
#print(public.getChartData(code=public.getCode(isin="US4592001014"), chartPeriod=ChartPeriod.H1, size=5))
account = test.getPortfolioPerformance(HistoryTimeframe.Y1)
#print(account)

x = []
y = []
y2 = []
y3 = []

for i in account["snapshots"]:
    x.append(i["time"])
    y.append(i["ppl"])
    y2.append(i["result"])
    y3.append(i["investment"])

plt.plot(x, y, label="ppl")
plt.plot(x, y2, label="result")
plt.plot(x, y3, label="investment")
plt.legend()
plt.show()