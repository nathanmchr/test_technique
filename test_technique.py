import pandas as pd
df = pd.read_csv("C:/Users/natha/Downloads/Test Alternance/train.csv")



def dangerFeatures(df): #retourne une liste de features avec comme valeurs un taux de dangerosité entre 0 et 1
    com=[]
    pois=[]
    dangerFeat=[]

    for i in range(len(df)): #balayage du dataset rangeant dans une liste "pois" les features des champignons vénéneux et dans une liste "com" les features des champignons comestibles 
        for j in range(len(df.columns)):
            if df.iloc[i,0]=='p':
                pois.append(df.iloc[i,j])
            else:
                com.append(df.iloc[i,j])
    
    for i in pois:  #remplit la liste dangerFeat avec les features auxquelles on attribue un taux de dangerosité entre 0 et 1 sous forme de tuple
        if com.count(i)==0:
            i=(i,1)
        else:
            i=(i,pois.count(i)/(pois.count(i)+com.count(i)))
        dangerFeat.append(i)
        list(filter(lambda x: x != i, pois)) 
    for i in com: #attribue un taux 0 aux features restantes de la liste com, ces dernières n'apparaissant pas dans la liste pois
        i=(i,0)
        dangerFeat.append(i)
        list(filter(lambda x: x != i, com))
    
    
    return dangerFeat



def predict(df, L): #prédit la commestibilité des champignons du dataset à partir de ses caractéristiques et de leur taux de dangerosité, sous forme 
    predic=[]
    s=0
    
    for i in range(len(df)): #balayage du dataset
        for j in range(len(df.columns)):
            if (df.iloc[i,j],_)[1]==0:
                predic.append('e') #détermine que le champignon est comestible si la feature est 100% sûre
                break
            elif (df.iloc[i,j],_)[1]==1:
                predic.append('p') #détermine que le champignon est empoisonné si la feature est 100% dangereuse
                break
            else:
                s+=(df.iloc[i,j],_)[1] #crée le taux de dangerosité d'un champignon à partir du taux de dangerosité de ses features
                if j==len(df.columns)+1:
                    if s/(len(df.columns)+1) < 0.5:
                        predic.append('e')
                    else:
                        predic.append('p')
            s=0
   
    return pd.Series(predic)



"""
if __name__ == "__main__":
    df = pd.read_csv('evaluation.csv')
    y = predict(df)
    evaluate(y, true_y) 
"""