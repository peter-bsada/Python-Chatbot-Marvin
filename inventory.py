"""
code for backpack
"""
filename = "inv.data"

def readfile():
    """
    read from file
    """
    with open(filename) as filehandle:
        content = filehandle.read()
        print(content)
    return content

def write_to_file(content, mode):
    """
    write to the file
    """
    with open(filename, mode) as filehandle:
        filehandle.write(content + "\n")

def remove_item(remove):
    """
    Remove an item from the filename
    """
    content = readfile()

    if remove in content:
        if content.index(remove) == 0:
            modified_content = content.replace(remove, "")
        else:
            modified_content = content.replace("\n" + remove, "")
        write_to_file(modified_content.strip(), "w")
