import base64, lzma, dis
file = input("[+] Drop file --> ")

def deobf(c:str):
    c=c.split("(base64.b64decode(b'")[1].split("'))")[0]
    shit_code = lzma.decompress(base64.b64decode(c.encode())).decode()
    shit_lzma = shit_code.split("= b'")[1].split("'\n")[0].encode().decode('unicode_escape').encode("raw_unicode_escape")
    shit_lzma = lzma.decompress(shit_lzma).decode()
    code = shit_lzma.replace(".exec","\nimport dis;dis.dis")
    exec(code)
    input()
 
content = open(file,"r").read()
deobf(content)
