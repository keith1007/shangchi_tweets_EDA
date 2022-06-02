import twint

c = twint.Config()
c.Search = "Shang-Chi OR Shang Chi OR ShangChi OR #shangchi OR #ShangChi"
c.Since ='2021-09-01'
c.Until ='2021-10-01'
c.Limit = None
c.Store_csv = True
c.Hide_output = True
c.Output = "ShangChiUpdated2.csv"
c.Lang = "en"
c.Translate = False
twint.run.Search(c)


