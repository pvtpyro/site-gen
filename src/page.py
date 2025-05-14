from os import makedirs, mkdir
from blocks import markdown_to_html_node
from os.path import dirname, exists


def extract_title(markdown:str):
    lines = markdown.strip().split("\n")
    for line in lines:
        line = line.strip()
        # print("!!!DEBUG TITLE", line)
        if line.startswith("# "):
            return line[2:]
        raise Exception("No heading level 1 provided")
    
def generate_page(from_path:str, template_path:str, dest_path:str):
    print("-----------------GENERATE PAGE FUNC -----------------")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Read the markdown file at from_path and store the contents in a variable.
    with open(from_path, "r") as file:
        markdown_file = file.read()
    # print('markdown', markdown_file)

    # Read the template file at template_path and store the contents in a variable.
    with open(template_path, "r") as file:
        template_file = file.read()
    # print('template', template_file)

    # Use your markdown_to_html_node function 
    # and .to_html() method to convert the markdown file to an HTML string.
    html_string:str = markdown_to_html_node(markdown_file).to_html()

    # Use the extract_title function to grab the title of the page.
    title = extract_title(markdown_file) or ""

    # Replace the {{ Title }} and {{ Content }} 
    # placeholders in the template with the HTML and title you generated.
    index_content = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    # Write the new full HTML page to a file at dest_path. 
    # Be sure to create any necessary directories if they don't exist.

    # get directory path
    directory = dirname(dest_path)
    # check if directory exists, if not, create it
    print(f"directory needed is {directory}")
    if directory:
        if not exists(directory):
            makedirs(directory, exist_ok=True)
            print("directory didn't exist. I create it")
        else:
            print("directory already exists, lets write the file")

    # write contents to the dest_path
    try:
        with open(dest_path, 'w') as file:
            file.write(index_content)
        print("successfully create page")
    except Exception as e:
        print(f"failed to write file: {e}")
