%% Pto 5 de trabajo practico 1
%% Gráficos de w en funcion de la cantidad k de iteraciones para cada n distinto

clear all, close all;

%graphics_toolkit gnuplot % Descomentar si se usa Octave

% Importo resultados de orbita de corrida de tp2.py 
% Debo tener en cuenta que cada archivo generado por tp2.py presenta una
% linea de encabezado y utiliza , para separar los datos .

orbita = dlmread('posiciones_euler.txt', ',',1,0);

%Obtengo las posiciones de la orbita a partir de los datos de orbita

x_orbita = orbita(:,1);
y_orbita = orbita(:,2);

%Defino variables para graficar la tierra y la luna como circunferencias

%Radio terrestre y lunar
r_tierra=6.731e6;

%Posicion terrestre
posicion_tierra=-4.670e6;

%Definiciones para graficar circunferencias
t=0:pi/30:2*pi;

x_tierra=posicion_tierra+r_tierra*cos(t);
y_tierra=r_tierra*sin(t);

% Primero, para identificar a los objetos, guardamos los "Handlers"
% Genero la figura
Hf1 = figure(1);
% Modifico las opciones de la figura. En este caso sólamente definimos el tamaño de la figura
% (a la hora de imprimirse).
set(Hf1,'PaperUnits','inches','PaperPosition',[0 0 5 5]);

%Genero ejes
Ha2 = axes;
% Cambio sus atributos.
set(Ha2,'Box','on','FontName','Arial','FontSize',12,'GridLineStyle','--','LineWidth',1,'TickDir','in');
grid on;
hold on;

%Grafico Tierra y Luna
plot(x_tierra,y_tierra,'k-','LineWidth',4); 

%Grafico orbita
plot(x_orbita,y_orbita,'-b','linewidth',3);

%Limites de los ejes para que las circunferencias no se deformen y se vea completa
%la orbita

xlim([-3E7 3E7]);
ylim([-7E7 7E7]);
 

% No necesitan etiquetas los ejes.

%xlabel('Largo de la viga');
%ylabel('Desviacion de la viga');

%Imprimo en un archivo el grafico
print('Orbita_tierra.pdf','-dpdf','-r300');
