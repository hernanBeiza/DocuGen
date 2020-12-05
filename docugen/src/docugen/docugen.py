import os
from sys import argv
from colorama import Fore, Back, Style, init
init(autoreset=True)

def main(args=None):
	#print("main: tarea");
	print(Fore.YELLOW + "docugen");
	titulo = input("Ingresa el título del archivo: ");
	carpetaFotos = input("Ingresa la ruta de la carpeta de fotos: ");
	archivoMarkdown = input("Ingresa el nombre del archivo markdown: ");
	leerCarpeta(titulo, carpetaFotos, archivoMarkdown);
	#main,titulo,carpetaFotos,archivoMarkdown = argv;

def leerCarpeta(titulo, carpetaFotos, archivoMarkdown):
	#print("leerCarpeta");
	if(carpetaFotos.endswith("/")==False):
		carpetaFotos+="/"
	carpetas = os.listdir(carpetaFotos);

	imagenes = []
	for archivo in sorted(carpetas):
		ruta = carpetaFotos+archivo;
		#print(item);
		#partes = item.split(".");
		#print(partes[len(partes)-1]);
		if(archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
			#print(archivo + " es imagen");
			imagenes.append(archivo);
	print(Fore.YELLOW + "Fotos encontradas: " + str(len(imagenes)));
	crearArchivo(titulo, imagenes, carpetaFotos+archivoMarkdown);

def crearArchivo(titulo, imagenes, rutaArchivoMarkdown):
	#print("crearArchivo: " + archivoSalida);
	archivoSalida = open(rutaArchivoMarkdown, "w+");
	tituloString = "# "+ titulo;
	archivoSalida.write(tituloString);
	archivoSalida.write("\n");

	indice = 1;
	for imagen in imagenes:
		#print(imagen);
		tituloFoto = "## "+ imagen;
		archivoSalida.write(tituloFoto);
		archivoSalida.write("\n");
		lineaFoto = "!["+imagen+"]("+imagen+")";
		archivoSalida.write(lineaFoto);
		archivoSalida.write("\n");
		archivoSalida.write("\n");
		respuesta = True;
		while respuesta == True:
			descripcionFoto = input("Foto N: "+str(indice)+" Ingresa una descripción para la foto "+imagen+": ");
			archivoSalida.write(" - " + descripcionFoto);
			archivoSalida.write("\n");
			respuesta = preguntar(indice);
		indice+=1;
	print(Fore.YELLOW + "Archivo markdown guardado en: " + rutaArchivoMarkdown)
	archivoSalida.close();

def preguntar(indice):
	opcion = input("¿Ingresar otra descripción a la foto N "+str(indice)+": (S/N)").lower();
	yes = {'yes','y', 'ye', 'S','s'}
	no = {'no','n'}	
	if opcion in yes:
		return True;
	elif opcion in no:
		return False;
	else:
		print(Fore.YELLOW + "Ingresa S ó N");
		return preguntar(indice);

if __name__ == '__main__':
	if len(argv) < 2:
		#argv por defecto
		#argv = ['script', '1', '2', '3']
		#print("Falta especificar carpeta con fotos y archivo de salida");
		main(argv)
	else:
		titulo = argv[1];
		carpetaFotos = argv[2];
		archivoMarkdown = argv[3];
		main(argv)