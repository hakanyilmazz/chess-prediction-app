# veri okumak için import edildi.
import joblib
from sklearn.linear_model import LogisticRegression
import pandas as pd

# veriler csv'den okunur.
chessData = pd.read_csv('chess.csv')
print(chessData, end="\n\n")

categoricals = []
for col, col_type in chessData.dtypes.iteritems():
    if col_type == 'O':
        categoricals.append(col)
    else:
        chessData[col].fillna(0, inplace=True)

# kategorik veriler nümerik veriye çevrildi.
df_ohe = pd.get_dummies(chessData, columns=categoricals, dummy_na=True)

dependentVariable = 'sonuc'

# bağımsız değişkenler
X = df_ohe[df_ohe.columns.difference([dependentVariable])]

# tahmin edilecek değişken
y = df_ohe[dependentVariable]

print(X, end="\n\n")
print(y, end="\n\n")

# veriyi eğittik.
logisticRegression = LogisticRegression()
logisticRegression.fit(X, y)

joblib.dump(logisticRegression, 'chess-model.pkl')
print("Model oluşturuldu.")

# veri kolonlarını eğitimden kaydetme
logisticRegression = joblib.load("chess-model.pkl")
modelKolonlari = list(X.columns)
joblib.dump(modelKolonlari, 'chess-model-columns.pkl')
print("Model kolonları oluşturuldu.")
