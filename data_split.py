import os,shutil,random
# main path for data
main_path='/dataset/data/'  # input main data container path
# make dirs for images
image_dir=main_path+'images/'
if os.path.exists(image_dir):
    shutil.rmtree(image_dir)
os.mkdir(image_dir)
# make dirs for labels
label_dir=main_path+'labels/'
if os.path.exists(label_dir):
    shutil.rmtree(label_dir)
os.mkdir(label_dir)
train_img_path=image_dir+'/train'
valid_img_path=image_dir+'/valid'
train_label_path=label_dir+'/train'
valid_label_path=label_dir+'/valid'
os.mkdir(train_img_path)
os.mkdir(valid_img_path)
os.mkdir(train_label_path)
os.mkdir(valid_label_path)
images=[]
extension='.jpg'
split_value=0.9
for m,l,f in os.walk(main_path):
    for file in f:
        if file.endswith(extension):
            file=file[:-4]
            images.append(file)
# reorganize the order of images in the list            
random.shuffle(images)
size=len(images)        
split=int(size*0.9)
train_data=images[:split]
valid_data=images[split:]
print('train data extracting...')
for data in train_data:
    src_img=main_path+data+extension
    shutil.move(src_img,train_img_path)
    src_label=main_path+data+'.txt'
    shutil.move(src_label,train_label_path)
print('validation data exporting...') 
for data in valid_data:
    src_image=main_path+data+extension
    shutil.move(src_image,valid_img_path)
    src_label=main_path+data+'.txt'
    shutil.move(src_label,valid_label_path) 
print('Proccess finished !!!')      