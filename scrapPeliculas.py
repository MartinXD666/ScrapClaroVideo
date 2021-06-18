#---------------BOOKSTORES----------------------
import json
import random
from time import sleep
from selenium import webdriver

#---------------------FUNCTIONS------------------------
def cargarJson():

    with open('dataPeliculas.json', 'a') as file:
        json.dump(data, file, indent=4)

def cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas):

    data['Peliculas'].append( {
        'Titulo' : titulo,
        'Subtitulo - Año' : subtitulo_anio,
        'Sinopsis' : sinopsis,
        'Genero' : genero,
        'Protagonistas' : listaDeProtagonistas
    })
    print(data)

def actualizarPrincipal():
    print("ACTUALIZANDO PAGINA PRINCIPAL...\n")
    driver.get('https://www.clarovideo.com/argentina/nv_catalogo')
    sleep(3)
    scrollFinal()
    url = driver.current_url
    print(url)

def scrollFinal():

    for i in range(8):
        driver.execute_script("window.scrollBy (0, 1000)")
        sleep(random.uniform(3.0, 6.0))

def cargarProtagonistas(listaProtagonistas):

    listaProtagonistasRetorno = []
    for p in listaProtagonistas:
        protagonista = p.find_element_by_xpath('.//p[@class="talents-slide_name"]').text
        listaProtagonistasRetorno.append(protagonista)
        deslizar = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[3]/div')
        deslizar.click()
    return listaProtagonistasRetorno

#------------------------------MAIN-----------------------------------------

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.clarovideo.com/argentina/nv_catalogo')
data = {}
data['Peliculas'] = []
sleep(3)
scrollFinal()
url=driver.current_url
print("COMENZANDO DESDE: ", url, "\n")
sections = driver.find_elements_by_xpath('//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
lengthSections = len(sections)
print(lengthSections)

for i in range(lengthSections):
    cantPeliculas = 0
    sections = driver.find_elements_by_xpath('//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
    if i == 0:
        print("--------------------------SECTION1--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[3]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

    if i == 1:
        print("--------------------------SECTION2--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[4]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    if i == 2:
        print("--------------------------SECTION3--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[5]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    if i == 3:
        print("--------------------------SECTION4--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[6]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    if i == 4:
        print("--------------------------SECTION5--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[7]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    if i == 5:
        print("--------------------------SECTION6--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[8]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    if i == 6:
        print("--------------------------SECTION7--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[9]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    if i == 7:
        print("--------------------------SECTION8--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[10]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    
    if i == 8:
        print("--------------------------SECTION9--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[11]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    
    if i == 9:
        print("--------------------------SECTION10--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[12]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    if i == 10:
        print("--------------------------SECTION11--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[13]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    
    if i == 11:
        print("--------------------------SECTION12--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[14]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    
    if i == 12:
        print("--------------------------SECTION13--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[15]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    
    if i == 13:
        print("--------------------------SECTION14--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[16]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    
    if i == 14:
        print("--------------------------SECTION15--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[17]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    
    if i == 15:
        print("--------------------------SECTION16--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[18]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    
    if i == 16:
        print("--------------------------SECTION17--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[19]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    if i == 17:
        print("--------------------------SECTION18--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[20]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


    if i == 18:
        print("--------------------------SECTION19--------------------------")
        peliculas = sections[i].find_elements_by_xpath('.//li')
        lengthPeliculas = len(peliculas)
        print(lengthPeliculas)
        for p in range(lengthPeliculas):
            cantPeliculas+=1
            sections = driver.find_elements_by_xpath(
                '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            peliculas = sections[i].find_elements_by_xpath('.//li')

            elem = peliculas[p].find_element_by_xpath('.//span[@class="play"]')
            print(elem.get_attribute('outerHTML'))
            elem.click()

            sleep(random.uniform(5.0, 10.0))
            print("GUARDO HTML")

            url = driver.current_url

            print("NOS ENCONTRAMOS EN: ", url ,"\n")

            titulo = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1').text

            subtitulo_anio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]').text

            sinopsis = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span').text

            genero = driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span').text

            protagonistas = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/ul/li')

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas)

            print("---------------PELICULA NUMERO: ", cantPeliculas, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)

            print("\n")

            actualizarPrincipal()

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                    './/*[@id="app"]/div/div[1]/div/div/div/section[21]/div[2]/div/div/div[3]/div')
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))

cargarJson()
driver.quit()
exit()