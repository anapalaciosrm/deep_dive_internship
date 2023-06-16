import pandas as pd
import csv 
import requests
from bs4 import BeautifulSoup

information = pd.read_csv(r'titulados.csv') #aquire information from csv file

for i in range(len(information['Nombre'].values)): #comparar la lista de estuduantes en CSV con la informacion en la pagina official
    yearCSV = information['Carrera'].values[i]
    yearWeb = findStudentWeb(i)
    if yearWeb == 0: deep_dive_response('deep_dive_response', i, "Información Válida") 
    elif yearCSV == yearWeb: deep_dive_response("No titulado", i)
    else: deep_dive_response("Titulado; año incorrecto", i)
print(information)

def findStudentWeb(index):

#identificar la informacion proveniente del website usando beautiful soup 
    information = pd.read_csv(r'titulados.csv') #aquire information from csv file
    if information['Carrera'].values[index] == "Economia": url = xxx
    if information['Carrera'].values[index] == "Economia": url = xxx
    if information['Carrera'].values[index] == "Economia": url = xxx
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table') #encontrar la tabla

    row_name = information['Nombre'].values[index]
    studentInQuestion = None

    for row in table.find_all('tr'): #encontrar la fila del alumno 
        if row_name in row.text:
            studentInQuestion = row
            break
    
    if target_row: #Año de titulación
        columns = target_row.find_all('td')
        year = columns[1].text
    else: year = 0
    return year 
        
def edit(column, row, text):
    information = pd.read_csv(r'titulados.csv') #aquire information from csv file

    information.at[row, column] = text #editar la respuesta de deep_dive

    information.to_csv(r'titulados.csv', index=False) #guardar los cambios


