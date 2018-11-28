%% Gráfico de la energia cinetica en funcion del paso

clear all, close all;

%graphics_toolkit gnuplot % Descomentar si se usa Octave

%eje y con numeros de final de tabla nombre ejey: Ec 
%eje x con numeros i/n (con n=5, es 0/5,1/5,2/5,etc) nombre ejex: h(t(s))

% Importo resultados de cada corrida de numerico.py 
% Debo tener en cuenta que cada archivo generado por numerico.py presenta una
% linea de encabezado y utiliza | para separar los datos .

energia = dlmread('emecanica_rk.txt', ',',0,0);

%Obtengo las energias a partir de los datos del programa

energia_c = energia(:,1);
energia_p = energia(:,2);
energia_m = energia(:,3);
tiempo_h = energia(:,4);


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
grid minor;
hold on;

%Grafico curvas de energias

h1 = plot(tiempo_h,energia_c,'r-','LineWidth',3);											% Energia Cinetica
h2 = plot(tiempo_h,energia_p,'b-','LineWidth',3);											% Energia Potencial
h3 = plot(tiempo_h,energia_m,'c-','LineWidth',3);					            % Energia Mecanica

% Ponemos etiquetas a los ejes.

ylabel('E(J)');
xlabel('t(s)');


%Preparo la leyenda

LEYENDA1 = sprintf('Energia Cinetica');
LEYENDA2 = sprintf('Energia Potencial');
LEYENDA3 = sprintf('Energia Mecanica');

Hleg = legend(Ha,[h1 h2 h3],{LEYENDA1, LEYENDA2, LEYENDA3}, 'Position', NorthWest);
legend('boxon');
set(Hleg,'FontName','Arial','FontSize',7);

%Imprimo en un archivo el grafico
print('Grafico_energias_rk.pdf','-dpdf','-r300');