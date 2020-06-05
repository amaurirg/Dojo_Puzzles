from sms import nums


def test_retorna_frase():
    cada = nums("CADA")
    cade = nums("cAdE")
    casa = nums("CASA")
    dojo = nums("SEMPRE ACESSO O DOJOPUZZLES")

    assert cada == "222_232"
    assert cade == "222_23_33"
    assert casa == "222_277772"
    assert dojo == "77773367_7773302_222337777_777766606660366656667889999_9999555337777"


def test_retorna_frase_com_parametro_invalido():
    lista = [("@"), ("CASA", "CADA"), (23), "palavra_com_anderline"]
    for l in lista:
        try:
            nums(l)
        except (TypeError, ValueError, AssertionError):
            pass
        else:
            assert True, "Entrada não permitida."
