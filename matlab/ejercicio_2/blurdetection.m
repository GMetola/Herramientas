function [] = blurdetection(in)
close all
direct = dir(fullfile(in));

for i = 3:length(direct)
    im = imread(fullfile(direct(i).folder, direct(i).name));
    conv = fspecial('laplacian');
    varianza = round(std2(imfilter(im, conv)));
    % menor varianza -> mayor desenfoque
    % umbral de varianza = 90
    figure
    if varianza > 90
        text{1} = ['Valida .Enfoque: ' num2str(varianza)];
    else
        text{1} = ['Ana no sabe hacer fotos .Enfoque: ' num2str(varianza)];
    end
    im = insertText(im, [1 1], text(1), 'FontSize', 10);
    imshow(im);
    waitforbuttonpress;
end
close all
end