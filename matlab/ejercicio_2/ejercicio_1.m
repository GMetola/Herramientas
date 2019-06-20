clear all
close all

no_header = detectImportOptions(fullfile('./', 'groundtruth.csv'),'NumHeaderLines',0);
infer_table = readtable(fullfile('./', 'detection.csv'), no_header);
inference = table2array(infer_table);

ground_table = readtable(fullfile('./', 'groundtruth.csv'), no_header);
ground = table2array(ground_table);

data_count = length(ground);
errors = isnan(ground(:,2));
num_errors = length(errors(errors == 1));

% calculo matricial que elimina los NaNs
clean_data = abs(inference(~errors,:) - ground(~errors,:));
% [a, b, c, d] = abs(inference(~errors,:) - ground(~errors,:));

area_2D = clean_data(:,2);
area_3D = clean_data(:,3);
complexity = clean_data(:,4);

% agrupaciones
bins_2 = [0 , 50, 100, 150, 200, 250, max(area_2D)+1];
bins_3 = [0 , 50, 100, 150, 200, 250, max(area_3D)+1];
bins_c = [0 , 1, 2, 3, max(complexity)+1];

% clasifica en los bins
clasif_2 = discretize(area_2D, bins_2);
clasif_3 = discretize(area_3D, bins_3);
clasif_c = discretize(complexity, bins_c);

area_2 = discretize(area_2D, bins_2);
group_2 = zeros(length(bins_2)-1,1);
for i = 1:length(bins_2)-1
    group_2(i) = length(area_2(area_2 == i));
end

area_3 = discretize(area_3D, bins_3);
group_3 = zeros(length(bins_3)-1,1);
for i = 1:length(bins_3)-1
    group_3(i) = length(area_3(area_3 == i));
end

area_c = discretize(complexity, bins_c);
group_c = zeros(length(bins_c)-1,1);
for i = 1:length(bins_c)-1
    group_c(i) = length(area_c(area_c == i));
end

group_2 = [num_errors; group_2] * 100 / data_count;
group_3 = [num_errors; group_3] * 100 / data_count;
group_c = [num_errors; group_c] * 100 / data_count;

label_2 = {'Nan', '0-50', '50-100', '100-150', '150-200', '200-250', '>250'};
label_3 = label_2;
label_c = {'0' , '1', '2', '3', '>4'};


%% graficas

% area 2d
fig_2 = figure;
bar(1, group_2(1), 'BarWidth', 0.5, 'FaceColor',[0 0 0], 'EdgeColor',[0 0 0]);
hold on
bar(2:length(group_2), group_2(2:end), 'BarWidth', 0.5, 'FaceColor',[1 0 0], 'EdgeColor',[0 0 0]);
title("Area 2D");
set(gca, 'xtick',1:length(group_2), 'xticklabel', label_2);
xlabel('Difference between detection and ground')
ylabel('Percentage of total measures')
ylim([0 100])
saveas(fig_2, "Area_2D.jpg")

% area 3d
fig_3 = figure;
bar(1, group_3(1), 'BarWidth', 0.5, 'FaceColor',[0 0 0], 'EdgeColor',[0 0 0]);
hold on
bar(2:length(group_3), group_3(2:end), 'BarWidth', 0.5, 'FaceColor',[1 0 0], 'EdgeColor',[0 0 0]);
title("Area 3D");
set(gca, 'xtick',1:length(group_3), 'xticklabel', label_3);
xlabel('Difference between detection and ground')
ylabel('Percentage of total measures')
ylim([0 100])
saveas(fig_2, "Area_3D.jpg")

% complexity
fig_c = figure;
bar(1, group_c(1), 'BarWidth', 0.5, 'FaceColor',[0 0 0], 'EdgeColor',[0 0 0]);
hold on
bar(2:length(group_c), group_c(2:end), 'BarWidth', 0.5, 'FaceColor',[1 0 0], 'EdgeColor',[0 0 0]);
title("Complexity");
set(gca, 'xtick',1:length(group_c), 'xticklabel', label_c);
xlabel('Difference between detection and ground')
ylabel('Percentage of total measures')
ylim([0 100])
saveas(fig_2, "Complexity.jpg")