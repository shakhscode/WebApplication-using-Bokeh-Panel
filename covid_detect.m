function covid_detect(f,p)
%% граничный период дыхания
Tgr = 2.5;
%% граничный объём легких
Vgr = 4;
%% для анализа рассматриватеся только первая
%гармоника сигнала
[V0 n] = max(p);
T0 = 1/f(n);
if V0>Vgr
if T0>Tgr
disp('проблемы с легкими не обнаружены')
else
disp('повреждение легких')
end
else
disp('повреждение легких')
end
end