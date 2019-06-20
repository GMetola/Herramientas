function [] = blurred(in, out)

direct = dir(fullfile(in,'*.jpg'));
% Im = zeros(1,numel(direct));
kernel = randi([1, 3], length(direct));
for k = 1:numel(direct)
    F = fullfile(in,direct(k).name);
    Im = imread(F);
    filename = direct(k).name;

    if kernel(k) == 1
        imblur = imgaussfilt(Im,[5 5]);
    elseif kernel(k) == 2
        imblur = imgaussfilt(Im,[15 15]);
    elseif kernel(k) == 3
        imblur = imgaussfilt(Im,[21 21]);
    end
    imwrite(imblur, fullfile(out,direct(k).name));
end
end