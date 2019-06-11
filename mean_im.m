path_imnames = '/home/ubuntu/Desktop/data250_250/train.txt';
path_images = '/home/ubuntu/Desktop/data250_250/';

fid = fopen(path_imnames);
tline = fgetl(fid);

i=0;
while ischar(tline)
    i = i+1;
    im_name = split(tline," ");
    im_name = im_name{1};
    
    im = imread(fullfile(path_images,im_name));
    ch1 = im(:,:,1);
    ch2 = im(:,:,2);
    ch3 = im(:,:,3);
    MEAN_IMG(i,:) = mean([ch1(:), ch2(:), ch3(:)],1);
    tline = fgetl(fid);
end
fclose(fid);
MEAN_IMG_ = mean(MEAN_IMG,1)