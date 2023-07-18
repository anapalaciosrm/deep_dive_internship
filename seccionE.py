import requests 
from bs4 import BeautifulSoup
import pandas as pd

from utils import get_url, main_page


class WebScrapper:
    """Class that facilitates the scrapping of the ITAM's graduation page.
    """
    def __init__(self, url:str=f"{main_page}"):
        self.url = url
        self.page = self.retreive_page(self.url)
        self.fetch_programs()


    def retreive_page(self, url):
        """Tries to retrieve the page and returns an error if it fails."""
        page = requests.get(url)
        if page.status_code != 200:
            raise Exception(f"Error: could not load the page from {url}.")
        
        return page
        

    def fetch_programs(self):
        """Fetches the programs
        """
        bs = BeautifulSoup(self.page.content, 'lxml')
        raw_array = bs.find_all('a')
        self.programs = {}
        for value in raw_array:
            self.programs[value.text] = value.attrs['href']
        
    def get_program_df(self, degree: str=None, prog: int=None, columns_from:int=1):
        """Turns the scraped information in a data frame, the name of the students as the index
        """
        prog_url = get_url(degree=degree, prog=prog)
        prog_page = self.retreive_page(prog_url)
        bs = BeautifulSoup(prog_page.content, 'lxml')
        df_list = []
        for value in  bs.find_all('tr'):
            row = [tr.text for tr in value]
            df_list.append(row)

        column_names= df_list[columns_from]
        df_list= df_list[columns_from+1:]
        df = pd.DataFrame(df_list, columns=column_names)
        df_ind = df.set_index('Nombre del alumno')

        return df_ind
    
    def find_gradYear(self, name: str=None, degree2: str=None):
        """Returns the graduation year of a student as established by the official ITAM website, finds information using degree and name
        """
     
        df = self.get_program_df(degree=degree2)
        new_df = df[df.index == name]["Año de titulación"]
        return new_df.values.item(0)

class ClassifyStudents:
    """Class that facilitates that extracts information from CSV file by transforming it into a data base 
    """

    def __init__(self, filename: str='titulados.csv'):
        self.filename = filename
        self.data = self.read_filename()

    def read_filename(self):
        """Converts the CSV file into a data frame, returns data frame with student names as index
        """
        df = pd.read_csv(self.filename)
        df_ind = df.set_index('Nombre')
        return df_ind

    def find_degree(self, name: str=None):
        """Finds the degree of student using index of name 
        """
        df = self.data
        new_df = df[df.index == name]["Carrera"]
        return new_df.values.item(0)
    
    def find_gradYear(self, name: str=None):
        """Finds the graduation year of student using index of name 
        """
        df = self.data
        new_df = df[df.index == name]["Año"]
        return new_df.values.item(0)


def compare(student): 
    """Function that compares graduation years of student in CSV file and official ITAM webpage, returns 0 if information is correct, 1 if year is incorrect, and 2 if student does not exist
    """
    scraper1 = ClassifyStudents()
    scraper2 = WebScrapper()
    try: 

        gradYearCSV = scraper1.find_gradYear(name=student)
        career = str(scraper1.find_degree(name=student))
        gradYearITAM = int(scraper2.find_gradYear(name = student.upper(), degree2 = career.upper()))
        if (gradYearITAM == gradYearCSV): return 0
        else: return 1

    except IndexError: 
        return 2

def deep_response():
    """Creates a new CSV file with deep_dive_response
    """
    scraper1 = ClassifyStudents()
    final_df = scraper1.read_filename()
    final_df['deep_dive_response'] = ""
    indexes_list = final_df.index.tolist()
        
    for index in indexes_list:
        response = compare(index)
        if response == 0: final_df.loc[index, 'deep_dive_response'] = 'Información Válida'
        elif response == 1: final_df.loc[index, 'deep_dive_response'] = 'Titulado; año incorrecto'
        else: final_df.loc[index, 'deep_dive_response'] = 'No titulado'
    csv_df = final_df.reset_index()     
    return csv_df


response_df = deep_response() #deep_dive response as a data frame
response_df.to_csv("tituladosResponse.csv", index=False) #deep_dive response as CSV file

print(response_df) #printing deep_dive response as a data frame
