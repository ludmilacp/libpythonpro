import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'ludmila.canfield@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'luciacanfield@gmail.com',
        'Cursos Python Pro',
        'Turma Pytools'
     )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'ludmila']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luciacanfield@gmail.com',
            'Cursos Python Pro',
            'Turma Pytools'
        )
