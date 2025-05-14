from os import listdir, makedirs
from os.path import exists, isdir, isfile, join
from shutil import rmtree, copyfile
from page import generate_page

def copy_files(source:str, destination:str):
    if not source or not destination:
        return
    
    # delete all contents from destination (public)
    if exists(destination):
        print(f"destination exists. lets delete it and recreate {destination}")
        rmtree(destination)
        makedirs(destination, exist_ok = True)
    else:
        print("desination doesn't exist, lets make the folder, or we'll just do that later with the copy")
        makedirs(destination, exist_ok = True)

    traverse_tree(source, destination)

def traverse_tree(source:str, destination:str):
    # copy * from source and paste into destination. IE static to public
    source_contents = listdir(source)
    print("source contents", source_contents)    

    for item in source_contents:
        source_path = join(source, item)
        destination_path = join(destination, item)

        if isfile(source_path):
            print(f"copying file from {source_path} to {destination_path}")
            # copy(source_path, destination_path)
            try:
                copyfile(source_path, destination_path)
            except Exception as e:
                print(f"Error copying {source_path}: {e}")
                # Alternative method if needed
                try:
                    with open(source_path, 'rb') as src_file:
                        with open(destination_path, 'wb') as dst_file:
                            dst_file.write(src_file.read())
                except Exception as e2:
                    print(f"Alternative method failed too: {e2}")

        elif isdir(source_path):
            print(f"copying dir from {source_path} to {destination_path}")
            if not exists(destination_path):
                makedirs(destination_path, exist_ok = True)
            traverse_tree(source_path, destination_path)

def main():
    copy_files("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()