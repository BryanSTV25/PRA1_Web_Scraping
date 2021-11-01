# PRA1_Publicaciones_Cientf

**Descripción**

Este proyecto extrae los datos bibliográficos de publicaciones científicas de las áreas anexas a la ciencia de datos. Para ello hace uso de la páginas <a href="semanticscholar.org">Semantic Schocal</a>, <a href="dialnet.unirioja.es">Dialnet</a> y <a href="scholar.google.com">Google Scholar</a>.


**Instrucciones**

**- Programa 1**

Para el programa 1 se hace uso del lenguaje Pyhton, por medio de Jupiter Notebooks, por lo que será necesario tener Jupiter Notebooks para probarlo.

Para ejecutarlo, seguir los siguientes pasos:
  
  1. Entrar a Jupiter Notebooks y navegar hasta la localización de los archivos.

  ![image](https://user-images.githubusercontent.com/27928138/138793298-7c627598-321b-4e59-a4ed-fb0f3e324a92.png)

  2. Abrir el archivo pra1_Semantic_Scholar.ipynb
  
  ![image](https://user-images.githubusercontent.com/27928138/139693827-90e78c3f-4d46-440b-a19a-4a6a88f57104.png)

  3. Presionar el botón Run.
  
  ![image](https://user-images.githubusercontent.com/27928138/138793570-5a779cdb-6906-4d65-b53a-123792ec878d.png)
 
  4. Ejecutar todas las funcionas hasta el final del programa.
  
  ![image](https://user-images.githubusercontent.com/27928138/138793744-c2639481-72e4-4e8f-a855-5bac33b652e7.png)

  5. Al finalizar el programa obtendrá un archivo con el nombre "_dtpapers.csv" en el directorio de ejecución del programa. También lo puede visualizar en el directorio Datasets CSV.
  
 ![image](https://user-images.githubusercontent.com/27928138/139693985-3910abf3-ac95-4654-a4b7-762dc48dbe91.png)

  6. Al abrirlo se encontrará con un archivo como este.

  ![image](https://user-images.githubusercontent.com/27928138/138794342-aa26dd63-559f-47d5-a73a-1c98cf1c99ee.png)

  7. Para facilitar su visualización, puede convertirlo a un formato excel, lo cual se verá así:
  
  ![image](https://user-images.githubusercontent.com/27928138/138794512-1fe8ad82-9aaf-4a7e-b2dd-ec70c38d0c00.png)

  Para efectos prácticos, en este caso, el archivo resultante en formato excel se puede visualizar en el archivo llamado Semantic Scholar Dataset.xlsx, que se encuentra en el directorio Datasets Excel.
  
  ![image](https://user-images.githubusercontent.com/27928138/138794642-781d5462-2d62-4b44-b950-be966b2bf321.png)

  En la hoja _dtpapers se encuentran los datos en un formato de tabla. Mientras que en la hoja Resumen Datos, se encuentra un breve resumen visual con gráfico y con tabla de los datos según su año, su acceso y su categoría.
  
  ![image](https://user-images.githubusercontent.com/27928138/138794868-9fb2ac8b-1426-4a7a-8c48-fcf8717eb752.png)


**- Programa 2**

Para el programa 2 se hace uso del lenguaje Pyhton, por medio de Jupiter Notebooks, por lo que será necesario tener Jupiter Notebooks para probarlo.

Para ejecutarlo, seguir los mismos pasos que el Programa 1.

Al finalizar el programa obtendrá un archivo con el nombre "_dtpapersdnt.csv" en el directorio de ejecución del programa. También lo puede visualizar en el directorio Datasets CSV. 

![image](https://user-images.githubusercontent.com/27928138/139694773-b2ebcd2e-0e1f-44de-a356-dc5f199e8dda.png)

Para efectos prácticos, en este caso, el archivo resultante en formato excel se puede visualizar en el archivo llamado Dialnet Dataset.xlsx, que se encuentra en el directorio Datasets Excel.

![image](https://user-images.githubusercontent.com/27928138/139695962-08c10f14-726a-40e4-b18b-35138d239aa2.png)


**- Programa 3**

Para el programa 3 se hace uso del lenguaje Pyhton, usando Spyder como IDE, por lo que se recomienda tener Spyder para probarlo.

Para ejecutarlo, seguir los siguientes pasos:

1. Entrar a Spyder y abrir los archivos scraper.py y pra1_Google_Scholar.py

![image](https://user-images.githubusercontent.com/27928138/139701368-ee2922f5-eeaa-445d-a913-4ff044d30c31.png)

2. Ejecutar el script pra1_Google_Scholar.py presionando el botón de play en Spyder.

![image](https://user-images.githubusercontent.com/27928138/139702307-d024701f-61f0-4c9c-86e2-86bf248b5ee9.png)

3. Al terminar la ejecución después de unos minutos, en el mismo directorio de encontrará con el archivo google_scholar_dataset.csv

![image](https://user-images.githubusercontent.com/27928138/139703023-0d046c91-f24c-4ba8-9208-9080aea411b3.png)

4. Al abrirlo se encontrará con un archivo como este.

![image](https://user-images.githubusercontent.com/27928138/139703135-c4c2913d-38c7-4ba9-a914-21c50ce66330.png)

5. Para facilitar la visualización puede convertirlo en un archivo excel, en este caso, el archivo resultante en formato excel se puede visualizar en el archivo llamado Google Scholar Dataset.xlsx, que se encuentra en el directorio Datasets Excel.

![image](https://user-images.githubusercontent.com/27928138/139705123-c86a3ff3-32a0-4d27-8da6-5630e3275e4f.png)

En la hoja google_scholar_dataset se encuentran los datos en un formato de tabla. Mientras que en la hoja Resumen Datos, se encuentra un breve resumen visual con gráfico y con tabla de los datos según categoría individual y agrupada.

**Miembros del equipo**

  - Bryan Steven Cortez Chichande
  - César Alexander Guzmán Vásquez
  
**Ficheros del código fuente**

**Programa 1**
  - pra1_Semantic_Scholar.ipynb: Jupiter Notebook con las instrucciones del programa
  - robot.txt: Archivo robot de la página Semantic Scholar
  - _dtpapers.csv: Archivo resultante con el dataset del programa

**Programa 2**
  - pra1_Dialnet.ipynb: Jupiter Notebook con las instrucciones del programa
  - _dtpapers.csv: Archivo resultante con el dataset del programa

**Programa 3**
  - pra1_Google_Scholar.py: Programa principal de ejecución 
  - scraper.py: Archivo con la clase y funciones necesarias para hacer el web scraping
  - google_scholar_dataset.csv: Archivo resultante con el dataset del programa

**Recursos**
Rodó, D. M. (2020). El lenguaje Pyhton. Barcelona.
Subirats, L. M., & Calvo, M. G. (2019). Web scraping. In L. M. Subirats, & M. G. Calvo. Barcelona: 2019.
