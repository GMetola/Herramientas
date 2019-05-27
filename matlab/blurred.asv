clear
in = 'C:\Users\Gabriel\Pictures\Fiestas Eli';
direct = dir(fullfile(in,'*.jpg'));
% Im = zeros(1,numel(direct));
    for k = 1:numel(direct)
        F = fullfile(in,direct(k).name);
        Im = imread(F);
        filename = direct(k).name;
        
        im_5 = imgaussfilt(Im,[5 5]);
        im_15 = imgaussfilt(Im,[15 15]);
        im_21 = imgaussfilt(Im,[21 21]);
        
        imwrite(im5, strcat(filename,'_5x5'));
        imwrite(im5, strcat(filename,'_15x15'));
        imwrite(im5, strcat(filename,'_21x21'));
    end
        