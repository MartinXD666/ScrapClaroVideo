#---------------BOOKSTORES----------------------
import json
import random
from time import sleep
from selenium import webdriver

#---------------------FUNCTIONS------------------------
def cargarJson():

    with open('dataPeliculas.json', 'a') as file:
        json.dump(data, file, indent=4)

def cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas, 
                        temporada, episodio):

    data['Series'].append( {
        'Titulo' : titulo,
        'Subtitulo - Año' : subtitulo_anio,
        'Sinopsis' : sinopsis,
        'Genero' : genero,
        'Protagonistas' : listaDeProtagonistas,
        'Temporada' : temporada,
        'Episodio' : episodio
    })
    print(data)

def actualizarPrincipal():
    print("ACTUALIZANDO PAGINA PRINCIPAL...\n")
    driver.get('https://www.clarovideo.com/argentina/nv_se_catalogo')
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


def scrapLaSeccion(numeroSeccion):

        cantSeries = 0
        sections = driver.find_elements_by_xpath('//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
        print("--------------------------SECTION {}--------------------------".format(numeroSeccion))
        series = sections[numeroSeccion].find_elements_by_xpath('.//li')
        lengthSeries = len(series)
        print(lengthSeries)
        for p in range(lengthSeries):
            cantSeries+=1
            sections = driver.find_elements_by_xpath(
                    '//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
            series = sections[numeroSeccion].find_elements_by_xpath('.//li')

            elem = series[p].find_element_by_xpath('.//span[@class="play"]')
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

            temporada = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/div/span[1]').text

            episodio = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/div/span[3]').text

            listaDeProtagonistas = cargarProtagonistas(protagonistas)

            cargarData(titulo, sinopsis, genero, subtitulo_anio, listaDeProtagonistas,
                                temporada, episodio)

            print("---------------PELICULA NUMERO: ", cantSeries, " --------------- \n")

            print(titulo)
            print(sinopsis)
            print(genero)
            print(subtitulo_anio)
            print(listaDeProtagonistas)
            print(temporada)
            print(episodio)

            print("\n")

            actualizarPrincipal()

            numeroSeccion+=2

            for j in range(p + 1):
                deslizar = driver.find_element_by_xpath(
                        './/*[@id="app"]/div/div[1]/div/div/div/section[{}]/div[2]/div/div/div[3]/div'.format(numeroSeccion))
                print(deslizar.get_attribute('outerHTML'))
                deslizar.click()
                sleep(random.uniform(2.0, 3.0))
            sleep(random.uniform(3.0, 6.0))


#------------------------------MAIN-----------------------------------------

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.clarovideo.com/argentina/nv_se_catalogo')
data = {}
data['Series'] = []
sleep(3)
scrollFinal()
url=driver.current_url
print("COMENZANDO DESDE: ", url, "\n")
sections = driver.find_elements_by_xpath('//section//div[@class="jcarousel jcarousel-1 horizontal carrousel-row"]')
lengthSections = len(sections)
print(lengthSections)

scrapLaSeccion(3)

cargarJson()
driver.quit()
exit()