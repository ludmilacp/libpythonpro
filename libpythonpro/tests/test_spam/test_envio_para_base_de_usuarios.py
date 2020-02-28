from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [Usuario(nome='Renzo', email='renzo@python.pro.br'), Usuario(nome='Luciano', email='renzo@python.pro.br')],
        [Usuario(nome='Renzo', email='renzo@python.pro.br')]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('renzo@python.pro.br', 'curso Python Pro', 'Confira os módulos fantasticos')
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('luciano@python.pro.br', 'curso Python Pro', 'Confira os modulos fantasticos')
    enviador.enviar.assert_called_once_with('luciano@python.pro.br', 'renzo@python.pro.br', 'curso Python Pro',
                                            'Confira os modulos fantasticos')
