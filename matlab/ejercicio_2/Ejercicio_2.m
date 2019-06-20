% Hola, Javier.
% He creado un archivo para que veas que el programa funciona
% Introduce un directorio donde tengas fotos buenas en
% "prueba_fotos_enfocadas"
% Y el directorio donde vas a hacer la prueba en "carpeta de Ana"
% Ten cuidado de no poner barra al final de las rutas.

prueba_fotos_enfocadas = 'C:\Users\Gabriel\Desktop\input';
carpeta_de_Ana = 'C:\Users\Gabriel\Desktop\output';

blurred(prueba_fotos_enfocadas, carpeta_de_Ana)
blurdetection(carpeta_de_Ana)