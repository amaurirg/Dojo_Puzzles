ln = {
    'ABC': {'A': '2', 'B': '22', 'C': '222'},
    'DEF': {'D': '3', 'E': '33', 'F': '333'},
    'GHI': {'G': '4', 'H': '44', 'I': '444'},
    'JKL': {'J': '5', 'K': '55', 'L': '555'},
    'MNO': {'M': '6', 'N': '66', 'O': '666'},
    'PQRS': {'P': '7', 'Q': '77', 'R': '777', 'S': '7777'},
    'TUV': {'T': '8', 'U': '88', 'V': '888'},
    'WXYZ': {'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'},
    ' ': {' ': '0'}
}

def nums(palavra: str) -> str:
    if not isinstance(palavra, str):
        raise TypeError("Precisa ser do tipo string.")
    resp = ""
    ln_key = ""
    for p in palavra.upper():
        for key in ln.keys():
            if p in key:
                if key == ln_key:
                    resp += "_"
                ln_key = key
                resp += ln[key][p]
                break
    if resp == "":
        raise ValueError("Somente letras e espaços são permitidos para enviar SMS.")
    return resp
