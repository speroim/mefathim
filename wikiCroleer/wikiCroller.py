# import os
# import requests
# import urllib
# from bs4 import BeautifulSoup
# import tqdm
# from os.path import abspath, dirname, exists

# def delete_folder(folder_path):
#     for item in os.listdir(folder_path):
#         item_path = os.path.join(folder_path, item)
#         if os.path.isfile(item_path):
#             os.unlink(item_path)  
#         elif os.path.isdir(item_path):
#             delete_folder(item_path)  
#     os.rmdir(folder_path)  


# def save_img(img, main_dir, title):
#     img_dir = os.path.join(main_dir,title)
#     os.mkdir(img_dir, exist_ok=True)
#     for img_path in img:
#         full_path = 'https:' + img_path
#         response = requests.get(full_path)
#         if requests.status_codes != 200:
#             print("failed to download image!")
#             continue
#         file_name = img_path.rsplit('/',1)[-1]
#         save_path = os.path.join(img_dir,file_name)
#         with open(full_path, 'wb') as file:
#             file.write(response.content)
#         print("image downloaded successfully")


# def get_img(url):
#     min_width, min_height = 5, 5
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     img = []
#     for img_tag in soup.find_all('img'):
#         img_url = img_tag.get('src')
#         img_class = img_tag.get('class')
#         img_width = img_tag.get('width') 
#         img_height = img_tag.get('height')
#         img_class = img_class[0] if img_class is not None else ""
#         img_width =  int(img_width) if img_width is not None else 0
#         img_height = int(img_height) if img_height is not None else 0
#         if img_class == 'mw-file-element' and \
#         img_width >= min_width and img_height >= min_height:
#             img.append(img_url)
#     return img

# def crawler(width, depth, url, main_dir, progress_bar, visited = None):
#     visited = set() if visited is None else visited
#     visited.add(url)

#     #get all img
#     title = url.rsplit("/",1)[-1]
#     img = get_img(url)
#     print(img)
#     save_img(img, main_dir, title)
#     progress_bar.update(1)
#     # if depth > 0:
#     #     links = get_links(url, width, visited)
#     #     for link in links:
#     #         crawler(width, depth - 1, url, main_dir, progress_bar, visited = None)


# def main():
#     width = int(input("enter the width:"))
#     assert width > 0, "must be positive"
#     depth = int(input("enter the depth:"))
#     assert depth >= 0, "must be not negative"

#     main_dir = f"{dirname(abspath(__file__))}/project1" # check 
#     if exists(main_dir):
#         delete_folder(main_dir)
#     else:
#         os.mkdir(main_dir)       

#     random_url = "https://en.wikipedia.org/wiki/Special:Random"
#     response = requests.get(random_url)
#     assert response.status_code == 200, "the connection fail"

#     init_url = response.url
#     print(init_url)
#     progress_bar = tqdm.tqdm(total = width**depth, desc = 'crawling now')
#     crawler(width, depth, init_url, main_dir, progress_bar)
#     progress_bar.close()

# if __name__ == "__main__":
#     main()


import os
from os.path import abspath, dirname, exists
import requests
import urllib
from bs4 import BeautifulSoup
from tqdm import tqdm

def delete_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            os.unlink(item_path)  
        elif os.path.isdir(item_path):
            delete_folder(item_path)  
    os.rmdir(folder_path)  

def get_img(url):
    min_width, min_height = 5, 5
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img = []
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        img_class = img_tag.get('class')
        img_width = img_tag.get('width') 
        img_height = img_tag.get('height')
        img_class = img_class[0] if img_class is not None else ""
        img_width =  int(img_width) if img_width is not None else 0
        img_height = int(img_height) if img_height is not None else 0
        if img_class == 'mw-file-element' and \
        img_width >= min_width and img_height >= min_height:
            img.append(img_url)
    return img

def save_img(img, main_dir, title):
    img_dir = os.path.join(main_dir, title)
    os.makedirs(img_dir, exist_ok=True) 
    for img_path in img:
        full_path = "https:" + img_path
        response = requests.get(full_path)
        if response.status_code != 200:
            continue
        file_name = img_path.rsplit('/',1)[-1]
        save_path = os.path.join(img_dir, file_name)
        with open (save_path, 'wb') as file:
            file.write(response.content)

        

def crawler(width, depth, url, main_dir, progress_bar, visited = None):
    visited = set() if visited is None else visited
    visited.add(url)

    title = url.rsplit("/", 1)[1]
    img = get_img(url)
    print(img)
    save_img(img, main_dir, title)
    progress_bar.update(1)

    # if depth > 0:
    #     links = get_links(url, width, visited)
    #     for link in links:
    #         crawler(width, depth -1, link, main_dir, progress_bar, visited)


def main():
    width = int(input("Please enter a number for width search: "))
    assert width > 0, "width must be a positive number."
    depth = int(input("Please enter a number for depth search: "))
    assert depth >= 0, "width must be a none negative number."

    main_dir = f"{dirname(abspath(__file__))}/result" 
    if exists(main_dir):
        delete_folder(main_dir) 
    os.mkdir(main_dir)
    random_url =  "https://en.wikipedia.org/wiki/Special:Random"
    response = requests.get(random_url)
    assert response.status_code == 200, "The connection fail."
    init_url = response.url
    progress_bar = tqdm(total= width**depth, desc= 'crawling now')
    print(f"""response: {response}
           init: {init_url}""")
    crawler(width, depth, init_url, main_dir, progress_bar)

    progress_bar.close()


if __name__ == "__main__":
    main()


    
