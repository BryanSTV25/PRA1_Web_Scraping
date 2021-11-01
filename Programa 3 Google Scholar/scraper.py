# -*- coding: utf-8 -*-
"""
Universidad Oberta de Catalunya

Práctica de Web Scraping - PRA1

Integrantes del grupo:
    Bryan Steven Cortez Chichande
    César Alexander Guzmán Vásquez
    
"""
import requests
import csv
from bs4 import BeautifulSoup

"""
La clase PageScrapper contiene todas las funciones para realizar el web 
scrapping a la página Google Scholar, estando diseñada para la estructura
de esta.
Todos los métodos han sido pensados de forma atómica en lo posible, para 
facilitar los cambios que se requieran, por lo que cada método realiza tareas
muy pequeñas que se unen en otros métodos.
"""
class PageScrapper():
    
    """
    Función: Obtiene la pagina del link insertado.
    
    Parámetros de entrada:
        String      link: Link de la página ingresada
    
    Parámetros de salida:
        Object      page: Objeto page de la librería requests
    """
    def getPage(self, link):
        page = requests.get(link)
        return page;
    
    """
    Función: Imprime los headers de la página insertada.
    
    Parámetros de entrada:
        Object      page: Objeto page de la librería requests
    """
    def printMainPageHeaders(self, page):
        print(page)
        print(page.headers)
        
    
    """
    Función: Devuelve un soup de la página insertada transformado por
    la librería BeautifulSoup
    
    Parámetros de entrada:
        Object      page: Objeto page de la librería requests
    """
    def beautifyPageContent(self, page):
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup;
    
    
    """
    Función: Imprime el objeto soup en formato html
    
    Parámetros de entrada:
        Object      soup: Objeto soup de la librería BeautifulSoup
    """
    def printBeautifyPageContent(self, soup):
        print(soup.prettify())
    
    """
    Función: Obtiene la lista de los links de toda la página de resultados 
    que coincidan con las citaciones
    
    Parámetros de entrada:
        Object      soup: Objeto soup de la librería BeautifulSoup
    
    Parámetros de salida:
        String[]        list_all_links: Arreglo con los links de todas las 
                        citaciones 
    """
    def getAllListLinks(self, soup):
        list_all_links = [];
        for link in soup.find_all('a'):
            inicial_link = "/citations?hl=es&user="
            complete_link = link.get('href')
            if inicial_link == complete_link[0:22]:
                list_all_links.append(complete_link)
        return list_all_links;
        

    """
    Función: Obtiene la lista de links de citaciones sin elementos repetidos
    
    Parámetros de entrada:
        String[]        list_all_links: Arreglo con los links de todas las 
                        citaciones 
    
    Parámetros de salida:
        String[]        list_unique_links: Arreglo con los links de todas las 
                        citaciones sin elementos repetidos
    """
    def getUniqueListLinks(self, list_all_links):
        list_unique_links = [];
        for item in list_all_links:
            if item not in list_unique_links:
                list_unique_links.append(item)
        return list_unique_links;
    

    """
    Función: Obtiene una lista de links usables de cada resultado
    
    Parámetros de entrada:
        String        linkBase: Link base de la página con la que se va a 
                        crear los links completos
        String[]      list_unique_links: Arreglo con los links de todas las 
                        citaciones sin elementos repetidos
    
    Parámetros de salida:
        String[]        list_complete_links: Arreglo con los links completos
    """
    def joinLinks(self, linkBase, list_unique_links):
        list_complete_links = [];
        for item in list_unique_links:
            individual_link = linkBase + item
            list_complete_links.append(individual_link)
        return list_complete_links;   


    """
    Función: Obtiene la lista con objetos pages de todos los links insertados
    
    Parámetros de entrada:
         String[]        list_complete_links: Arreglo con los links completos
    
    Parámetros de salida:
        page[]        pages_array: Arreglo con los objetos pages de los links
                        insertados
    """
    def getIndividualPages(self, list_complete_links):
        pages_array = [];
        for complete_link in list_complete_links:
            pages_array.append(self.getPage(complete_link))
        return pages_array;
    
    
    """
    Función: Obtiene una lista de soups de todas las paginas insertadas
    
    Parámetros de entrada:
         page[]        pages_array: Arreglo con los objetos pages de los links
                        insertados
    
    Parámetros de salida:
        soup[]        soups_array: Arreglo con los objetos soups de los links
                        insertados
    """
    def getBeautifyPagesContent(self, pages_array):
        soups_array = [];
        for page in pages_array:
            soups_array.append(self.beautifyPageContent(page))
        return soups_array;

    
    """
    Función: Obtiene la parte clave del link de la siguiente página de 
    resultados
    
    Parámetros de entrada:
         Object      soup: Objeto soup de la librería BeautifulSoup
    
    Parámetros de salida:
        String        linkNextButton: String con la parte clave del link de la
                        siguiente página de resultados
    """
    def getNextButtonLink(self, soup):
        for button in soup.find_all('button'):
            if button['aria-label'] == "Siguiente":
                linkNextButton = button['onclick'][128:(len(button['onclick'])-17)]
        return linkNextButton;

    
    """
    Función: Crea un link válido de la siguiente página de resultados
    
    Parámetros de entrada:
         String      linkB2: String con la parte clave del link de la
                        siguiente página de resultados
        int          maxRegisterPage: Máximo número de registros que se desea
                        obtener
    
    Parámetros de salida:
        String        String completo y válido de la siguiente página de
                        resultados
    """
    def getNextPageLink(self, linkB2, maxRegisterPage):
        linkB1 = 'https://scholar.google.es/citations?view_op=search_authors&hl=es&mauthors=data+science&after_author='
        linkB3 = '&astart='
        linkB4 = str(maxRegisterPage)
        return linkB1 + linkB2 + linkB3 + linkB4;
        
    
    """
    Función: Obtiene una lista de todos con links válidos de las siguientes 
    páginas de resultados
    
    Parámetros de entrada:
         Object      soup: Objeto soup de la librería BeautifulSoup
         int         maxRegisterPage: Máximo número de registros que se desea
                        obtener
        String[]     list_first_links: Lista de los primeros links de la página
                     de resultados
    
    Parámetros de salida:
        String[]     result_pages_array: Arreglo con los links de las siguientes
                     páginas de resultados
    """
    def getAllResultPagesLinks(self, soup, maxRegisterPage, list_first_links):
        result_pages_array = [];
        for link in list_first_links:
            result_pages_array.append(link)
        countResult = 0;
        page_temp = requests.get(self.getNextPageLink(self.getNextButtonLink(soup), countResult))
        soup_temp = BeautifulSoup(page_temp.content, 'html.parser')
        while countResult <= maxRegisterPage:
            result_pages_array.append(self.getNextPageLink(self.getNextButtonLink(soup_temp), countResult))
            countResult += 10
            page_temp = requests.get(self.getNextPageLink(self.getNextButtonLink(soup_temp), countResult))
            soup_temp = BeautifulSoup(page_temp.content, 'html.parser')
        return result_pages_array;
            
    
    """
    Función: Obtiene una lista de todos los links de las paginas de resultados
    
    Parámetros de entrada:
        String[]     list_first_links: Arreglo de los links de todas las 
                        páginas de resultados
        String       linkBase: Link base para crear los links
    
    Parámetros de salida:
        String[]     list_individual_result_links_array: Arreglo con todos los
                        links de todas las páginas de resultados
    """
    def getAllIndividualLinkPages(self, result_pages_array, linkBase):
        list_individual_links_array = [];
        list_individual_result_links_array = [];
        soups_array = self.getBeautifyPagesContent(self.getIndividualPages(result_pages_array))
        for soupResultPage in soups_array:
            list_individual_links_array = self.joinLinks(linkBase, self.getUniqueListLinks(self.getAllListLinks(soupResultPage)))
            for item in list_individual_links_array:
                list_individual_result_links_array.append(item)
        return list_individual_result_links_array;
        
    
    """
    Función: Obtiene el nombre del autor de la página
    
    Parámetros de entrada:
        Object      soup: Objeto soup de la librería BeautifulSoup
    
    Parámetros de salida:
        String     link.text: String con el nombre del autor
    """
    def getAuthorName(self, soup):
        for link in soup.find_all('div'):
            idDiv = link.get('id')
            if idDiv == 'gsc_prf_in':
                return link.text;
    
    
    """
    Función: Obtiene la especializacion o área de estudio del autor
    
    Parámetros de entrada:
        Object      soup: Objeto soup de la librería BeautifulSoup
    
    Parámetros de salida:
        String     link.text: String con el área de estudio del autor
    """
    def getAuthorSpecialization(self, soup):
        for link in soup.find_all('a', attrs={'class':'gsc_prf_inta gs_ibl'}):
            return link.text;
    
    
    """
    Función: Obtiene los datos de las citaciones del autor
    
    Parámetros de entrada:
        Object      soup: Objeto soup de la librería BeautifulSoup
    
    Parámetros de salida:
        String[]    list_citations: Arreglo con la información de las citaciones
    """
    def getCitations(self, soup):
        list_citations = [];
        for link in soup.find_all('td', attrs={'class':'gsc_rsb_std'}):
            list_citations.append(link.text)
        return list_citations;
    
    
    """
    Función: Obtiene los datos de la pagina
    
    Parámetros de entrada:
        Object      soup: Objeto soup de la librería BeautifulSoup
    
    Parámetros de salida:
        String[]    page_data: Arreglo con la información de toda la página
    """
    def getPageData(self, soup):
        page_data = []; 
        page_data.append(self.getAuthorName(soup));
        page_data.append(self.getAuthorSpecialization(soup));
        for citation in self.getCitations(soup):
             page_data.append(citation);        
        return page_data;
        
    
    """
    Función: Obtiene la data de todas las paginas de resultados
    
    Parámetros de entrada:
        String[]    list_individual_result_links_array: Arreglo con los links 
                    de todas las páginas que contienen la información
        Object      soup: Objeto soup de la librería BeautifulSoup
    
    Parámetros de salida:
        String[]    all_data: Arreglo con la información individual de todas
                    las páginas
        
    """
    def getAllDataPages(self, list_individual_result_links_array):
        all_data = [];
        for individual_page in list_individual_result_links_array:
            page = self.getPage(individual_page);
            soup = self.beautifyPageContent(page);
            page_data = self.getPageData(soup);
            all_data.append(page_data);
        return all_data;
    
    
    """
    Función: Genera el archivo csv con los resultados 
    
    Parámetros de entrada:
        String[]    all_data: Arreglo con la información individual de todas
                    las páginas
        
    """
    def saveCSVFile(self, all_data):
        datahead = ['Autor', 'Especializacion', 'Total de citas', 'Citas Ultimos 5 años', 'Total Indice H', 'Indice H Ultimos 5 años', 'Indice i10', 'Indice i10 Ultimos 5 años']
        csv_file =  open("google_scholar_dataset.csv", 'w', newline='', encoding="utf-8")  
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(datahead)
        for data in all_data:
            csv_writer.writerow(data)
        csv_file.close()
        
        
        
        
        
        
        
        
        
        
        
        