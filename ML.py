import mysql.connector
from sklearn import tree

cnx = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'car')
cursor = cnx.cursor()

query = 'SELECT * FROM moshakhasat'
cursor.execute(query)

x = []
y = []
for (name, price, mile) in cursor:
    x.append([price, mile])
    y.append(name)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)


new_data = [[82615, 18882]]
answer = clf.predict(new_data)

print(answer)   

cnx.commit()
cnx.close() 