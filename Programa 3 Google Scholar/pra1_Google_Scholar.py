# -*- coding: utf-8 -*-
"""
Universidad Oberta de Catalunya

Práctica de Web Scraping - PRA1

Integrantes del grupo:
    Bryan Steven Cortez Chichande
    César Alexander Guzmán Vásquez
    
"""


"""
Archivo principal donde se hace el llamado a las funciones de la clase Scraper.

El programa básicamente realiza un web scraping de 2 niveles, el primer nivel
lo hace de la primera página de resultados, obteniendo el link de la siguiente
página de resultados, a la vez que obtiene los páginas individuales que 
contienen las páginas de resultados. Finalmente de la página individual extrae
los datos que resultaban útiles para este análisis.  
"""

from scraper import PageScrapper

"""
Llamado a la clase Scraper  
"""
scraper = PageScrapper();

"""
Definición de los links base, uno con la página principal y otro con la primera
página de resultados de la busqueda de data science en Google Scholar
"""
linkBase = 'https://scholar.google.es'
linkMainPage = 'https://scholar.google.es/citations?view_op=search_authors&mauthors=data+science&hl=es&oi=ao'


"""
Obtención de la página para poder usarla como objeto soup
"""
mainPage = scraper.getPage(linkMainPage)
soup =  scraper.beautifyPageContent(mainPage)

print("\n************* Iniciando programa *************\n")

print("\n************* Page Headers *************\n")
scraper.printMainPageHeaders(mainPage)

"""
Iniciación del proceso de scraping de la primera página de resultados
"""
list_all_links = scraper.getAllListLinks(soup)

list_unique_links = scraper.getUniqueListLinks(list_all_links)

list_complete_links = scraper.joinLinks(linkBase, list_unique_links)


"""
Obtención de la lista de todos los links de las páginas de resultados siguientes
"""

print("\n************* Lista Links de Resultados Inidividuales *************\n")

list_result_links = scraper.getAllResultPagesLinks(soup, 500, list_complete_links)

list_results_indiividual_links = scraper.getAllIndividualLinkPages(list_result_links, linkBase)

print(list_results_indiividual_links)

"""
Obtención de la información de todas las páginas de resultados y guardado en 
el archivo csv
"""
data_pages = scraper.getAllDataPages(list_results_indiividual_links)

scraper.saveCSVFile(data_pages)

print("\n************* Programa Finalizado*************\n")

































