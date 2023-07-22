from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    pass
    assert encrypt_message("Olá Mundo", 1) == (
        "O_odnuM ál"
    )
    assert encrypt_message("Olá Mundo", 7) == (
        "nuM álO_od"
    )
    assert encrypt_message("Olá Mundo", 12) == (
        "odnuM álO"
    )
    assert encrypt_message("Olá Mundo", 15) == (
        "odnuM álO"
    )
    assert encrypt_message("Olá Mundo", -150) == (
        "odnuM álO"
    )

    with pytest.raises(TypeError):
        encrypt_message("Olá Mundo", "8")
        encrypt_message(1892981273, 6)

