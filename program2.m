%Создание окон
x0=100;
y0=100;
w0=700;
h0=850;
figure('Position',[x0,y0,w0,h0])
x1=30;
dx=50;
dy=50;
y1=30;
w=200;
h=130;
hAxes1=axes('Units','pixels','Position',[x1,y1,w,2*h])
hAxes2=axes('Units','pixels','Position',[x1,y1+dy+2*h,w,h])
hAxes3=axes('Units','pixels','Position',[x1,y1+2*(dy+h)+h,w,h])
hAxes4=axes('Units','pixels','Position',[x1,y1+3*(dy+h)+h,w,h])
Fs=500;
S=load('dataset.txt');
N=length(S)
T=1/Fs;
tmax=N/Fs;
t=0:T:tmax-T;
ECG=S(:,1);
Puls_R=S(:,2);
Puls_IR=S(:,3);
C=500;
axes(hAxes4)% сигнал ЭКГ верхний график
plot(t,ECG)
axes(hAxes1)% пульсоксиметрические сигналы нижний график
plot(t,Puls_R)  %#################
hold on
plot(t,Puls_IR-C)   %################
for n=3:N
Y(n)=ECG(n)-ECG(n-2);
ECG_dif(n)=abs(Y(n));
end
axes(hAxes3)% график с дифференцированием ЭКГ
plot(t,Y)    %##################
axes(hAxes2)% график модуля дифференцированного ЭКГ
plot(t,ECG_dif)
Limit=20;
XLimit(1)=0;
XLimit(2)=tmax-T;
YLimit(1:2)=Limit;
hold on
line(XLimit,YLimit)% горизонтальная линия на уровне порога
Jmax=100;
k=0;
j=Jmax;
for i=1:N % обнаружение QRS-комплексов ЭКГ
j=j+1;
if (ECG_dif(i)>Limit)&&(j>Jmax)
k=k+1;
QRS(k)=i;
j=0;
end
end
axes(hAxes1) % добавляем в график точки обнаружения QRS-комплексов ЭКГ
YLimits=get(hAxes4,'YLim');
for i=1:k
XLimits(1:2)=QRS(i)*T;
HLine=line(XLimits,YLimits);
set(HLine,'LineStyle','--')
end
D1=0;%расчет среднего размаха пульсоксиметрических сигналов
D2=0;
for i=1:(k-1)
clear m1
clear m2
m1=Puls_R(QRS(i):QRS(i+1));
m2=Puls_IR(QRS(i):QRS(i+1));
D1=D1+(max(m1)-min(m1));
D2=D2+(max(m2)-min(m2));
end
D1=D1/(k-1);
D2=D2/(k-1);
a=D2/D1;
SaO2=(0.872-0.16*a)*100/(0.14*a+0.754);
w1=50;
h1=30;
x2=250;
y2=195;
x3=300;
y3=200;
hTxt1=uicontrol('Style','text','String','SaO2=','Position',[x2,y2,w1,h1]);
hEd=uicontrol('Style','edit','Position',[x3,y3,w1,h1]);
set(hEd,'String',num2str(SaO2))
