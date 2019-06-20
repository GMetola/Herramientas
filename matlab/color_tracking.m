close all
input_path = './images/';
input = dir(fullfile(input_path, '*.jpg'));
input = input(~[input.isdir]);

L = [29, 43, 126];
H = [126, 255, 255];
square_struct = strel('square',3);
for i = 1:numel(input)
    im_rgb = imread(fullfile(input(i).folder, input(i).name));
    imshow(im_rgb)
    im_hsv = rgb2hsv(im_rgb);
        
    H = (im_hsv(:,:,1) >= L(1)) & (im_hsv(:,:,1) <= H(1)) & (im_hsv(:,:,2) >= L(2)) ...
        & (im_hsv(:,:,2) <= H(2)) & (im_hsv(:,:,3) >= L(3)) & (im_hsv(:,:,3) <= H(3));
    
    mask = imerode(mask, square_struct);
    mask = imerode(mask, square_struct);
    mask = imdilate(mask, square_struct);
    mask = imdilate(mask, square_struct);
    
    region = regionprops(mask, 'Area', 'BoundingBox', 'Centroid');
    if isempty(region(Centroid))
        [rango, lapiz] = max([region.Area]);
        caja = region(lapiz).BoundingBox;
        centro = region(lapiz).Centroid;
        hold on
        rectangle('Position',caja)
    end
end