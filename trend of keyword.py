
import pandas as pd



df = pd.read_csv('../prj_sns_trend_private/crawling_from20200101_to20201015.csv')
df.drop([df.columns[0]],axis=1, inplace=True)


keywords = ['BHC']
b = []


for i in range(len(df)):
    print(df['title'][i])



#    if keywords in df['title'][i]:
#       b.append(df['title'][i])


for a in range(len(df)):
    b = a+1
    new_title = []
    new_date = []
    if df['title'][a] == df['title'][b]:
        pass
    else:
        new_title.append(df['title'][a])
        new_date.append(df['date'][a])

    if df['comment'][a] == df['comment'][b]:
        new_title.append(df['comment'][b])
    else:
        pass
